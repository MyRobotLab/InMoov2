angular.module('mrlapp.service.InMoov2HeadGui', []).controller('InMoov2HeadGuiCtrl', ['$scope', '$log', 'mrl', function($scope, $log, mrl) {
    $log.info('InMoov2HeadGuiCtrl')
    var _self = this
    var msg = this.msg
    $scope.servos = []
    $scope.sliders = []
    $scope.controller = null
    $scope.pinsList = []
    $scope.pin = null
    $scope.possibleController = null

    $scope.mrl = mrl
    
    $scope.activePanel = 'head'
    $scope.toggleValue = true

    $scope.filterPeers = function(peerName) {
        if (peerName) {
            mrl.search($scope.service.name + '.' + peerName)
        } else {
            mrl.search("")
        }
    }        

    // GOOD TEMPLATE TO FOLLOW
    this.updateState = function(service) {
        $scope.service = service
        
        if (service.controller != null) {
            $scope.possibleController = service.controller
        }
        $scope.controller = service.controller
        $scope.pin = service.pin
        $scope.pinList = service.pinList
    }

    $scope.toggle = function(servo) {
        $scope.sliders[servo].tracking = !$scope.sliders[servo].tracking
    }

    _self.onSliderChange = function(servo){
        if (!$scope.sliders[servo].tracking){
            msg.sendTo(servo, 'moveTo', $scope.sliders[servo].value)
        }
    }   

    $scope.setActive = function(val) {
        var index = array.indexOf(5);
        if (index > -1) {
            array.splice(index, 1);
        }
    }

    $scope.getPeer = function(peerName) {
        let s = mrl.getService($scope.service.name + '.' + peerName + '@' + this.service.id)
        return s
    }

    $scope.setPanel = function(panelName) {
        $scope.activePanel = panelName
        buttonOn(panelName)
    }

    $scope.showPanel = function(panelName) {
        return $scope.activePanel == panelName
    }        

    this.updateState($scope.service)

    this.onMsg = function(inMsg) {
        switch (inMsg.method) {
        case 'onState':
            _self.updateState(inMsg.data[0])
            $scope.$apply()
            break
        case 'onServoData':
            var data = inMsg.data[0];
            $scope.sliders[data.name].value = data.pos;
            $scope.$apply()
            break
        case 'onStatus':
            $scope.status = data
            $scope.$apply()
            break
        case 'addListener':
            // wtf?
            $log.info("Add listener called")
            $scope.status = data
            $scope.$apply()
            break    
        case 'onMetaData':
            // servos sliders are either in "tracking" or "control" state
            // "tracking" they are moving from callback position info published by servos
            // "control" they are sending control messages to the servos
            $scope.servos = inMsg.data[0]
            for (var servo of $scope.servos) {
                // dynamically build sliders
                $scope.sliders[servo] = {                    
                    value: 0,
                    tracking: true,
                    options: {
                        id: servo,
                        floor: 0,
                        ceil: 180,
                        onStart: function(id) {},
                        onChange: function(id) {
                            _self.onSliderChange(id)
                        },
                        /*
                        onChange: function() {
                            if (!this.tracking) {
                                // if not tracking then control
                                msg.sendTo(servo, 'moveToX', sliders[servo].value)
                            }
                        },*/
                        onEnd: function(id) {}
                    }
                }
                // dynamically add callback subscriptions
                // these are "intermediate" subscriptions in that they
                // don't send a subscribe down to service .. yet 
                // that must already be in place (and is in the case of Servo.publishServoData)
                msg.subscribeTo(_self, servo, 'publishServoData')

            }
            $scope.$apply()
            break
        default:
            $log.error("ERROR - unhandled method " + $scope.name + " " + inMsg.method)
            break
        }
    }

    $scope.isAttached = function() {
        return $scope.service.controller != null
    }

    $scope.setPin = function(inPin) {
        $scope.pin = inPin
    }

    $scope.setSelectedController = function(name) {
        $log.info('setSelectedController - ' + name)
        $scope.selectedController = name
        $scope.controller = name
    }    

    $scope.attachController = function() {
        $log.info("attachController")

        // FIXME - there needs to be some updates to handle the complexity of taking updates from the servo vs
        // taking updates from the UI ..  some of this would be clearly solved with a (control/status) button

        let pos = $scope.pos.value;
        // currently taken from the slider's value :P - not good if the slider's value is not good :(

        msg.send('attach', $scope.possibleController, $scope.pin, pos)
        // $scope.rest) <-- previously used rest which is (not good)
        // msg.attach($scope.controller, $scope.pin, 90)
    }

    msg.subscribe("getMetaData")
    msg.send('getMetaData')
    msg.subscribe(this)
}
])
