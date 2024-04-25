angular.module('mrlapp.service.InMoov2Gui', []).controller('InMoov2GuiCtrl', ['$scope', 'mrl', '$uibModal', 'modalService', 'peer', function($scope, mrl, $uibModal, modalService, peer) {
    console.info('InMoov2GuiCtrl')
    var _self = this
    var msg = this.msg
    var init = true

    let numCircularButtons = 0
    // this is circle center - it needs to be
    // dynamically calculated from size of background and radius
    let centerX = 238
    let centerY = 226
    let radius = 215

    let firstTime = true

    $scope.batteryLevel = 0
    $scope.currentState = "boot"
    $scope.systemEvent = null

    $scope.peer = peer
    $scope.mrl = mrl
    $scope.peerConfig = {}

    $scope.selected = {
        configName: "default",
    }

    $scope.servos = []
    $scope.sliders = []

    $scope.mrl = mrl
    $scope.panel = mrl.getPanel('runtime')
    $scope.msg = msg

    // text published from InMoov2 service
    $scope.onText = null
    $scope.languageSelected = null
    $scope.speakText = null
    $scope.toggleValue = true
    
    $scope.speechType = 'MarySpeech'

    $scope.activePanel = 'settings'

    $scope.speechTypes = null
    $scope.mouth = null

    $scope.selectedButton = {}

    $scope.selectedGesture = null
    $scope.selectedConfig = null

    $scope.configList = mrl.getService('runtime').configList

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
            button.translate = x + "px," + y + "px"
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
    $scope.deleteConfig = function() {
        console.info('deleteConfig', $scope.selected.configName)
        msg.sendTo('runtime', 'deleteConfig', $scope.selected.configName)
        $scope.selected.configName = null; 
    }

    $scope.startConfig = function() {
        console.info('startConfig', $scope.selected.configName)
        msg.sendTo('runtime', 'startConfig', $scope.selected.configName)
    }

    $scope.releaseConfig = function() {
        console.info('releaseConfig', $scope.selected.configName)
        msg.sendTo('runtime', 'releaseConfig', $scope.selected.configName)
    }

    $scope.saveConfig = function() {
        console.info('saveConfig')

        let onOK = function() {
            msg.sendTo('runtime', 'setConfig', $scope.selected.configName)
            msg.sendTo('runtime', 'saveConfig', $scope.selected.configName)
            msg.sendTo('runtime', 'getConfigName')
        }

        let onCancel = function() {
            console.info('save config cancelled')
        }

        let ret = modalService.openOkCancel('widget/modal-dialog.view.html', 'Save Configuration', 'Save your current configuration in a directory named', onOK, onCancel, $scope);
        console.info('ret ' + ret);
    }

    $scope.getResponse = function(utterance) {
        msg.send('getResponse', utterance)
        $scope.utterance = ""
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

    $scope.peerState = function(peerKey) {
        $scope.service.serviceType.peers[peerKey].state
    }

    // GOOD TEMPLATE TO FOLLOW
    this.updateState = function(service) {
        $scope.service = service

        $scope.service.configName = mrl.getService('runtime').configName
        $scope.languageSelected = service.locale.tag
        $scope.mouth = mrl.getService(service.name + '.mouth')

        if (firstTime){
            mrl.changeTab(service.name)
            firstTime = false
        }
        
        $scope.$apply()
    }

    $scope.getShortName = function(longName) {
        return longName.substring(longName.lastIndexOf(".") + 1)
    }

    $scope.toggle = function(servo) {
        $scope.sliders[servo].tracking = !$scope.sliders[servo].tracking
    }

    $scope.startPeer = function(peerKey) {
        console.info(peerKey)
        console.info($scope.msg)
        msg.send('startPeer', peerKey)
    }

    $scope.startMouth = function() {
        msg.send('startPeer', 'mouth')
        msg.send('startPeer', 'htmlFilter')
    }

    $scope.stopMouth = function() {
        msg.send('releasePeer', 'mouth')
        msg.send('releasePeer', 'htmlFilter')
    }

    $scope.releasePeer = function(peerKey) {
        console.info(peerKey)
        msg.send('releasePeer', peerKey)
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
        case 'onPeerConfig':
            console.info(data)
            // $scope.peerConfig
            $scope.$apply()
            break
        case 'onState':
            _self.updateState(data)
            $scope.$apply()
            break
        case 'onStateChange':
            $scope.service.state = data.state
            $scope.$apply()
            break
        case 'onSystemEvent':
            $scope.systemEvent = data
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
        case 'onBatteryLevel':
            $scope.batteryLevel = data;
            $scope.$apply()
            break
        case 'onVoices':
            $scope.service.voices = data
            $scope.$apply()
            break
        case 'onPeerStarted':
            if (data == 'mouth') {
                let actualName = $scope.service.serviceType.peers[data].actualName
                mrl.subscribe(actualName, 'getVoices')
                mrl.subscribeToServiceMethod(_self.onMsg, actualName, 'getVoices');
                msg.sendTo(actualName, 'getVoices')
            }
            $scope.$apply()
            break
        case 'onConfigList':
            $scope.configList = data
            $scope.$apply()
            break
        case 'onStatus':
            break

        default:
            console.error("ERROR - unhandled method " + $scope.name + " " + inMsg.method)
            break
        }
    }

    $scope.setConfig = function() {
        console.info('setConfig', $scope.selected.configName)
        msg.sendTo('runtime', 'setConfig', $scope.selected.configName)
        msg.sendTo('runtime', 'getConfig')
    }

    

    $scope.loadGestures = function() {
        console.info('loadGestures')
        msg.send('loadGestures')
    }

    $scope.execScript = function(resourceScript) {
        console.info('execScript')
        msg.send('execScript', resourceScript)
    }    

    $scope.setSpeechType = function(){
        msg.send('setSpeechType', $scope.service.config.peers['mouth'].type)
    }

    $scope.setConfigValue = function(fieldname, value){
        msg.send('setConfigValue', fieldname, value)
        msg.send('broadcastState')
    }

    $scope.setPeerConfigValue = function(peerkey, fieldname, value){
        msg.send('setPeerConfigValue', peerkey, fieldname, value)
        msg.send('broadcastState')
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

    addButton('InMoov', 'absolute', 157, 150)

    calculatButtonPos()

    $scope.setPanel('InMoov')

    msg.subscribe('publishConfigList')

    runtimeFull = mrl.getRuntime().name

    // FIXME FIXME FIXME - single simple subscribeTo(name, method) !!!
    mrl.subscribe(mrl.getRuntime().name, 'getServiceTypeNamesFromInterface');
    mrl.subscribeToServiceMethod(_self.onMsg, mrl.getRuntime().name, 'getServiceTypeNamesFromInterface');

    msg.subscribe('onStateChange')
    msg.subscribe('publishSystemEvent')

    msg.subscribe('publishStateChange')
    msg.subscribe('getPeerConfig')
    msg.subscribe('publishText')
    msg.subscribe('publishPeerStarted')
    msg.subscribe('publishBatteryLevel')
    msg.sendTo(mrl.getRuntime().name, 'getServiceTypeNamesFromInterface', 'SpeechSynthesis')
    msg.sendTo(mrl.getRuntime().name, 'publishConfigList')
    msg.send('getPeerConfig', 'opencv')
    msg.subscribe(this)
    
}
])
