angular.module('mrlapp.service.InMoov2Gui', []).controller('InMoov2GuiCtrl', ['$scope', 'mrl', function($scope, mrl) {
    console.info('InMoov2GuiCtrl')
    var _self = this
    var msg = this.msg

    let numCircularButtons = 0
    // this is circle center - it needs to be
    // dynamically calculated from size of background and radius
    let centerX = 238
    let centerY = 226
    let radius = 215

    $scope.servos = []
    $scope.sliders = []

    $scope.mrl = mrl

    // text published from InMoov2 service
    $scope.onText = null
    $scope.languageSelected = null
    $scope.speakText = null
    $scope.toggleValue = true

    $scope.activePanel = 'settings'

    $scope.speechTypes = null
    $scope.mouth = null

    $scope.selectedButton = {}

    $scope.selectedGesture = null

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

    let calculatButtonPos = function() {
        let angle = 234.5 * (Math.PI / 180)
        // (360 - 90) * (Math.PI / 180)
        let dangle = (360 / numCircularButtons) * (Math.PI / 180)
        for (i = 0; i < $scope.buttons.length; i++) {
            if ($scope.buttons[i].type == 'circular') {
                angle += dangle
                // $scope.buttons[i].rotate = angle + "deg"
                let x = Math.round(centerX + radius * Math.cos(angle));
                let y = Math.round(centerY + radius * Math.sin(angle));
                $scope.buttons[i].translate = x + "px," + y + "px"
            }
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

    $scope.executeGesture = function(gesture) {
        msg.send('execGesture', gesture);
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

    $scope.startMouth = function() {
        msg.send('setSpeechType', $scope.speechTypeSelected)
        msg.send('startMouth')
    }

    $scope.speak = function() {
        if ($scope.mouth == null) {
            $scope.startMouth()
        }
        msg.send('speakBlocking', $scope.speakText)
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
    addButton('brain', 'circular')
    addButton('mouth', 'circular')
    addButton('head', 'circular')
    addButton('torso', 'circular')
    addButton('extra', 'circular')
    addButton('leg', 'circular')
    addButton('sensor', 'circular')
    addButton('arm', 'circular')
    addButton('hand', 'circular')
    addButton('ear', 'circular')

    //addButton('InMoov', 'absolute', 157, 150)
    //addButton('battery', 'absolute', 22, 484)
    addButton('back', 'absolute', 22, 520)
    //----Glowing body parts for Activated purpose
    //addButton('handR', 'absolute', 141, 199)
    //addButton('handL', 'absolute', 392, 199)
    //addButton('headA', 'absolute', 284, 145)
    //addButton('armR', 'absolute', 191, 183)
    //addButton('armL', 'absolute', 315, 183)
    //addButton('legL', 'absolute', 304, 262)
    //addButton('legR', 'absolute', 275, 262)
    //addButton('torsoA', 'absolute', 278, 216)
    //---Arm-----------------
    //addButton('rightArm', 'absolute', 60, 30)
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

    calculatButtonPos()

    $scope.setPanel('InMoov')

    // FIXME FIXME FIXME - single simple subscribeTo(name, method) !!!
    mrl.subscribe(mrl.getRuntime().name, 'getServiceTypeNamesFromInterface');
    mrl.subscribeToServiceMethod(_self.onMsg, mrl.getRuntime().name, 'getServiceTypeNamesFromInterface');

    msg.subscribe('publishText')
    msg.sendTo(mrl.getRuntime().name, 'getServiceTypeNamesFromInterface', 'SpeechSynthesis')
    msg.subscribe(this)
}
])
