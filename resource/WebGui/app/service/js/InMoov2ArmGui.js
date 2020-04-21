angular.module('mrlapp.service.InMoov2ArmGui', []).controller('InMoov2ArmGuiCtrl', ['$scope', 'mrl', function($scope, mrl) {
    console.info('InMoov2ArmGuiCtrl')
    var _self = this
    var msg = this.msg

    $scope.mrl = mrl
    $scope.panel = mrl.getPanel('runtime')

    // text published from InMoov2 service
    $scope.onText = null
    $scope.languageSelected = null
    $scope.speakText = null

    $scope.activePanel = 'arm'

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


        $scope.buttons.push(button)
    }

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

    // circular main menu buttons

    //addButton('arm', 'circular')

    //---Arm-----------------
    //addButton('rightArm', 'absolute', 343, 30)
    //addButton('rightArm.omoplate', 'absolute', 60, 410)
    //addButton('rightArm.shoulder', 'absolute', 10, 355)
    //addButton('rightArm.rotate', 'absolute', 60, 105)
    //addButton('rightArm.bicep', 'absolute', 10, 160)

    //addButton('leftArm', 'absolute', 343, 30)
    //addButton('leftArm.omoplate', 'absolute', 343, 410)
    //addButton('leftArm.shoulder', 'absolute', 395, 355)
    //addButton('leftArm.rotate', 'absolute', 343, 105)
    //addButton('leftArm.bicep', 'absolute', 395, 160)
    //addButton('redBlink', 'absolute', 193, 216)


    $scope.setPanel('arm')

    // FIXME FIXME FIXME - single simple subscribeTo(name, method) !!!
    mrl.subscribe(mrl.getRuntime().name, 'getServiceTypeNamesFromInterface');
    mrl.subscribeToServiceMethod(_self.onMsg, mrl.getRuntime().name, 'getServiceTypeNamesFromInterface');

    msg.subscribe('publishText')
    msg.sendTo(mrl.getRuntime().name, 'getServiceTypeNamesFromInterface', 'SpeechSynthesis')
    msg.subscribe(this)
}
])
