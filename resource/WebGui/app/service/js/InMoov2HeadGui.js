angular.module('mrlapp.service.InMoov2HeadGui', []).controller('InMoov2HeadGuiCtrl', ['$scope', '$log', 'mrl', function($scope, $log, mrl) {
    $log.info('InMoov2HeadGuiCtrl')
    var _self = this
    var msg = this.msg

    $scope.mrl = mrl
    $scope.panel = mrl.getPanel('runtime')
    
    $scope.activePanel = 'head'

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

        // unselect active buttons by removing active class
        var container = document.querySelector("#containerHead2");
        if (container!=null) {
            var matchesItems = container.querySelectorAll(".dotHeadActive");
            for (var i = 0; i < matchesItems.length; i++) { matchesItems[i].classList.remove('dotHeadActive'); }

            var matchesItems = container.querySelectorAll(".dotHeadButtonsActive");
            for (var i = 0; i < matchesItems.length; i++) { matchesItems[i].classList.remove('dotHeadButtonsActive'); matchesItems[i].classList.add('dotHeadButtons'); }
        }     

        // add activ class to dot ans button object
        if (document.querySelector("#"+panelName+"Dot")!=null) {
            document.querySelector("#"+panelName+"Dot").classList.add('dotHeadActive');
            document.querySelector("#"+panelName+"Button").classList.add('dotHeadButtonsActive');
        }   

    }

    $scope.showPanel = function(panelName) {
        return $scope.activePanel == panelName
    }        

    this.updateState($scope.service)

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

    // FIXME FIXME FIXME - single simple subscribeTo(name, method) !!!
    mrl.subscribe(mrl.getRuntime().name, 'getServiceTypeNamesFromInterface');
    mrl.subscribeToServiceMethod(_self.onMsg, mrl.getRuntime().name, 'getServiceTypeNamesFromInterface');
    msg.subscribe(this)

    msg.subscribe('publishText')
    msg.sendTo(mrl.getRuntime().name, 'getServiceTypeNamesFromInterface', 'SpeechSynthesis')
    msg.subscribe(this)
}
])

