angular.module('mrlapp.service.InMoov2ArmGui', []).controller('InMoov2ArmGuiCtrl', ['$scope', 'mrl', function($scope, mrl) {
    console.info('InMoov2ArmGuiCtrl')
    var _self = this
    var msg = this.msg

    $scope.mrl = mrl
    $scope.panel = mrl.getPanel('runtime')

    $scope.activePanel = 'arm'

    $scope.isRight = function() {
        if ($scope.service){
            return $scope.service.name.includes("right")
        }
        return false
    }

    $scope.isLeft = function() {
        if ($scope.service){
            return $scope.service.name.includes("left")
        }
        return false
    }    

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
        $scope.languageSelected = service.locale.tag
        $scope.mouth = mrl.getService(service.name + '.mouth')
        $scope.$apply()
    }

    $scope.getShortName = function(longName) {
        return longName.substring(longName.lastIndexOf(".") + 1)
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

        // unselect active buttons by removing active class
        var container = document.querySelector("#containerArm2");
        if (container!=null) {
            var matchesItems = container.querySelectorAll(".dotArmActive");
            for (var i = 0; i < matchesItems.length; i++) { matchesItems[i].classList.remove('dotArmActive'); }

            var matchesItems = container.querySelectorAll(".dotArmButtonsActive");
            for (var i = 0; i < matchesItems.length; i++) { matchesItems[i].classList.remove('dotArmButtonsActive'); matchesItems[i].classList.add('dotArmButtons');}
        }     

        // add activ class to dot ans button object
        if (document.querySelector("#"+panelName+"Dot")!=null) {
            document.querySelector("#"+panelName+"Dot").classList.add('dotArmActive');
            document.querySelector("#"+panelName+"Button").classList.add('dotArmButtonsActive');
        }   

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


    $scope.setPanel('arm')

    // FIXME FIXME FIXME - single simple subscribeTo(name, method) !!!
    mrl.subscribe(mrl.getRuntime().name, 'getServiceTypeNamesFromInterface');
    mrl.subscribeToServiceMethod(_self.onMsg, mrl.getRuntime().name, 'getServiceTypeNamesFromInterface');

    msg.subscribe('publishText')
    msg.subscribe(this)
}
])
