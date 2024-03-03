angular.module('mrlapp.service.InMoov2HeadGui', []).controller('InMoov2HeadGuiCtrl', ['$scope', '$log', 'mrl', function($scope, $log, mrl) {
    $log.info('InMoov2HeadGuiCtrl')
    var _self = this
    var msg = this.msg

    $scope.mrl = mrl
    $scope.panel = mrl.getPanel('runtime')
    $scope.state = {
        version: "V2",
        styleSheet: "../service/css/InMoov2HeadGuiV2.css"
    }

    $scope.activePanel = 'head'

    $scope.filterPeers = function(peerName) {
        if (peerName) {
            mrl.search($scope.service.name + '.' + peerName)
        } else {
            mrl.search("")
        }
    }

    $scope.toggleVersion = function() {
        $scope.state.styleSheet = ($scope.state.version == "V1") ? "../service/css/InMoov2HeadGuiV2.css" : "../service/css/InMoov2HeadGui.css"
        $scope.state.version = ($scope.state.version == "V1") ? "V2" : "V1"
    }


    // GOOD TEMPLATE TO FOLLOW
    this.updateState = function(service) {
        $scope.service = service
    }


    $scope.getPeer = function(peerName) {
        let s = mrl.getService($scope.service.name + '.' + peerName + '@' + this.service.id)
        return s
    }

    $scope.setPanel = function(panelName) {
        $scope.activePanel = panelName

        // unselect active buttons by removing active class
        var container = document.querySelector("#containerHead2");
        if (container != null) {
            var matchesItems = container.querySelectorAll(".dotHeadActive");
            for (var i = 0; i < matchesItems.length; i++) {
                matchesItems[i].classList.remove('dotHeadActive');
            }

            var matchesItems = container.querySelectorAll(".dotHeadButtonsActive");
            for (var i = 0; i < matchesItems.length; i++) {
                matchesItems[i].classList.remove('dotHeadButtonsActive');
                matchesItems[i].classList.add('dotHeadButtons');
            }
        }

        // add activ class to dot ans button object
        if (document.querySelector("#" + panelName + "Dot") != null) {
            document.querySelector("#" + panelName + "Dot").classList.add('dotHeadActive');
            document.querySelector("#" + panelName + "Button").classList.add('dotHeadButtonsActive');
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

        default:
            console.error("ERROR - unhandled method " + $scope.name + " " + inMsg.method)
            break
        }
    }

    msg.subscribe(this)
}
])
