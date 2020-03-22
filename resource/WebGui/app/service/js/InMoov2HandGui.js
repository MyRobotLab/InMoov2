angular.module('mrlapp.service.InMoov2HandGui', []).controller('InMoov2HandGuiCtrl', ['$scope', 'mrl', function($scope, mrl) {
    console.info('InMoov2HandGuiCtrl')
    var _self = this
    var msg = this.msg


    $scope.servos = []
    $scope.sliders = []

    $scope.mrl = mrl

    // text published from InMoov2 service
    $scope.onText = null
    $scope.toggleValue = true

    $scope.activePanel = 'settings'

    $scope.selectedButton = {}

    // inmoov "all" buttons
    $scope.buttons = []

    // add a generalized button
    let addButton = function(name, type, x, y) {

        let button = {
            name: name,
            type: type,
            translate: "0px,0px",
            img: "img/InMoov2/" + name + "_off.png",
            hover: "img/InMoov2/" + name + "_hover.png"
        }

        if (type == 'absolute') {
            button.translate = x + "px," + y +"px"
        }

        if (type == 'circular') {
            numCircularButtons++
        }

        $scope.buttons.push(button)
    }

    $scope.filterPeers = function(peerName) {
        if (peerName) {
            mrl.search($scope.service.name + '.' + peerName)
        } else {
            mrl.search("")
        }
    }


    let buttonsOff = function() {
        for (i = 0; i < $scope.buttons.length; i++) {
            $scope.selectedButton.name = name
            $scope.selectedButton.translate = $scope.buttons[i].translate
            $scope.selectedButton.img = "img/InMoov2/" + name + "_off.png"
        }
    }

    let buttonOn = function(name) {
        buttonsOff()
        for (i = 0; i < $scope.buttons.length; i++) {
            if ($scope.buttons[i].name == name) {
                $scope.selectedButton.name = name
                $scope.selectedButton.translate = $scope.buttons[i].translate
                $scope.selectedButton.img = "img/InMoov2/" + name + "_Activ.png"
                break
            }
        }
    }

    // GOOD TEMPLATE TO FOLLOW
    this.updateState = function(service) {
        $scope.service = service
        $scope.languageSelected = service.locale.tag
        $scope.mouth = mrl.getService(service.name + '.mouth')
        $scope.$apply()
    }

    $scope.getShortName = function(longName) {
        return longName.substring(longName.lastIndexOf(".") + 1)
    }

    $scope.toggle = function(servo) {
        $scope.sliders[servo].tracking = !$scope.sliders[servo].tracking
    }

    _self.onSliderChange = function(servo) {
        if (!$scope.sliders[servo].tracking) {
            msg.sendTo(servo, 'moveTo', $scope.sliders[servo].value)
        }
    }

    $scope.active = ["btn", "btn-default", "active"]


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

    this.onMsg = function(inMsg) {
        let data = inMsg.data[0];

        switch (inMsg.method) {
        case 'onState':
            _self.updateState(data)
            $scope.$apply()
            break
        case 'onServiceTypeNamesFromInterface':
            $scope.speechTypes = data.serviceTypes;
            $scope.$apply()
            break
        case 'onText':
            $scope.onText = data;
            $scope.$apply()
            break
            
        default:
            console.error("ERROR - unhandled method " + $scope.name + " " + inMsg.method)
            break
        }
    }

    // circular main menu buttons

    //addButton('arm', 'circular')

    //---Hand-----------------

    //---FIXME------------------
    addButton('rightHand', 'absolute', 60, 30)
    //----Hand sensor
    //addButton('leftHandSensor', 'absolute', 60, 30)
    //addButton('leftThumbSensor', 'absolute', 103, 107)
    //addButton('leftIndexSensor', 'absolute', 73, 138)
    //addButton('leftMajeureSensor', 'absolute', 36, 170)
    //addButton('leftRingFingerSensor', 'absolute', 0, 203)
    //addButton('leftPinkySensor', 'absolute', -3, 238)

    //addButton('rightHandSensor', 'absolute', 343, 30)
    //addButton('rightThumbSensor', 'absolute', 293, 107)
    //addButton('rightIndexSensor', 'absolute', 323, 138)
    //addButton('rightMajeureSensor', 'absolute', 360, 170)
    //addButton('rightRingFingerSensor', 'absolute', 393, 203)
    //addButton('rightPinkySensor', 'absolute', 401, 238)


    $scope.setPanel('hand')

    // FIXME FIXME FIXME - single simple subscribeTo(name, method) !!!
    mrl.subscribe(mrl.getRuntime().name, 'getServiceTypeNamesFromInterface');
    mrl.subscribeToServiceMethod(_self.onMsg, mrl.getRuntime().name, 'getServiceTypeNamesFromInterface');

    msg.subscribe('publishText')
    msg.sendTo(mrl.getRuntime().name, 'getServiceTypeNamesFromInterface', 'SpeechSynthesis')
    msg.subscribe(this)
}
])
