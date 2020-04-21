angular.module('mrlapp.service.InMoov2HandGui', []).controller('InMoov2HandGuiCtrl', ['$scope', 'mrl', function($scope, mrl) {
    console.info('InMoov2HandGuiCtrl')
    var _self = this
    var msg = this.msg

    $scope.mrl = mrl
    $scope.panel = mrl.getPanel('runtime')

    // text published from InMoov2 service
    $scope.onText = null

    $scope.activePanel = 'hand'

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
        var container = document.querySelector("#containerHand2");
        if (container!=null) {
            var matchesItems = container.querySelectorAll(".dotHandActive");
            for (var i = 0; i < matchesItems.length; i++) { matchesItems[i].classList.remove('dotHandActive'); }

            var matchesItems = container.querySelectorAll(".dotHandButtonsActive");
            for (var i = 0; i < matchesItems.length; i++) { matchesItems[i].classList.remove('dotHandButtonsActive'); matchesItems[i].classList.add('dotHandButtons');}
        }     

        // add activ class to dot ans button object
        if (document.querySelector("#"+panelName+"Dot")!=null) {
            document.querySelector("#"+panelName+"Dot").classList.add('dotHandActive');
            document.querySelector("#"+panelName+"Button").classList.add('dotHandButtonsActive');
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

    //$scope.setPanel('leftHand')
    //$scope.setPanel('rightHand')

    // FIXME FIXME FIXME - single simple subscribeTo(name, method) !!!
    mrl.subscribe(mrl.getRuntime().name, 'getServiceTypeNamesFromInterface');
    mrl.subscribeToServiceMethod(_self.onMsg, mrl.getRuntime().name, 'getServiceTypeNamesFromInterface');

    msg.subscribe('publishText')
    msg.subscribe(this)
}
])
