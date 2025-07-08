##############################################################
# MyRobotLab configuration file
# This file is generated from a running instance of MyRobotLab.
# It is meant to get MyRobotLab as close to that instance's state a possible.
# This file can be generated at any time using Runtime.save(filename)
# More information @ http://myrobotlab.org and https://github.com/myrobotlab

##############################################################
## imports ####
from org.myrobotlab.net import BareBonesBrowserLaunch
import time
import org.myrobotlab.framework.Platform as Platform
import org.myrobotlab.service.Runtime as Runtime

# InMoov2 Config : i01
i01 = runtime.start('i01', 'InMoov2')
i01.setVirtual(False)
i01.setMute(False)

rightPort = "COM4"
leftPort = "COM5"
controller3Port = "COM6"
##############################################################
## creating 69 services ####
# Although runtime.start(name,type) both creates and starts services it might be desirable on creation to
# substitute peers, types or references of other sub services before the service is "started"
# e.g. i01 = Runtime.create('i01', 'InMoov') # this will "create" the service and config could be manipulated before starting 
# e.g. i01_left = Runtime.create('i01.left', 'Ssc32UsbServoController')
##############################################################
RuningFolder="resource/InMoov2"
# libraries import
execfile(RuningFolder+'/system/Import_Libraries.py')
# common functions
execfile(RuningFolder+'/system/Import_Functions.py')

RuningFolder=os.getcwd().replace("\\", "/")+"/"+RuningFolder+"/"
# global vars import
execfile(RuningFolder+'/system/Robot_Satus_GlobalsVars.py')
##############################################################

runtime = Runtime.getInstance()
runtime.setAllLocales('en-US')
#i01_jme = runtime.start('i01.jme', 'JMonkeyEngine')
i01_servoMixer = runtime.start('i01.servoMixer', 'ServoMixer')
i01_leftArm_rotate = runtime.start('i01.leftArm.rotate', 'Servo')
i01_torso_topStom = runtime.start('i01.torso.topStom', 'Servo')
i01_rightArm_bicep = runtime.start('i01.rightArm.bicep', 'Servo')
security = runtime.start('security', 'Security')
i01_head_rollNeck = runtime.start('i01.head.rollNeck', 'Servo')
i01_leftHand = runtime.start('i01.leftHand', 'InMoov2Hand')
i01_rightHand_ringFinger = runtime.start('i01.rightHand.ringFinger', 'Servo')
# MoveEyesTimer = runtime.start('MoveEyesTimer', 'Clock')
i01_leftHand_majeure = runtime.start('i01.leftHand.majeure', 'Servo')
i01_leftHand_index = runtime.start('i01.leftHand.index', 'Servo')
i01_rightHand_majeure = runtime.start('i01.rightHand.majeure', 'Servo')
i01_head_eyeX = runtime.start('i01.head.eyeX', 'Servo')
i01_right_serial = runtime.start('i01.right.serial', 'Serial')
python = runtime.start('python', 'Python')
i01_rightHand_index = runtime.start('i01.rightHand.index', 'Servo')
i01_rightHand = runtime.start('i01.rightHand', 'InMoov2Hand')
i01_leftArm_bicep = runtime.start('i01.leftArm.bicep', 'Servo')
# MoveBodyTimer = runtime.start('MoveBodyTimer', 'Clock')
i01_rightArm_rotate = runtime.start('i01.rightArm.rotate', 'Servo')
#vi01_left_uart = runtime.start('vi01.left.uart', 'Serial')
# AzureTranslator = runtime.start('AzureTranslator', 'AzureTranslator')
i01_left = runtime.start('i01.left', 'Arduino')
i01_rightArm_shoulder = runtime.start('i01.rightArm.shoulder', 'Servo')
#vi01_right_uart = runtime.start('vi01.right.uart', 'Serial')
i01_left_serial = runtime.start('i01.left.serial', 'Serial')
# wdf = runtime.start('wdf', 'WikiDataFetcher')
i01_mouth_audioFile = runtime.start('i01.mouth.audioFile', 'AudioFile')
i01_chatBot = runtime.start('i01.chatBot', 'ProgramAB')
i01_leftHand_wrist = runtime.start('i01.leftHand.wrist', 'Servo')
i01_right = runtime.start('i01.right', 'Arduino')
log = runtime.start('log', 'Log')
HealthCheck = runtime.start('HealthCheck', 'Clock')
i01_torso_lowStom = runtime.start('i01.torso.lowStom', 'Servo')
i01_head_jaw = runtime.start('i01.head.jaw', 'Servo')
i01_leftHand_ringFinger = runtime.start('i01.leftHand.ringFinger', 'Servo')
imageDisplay = runtime.start('imageDisplay', 'ImageDisplay')
i01_leftHand_pinky = runtime.start('i01.leftHand.pinky', 'Servo')
i01_rightArm = runtime.start('i01.rightArm', 'InMoov2Arm')
webgui = runtime.start('webgui', 'WebGui')
i01 = runtime.start('i01', 'InMoov2')
i01_leftArm_omoplate = runtime.start('i01.leftArm.omoplate', 'Servo')
i01_rightHand_pinky = runtime.start('i01.rightHand.pinky', 'Servo')
htmlFilter = runtime.start('htmlFilter', 'HtmlFilter')
i01_head_eyeY = runtime.start('i01.head.eyeY', 'Servo')
i01_leftHand_thumb = runtime.start('i01.leftHand.thumb', 'Servo')
# MoveRandomTimer = runtime.start('MoveRandomTimer', 'Clock')
i01_torso = runtime.start('i01.torso', 'InMoov2Torso')
i01_rightArm_omoplate = runtime.start('i01.rightArm.omoplate', 'Servo')
i01_torso_midStom = runtime.start('i01.torso.midStom', 'Servo')
i01_rightHand_thumb = runtime.start('i01.rightHand.thumb', 'Servo')
i01_head = runtime.start('i01.head', 'InMoov2Head')
i01_chatBot_search = runtime.start('i01.chatBot.search', 'GoogleSearch')
# MoveHeadTimer = runtime.start('MoveHeadTimer', 'Clock')
#gui = runtime.start('gui', 'SwingGui')
#vi01_left = runtime.start('vi01.left', 'VirtualArduino')
#vi01_right = runtime.start('vi01.right', 'VirtualArduino')
i01_head_rothead = runtime.start('i01.head.rothead', 'Servo')
i01_leftArm = runtime.start('i01.leftArm', 'InMoov2Arm')
openWeatherMap = runtime.start('openWeatherMap', 'OpenWeatherMap')
i01_ear = runtime.start('i01.ear', 'WebkitSpeechRecognition')
i01_head_neck = runtime.start('i01.head.neck', 'Servo')
i01_head_eyelidLeft = runtime.start('i01.head.eyelidLeft', 'Servo')
i01_head_eyelidRight = runtime.start('i01.head.eyelidRight', 'Servo')
i01_leftArm_shoulder = runtime.start('i01.leftArm.shoulder', 'Servo')
i01_rightHand_wrist = runtime.start('i01.rightHand.wrist', 'Servo')
i01_mouth = runtime.start('i01.mouth', 'LocalSpeech')
i01_audioPlayer = runtime.start("i01.audioPlayer", "AudioFile")
i01_controller3 = runtime.start('i01.controller3', 'Arduino')
i01_llm = runtime.start('i01.llm', 'LLM')
#############################################################
## i2Head
i01_pca9685 = runtime.start("i01.pca9685","Adafruit16CServoDriver")
i01_head_eyeLeftLR = runtime.start('i01.head.eyeLeftLR', 'Servo')
i01_head_eyeRightLR = runtime.start('i01.head.eyeRightLR', 'Servo')
i01_head_eyeLeftUD = runtime.start('i01.head.eyeLeftUD', 'Servo')
i01_head_eyeRightUD = runtime.start('i01.head.eyeRightUD', 'Servo')
i01_head_cheekRight = runtime.start('i01.head.cheekRight', 'Servo')
i01_head_cheekLeft = runtime.start('i01.head.cheekLeft', 'Servo')
i01_head_forheadRight = runtime.start('i01.head.forheadRight', 'Servo')
i01_head_forheadLeft = runtime.start('i01.head.forheadLeft', 'Servo')
i01_head_eyelidLeftUpper = runtime.start('i01.head.eyelidLeftUpper', 'Servo')
i01_head_eyelidLeftLower = runtime.start('i01.head.eyelidLeftLower', 'Servo')
i01_head_eyelidRightUpper = runtime.start('i01.head.eyelidRightUpper', 'Servo')
i01_head_eyelidRightLower = runtime.start('i01.head.eyelidRightLower', 'Servo')
i01_head_upperLip = runtime.start('i01.head.upperLip', 'Servo')
i01_head_eyebrowRight = runtime.start('i01.head.eyebrowRight', 'Servo')
i01_head_eyebrowLeft = runtime.start('i01.head.eyebrowLeft', 'Servo')
#############################################################
## Needs fixing in InMoov2.java
i01_pir = runtime.start('i01.pir', 'Pir')
i01_ultrasonicRight = runtime.start('i01.ultrasonicRight', 'UltrasonicSensor')
i01_ultrasonicLeft = runtime.start('i01.ultrasonicLeft', 'UltrasonicSensor')
i01_neopixel = runtime.start('i01.neopixel', 'NeoPixel')
i01_opencv = runtime.start('i01.opencv', 'OpenCV')
##############################################################
## creating client connections connections ####

##############################################################
## configuring services ####
# Servo Config : i01_leftArm_rotate
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftArm_rotate.setPosition(90)
i01_leftArm_rotate.map(40.0,180.0,40.0,180.0)
i01_leftArm_rotate.setInverted(False)
i01_leftArm_rotate.setSpeed(50.0)
i01_leftArm_rotate.setRest(90.0)
i01_leftArm_rotate.setPin(9)
i01_leftArm_rotate.setAutoDisable(True)

# Servo Config : i01_torso_topStom
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_torso_topStom.setPosition(90)
i01_torso_topStom.map(60.0,120.0,60.0,120.0)
i01_torso_topStom.setInverted(False)
i01_torso_topStom.setSpeed(50.0)
i01_torso_topStom.setRest(90.0)
i01_torso_topStom.setPin(27)
i01_torso_topStom.setAutoDisable(True)

# Servo Config : i01_rightArm_bicep
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightArm_bicep.setPosition(0)
i01_rightArm_bicep.map(0.0,90.0,0.0,90.0)
i01_rightArm_bicep.setInverted(False)
i01_rightArm_bicep.setSpeed(50.0)
i01_rightArm_bicep.setRest(0.0)
i01_rightArm_bicep.setPin(8)
i01_rightArm_bicep.setAutoDisable(True)

# Servo Config : i01_head_rollNeck
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_rollNeck.setPosition(90)
i01_head_rollNeck.map(0.0,180.0,60.0,130.0)
i01_head_rollNeck.setInverted(False)
i01_head_rollNeck.setSpeed(50.0)
i01_head_rollNeck.setRest(90.0)
i01_head_rollNeck.setPin(12)
i01_head_rollNeck.setAutoDisable(True)

# Servo Config : i01_rightHand_ringFinger
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightHand_ringFinger.setPosition(2)
i01_rightHand_ringFinger.map(0.0,180.0,0.0,180.0)
i01_rightHand_ringFinger.setInverted(False)
i01_rightHand_ringFinger.setSpeed(100.0)
i01_rightHand_ringFinger.setRest(2.0)
i01_rightHand_ringFinger.setPin(5)
i01_rightHand_ringFinger.setAutoDisable(True)

# Servo Config : i01_leftHand_majeure
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftHand_majeure.setPosition(2)
i01_leftHand_majeure.map(0.0,180.0,0.0,180.0)
i01_leftHand_majeure.setInverted(False)
i01_leftHand_majeure.setSpeed(100.0)
i01_leftHand_majeure.setRest(2.0)
i01_leftHand_majeure.setPin(4)
i01_leftHand_majeure.setAutoDisable(True)

# Servo Config : i01_leftHand_index
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftHand_index.setPosition(2)
i01_leftHand_index.map(0.0,180.0,0.0,180.0)
i01_leftHand_index.setInverted(False)
i01_leftHand_index.setSpeed(100.0)
i01_leftHand_index.setRest(2.0)
i01_leftHand_index.setPin(3)
i01_leftHand_index.setAutoDisable(True)

# Servo Config : i01_rightHand_majeure
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightHand_majeure.setPosition(2)
i01_rightHand_majeure.map(0.0,180.0,0.0,180.0)
i01_rightHand_majeure.setInverted(False)
i01_rightHand_majeure.setSpeed(100.0)
i01_rightHand_majeure.setRest(2.0)
i01_rightHand_majeure.setPin(4)
i01_rightHand_majeure.setAutoDisable(True)

# Servo Config : i01_head_eyeX
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_eyeX.setPosition(90)
i01_head_eyeX.map(0.0,180.0,60.0,120.0)
i01_head_eyeX.setInverted(False)
i01_head_eyeX.setSpeed(50.0)
i01_head_eyeX.setRest(90.0)
i01_head_eyeX.setPin(22)
i01_head_eyeX.setAutoDisable(True)

# Servo Config : i01_head_eyelidLeft
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_eyelidLeft.setPosition(90)
i01_head_eyelidLeft.map(0.0,180.0,0.0,180.0)
i01_head_eyelidLeft.setInverted(False)
i01_head_eyelidLeft.setSpeed(50.0)
i01_head_eyelidLeft.setRest(90.0)
i01_head_eyelidLeft.setPin(22)
i01_head_eyelidLeft.setAutoDisable(True)

# Servo Config : i01_head_eyelidRight
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_eyelidRight.setPosition(90)
i01_head_eyelidRight.map(0.0,180.0,0.0,180.0)
i01_head_eyelidRight.setInverted(False)
i01_head_eyelidRight.setSpeed(50.0)
i01_head_eyelidRight.setRest(90.0)
i01_head_eyelidRight.setPin(24)
i01_head_eyelidRight.setAutoDisable(True)

# Servo Config : i01_head_eyelidRightUpper
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_eyelidRightUpper.setPosition(90)
i01_head_eyelidRightUpper.map(0.0,180.0,0.0,180.0)
i01_head_eyelidRightUpper.setInverted(False)
i01_head_eyelidRightUpper.setSpeed(50.0)
i01_head_eyelidRightUpper.setRest(90.0)
i01_head_eyelidRightUpper.setPin(8)
i01_head_eyelidRightUpper.setAutoDisable(True)

# Servo Config : i01_head_eyelidRightLower
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_eyelidRightLower.setPosition(90)
i01_head_eyelidRightLower.map(0.0,180.0,0.0,180.0)
i01_head_eyelidRightLower.setInverted(True)
i01_head_eyelidRightLower.setSpeed(50.0)
i01_head_eyelidRightLower.setRest(90.0)
i01_head_eyelidRightLower.setPin(9)
i01_head_eyelidRightLower.setAutoDisable(True)

# Servo Config : i01_head_eyelidLeftUpper
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_eyelidLeftUpper.setPosition(90)
i01_head_eyelidLeftUpper.map(0.0,180.0,0.0,180.0)
i01_head_eyelidLeftUpper.setInverted(True)
i01_head_eyelidLeftUpper.setSpeed(50.0)
i01_head_eyelidLeftUpper.setRest(90.0)
i01_head_eyelidLeftUpper.setPin(6)
i01_head_eyelidLeftUpper.setAutoDisable(True)

# Servo Config : i01_head_eyelidLeftLower
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_eyelidLeftLower.setPosition(90)
i01_head_eyelidLeftLower.map(0.0,180.0,0.0,180.0)
i01_head_eyelidLeftLower.setInverted(False)
i01_head_eyelidLeftLower.setSpeed(50.0)
i01_head_eyelidLeftLower.setRest(90.0)
i01_head_eyelidLeftLower.setPin(7)
i01_head_eyelidLeftLower.setAutoDisable(True)

# Servo Config : i01_head_eyeLeftLR
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_eyeLeftLR.setPosition(90)
i01_head_eyeLeftLR.map(0.0,180.0,0.0,80.0)
i01_head_eyeLeftLR.setInverted(False)
i01_head_eyeLeftLR.setSpeed(50.0)
i01_head_eyeLeftLR.setRest(90.0)
i01_head_eyeLeftLR.setPin(22)
i01_head_eyeLeftLR.setAutoDisable(True)

# Servo Config : i01_head_eyeRightLR
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_eyeRightLR.setPosition(90)
i01_head_eyeRightLR.map(0.0,180.0,0.0,180.0)
i01_head_eyeRightLR.setInverted(True)
i01_head_eyeRightLR.setSpeed(50.0)
i01_head_eyeRightLR.setRest(90.0)
i01_head_eyeRightLR.setPin(22)
i01_head_eyeRightLR.setAutoDisable(True)

# Servo Config : i01_head_eyeLeftUD
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_eyeLeftUD.setPosition(90)
i01_head_eyeLeftUD.map(0.0,180.0,0.0,180.0)
i01_head_eyeLeftUD.setInverted(True)
i01_head_eyeLeftUD.setSpeed(50.0)
i01_head_eyeLeftUD.setRest(90.0)
i01_head_eyeLeftUD.setPin(24)
i01_head_eyeLeftUD.setAutoDisable(True)

# Servo Config : i01_head_eyeRightUD
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_eyeRightUD.setPosition(90)
i01_head_eyeRightUD.map(0.0,180.0,0.0,180.0)
i01_head_eyeRightUD.setInverted(False)
i01_head_eyeRightUD.setSpeed(50.0)
i01_head_eyeRightUD.setRest(90.0)
i01_head_eyeRightUD.setPin(24)
i01_head_eyeRightUD.setAutoDisable(True)

# Servo Config : i01_head_cheekRight
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_cheekRight.setPosition(90)
i01_head_cheekRight.map(0.0,180.0,0.0,180.0)
i01_head_cheekRight.setInverted(False)
i01_head_cheekRight.setSpeed(50.0)
i01_head_cheekRight.setRest(90.0)
i01_head_cheekRight.setPin(15)
i01_head_cheekRight.setAutoDisable(True)

# Servo Config : i01_head_cheekLeft
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_cheekLeft.setPosition(90)
i01_head_cheekLeft.map(0.0,180.0,0.0,180.0)
i01_head_cheekLeft.setInverted(True)
i01_head_cheekLeft.setSpeed(50.0)
i01_head_cheekLeft.setRest(90.0)
i01_head_cheekLeft.setPin(14)
i01_head_cheekLeft.setAutoDisable(True)

# Servo Config : i01_head_forheadRight
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_forheadRight.setPosition(90)
i01_head_forheadRight.map(0.0,180.0,0.0,180.0)
i01_head_forheadRight.setInverted(False)
i01_head_forheadRight.setSpeed(50.0)
i01_head_forheadRight.setRest(90.0)
i01_head_forheadRight.setPin(13)
i01_head_forheadRight.setAutoDisable(True)

# Servo Config : i01_head_forheadLeft
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_forheadLeft.setPosition(90)
i01_head_forheadLeft.map(0.0,180.0,0.0,180.0)
i01_head_forheadLeft.setInverted(True)
i01_head_forheadLeft.setSpeed(50.0)
i01_head_forheadLeft.setRest(90.0)
i01_head_forheadLeft.setPin(12)
i01_head_forheadLeft.setAutoDisable(True)

# Servo Config : i01_head_upperLip
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_upperLip.setPosition(90)
i01_head_upperLip.map(0.0,180.0,0.0,180.0)
i01_head_upperLip.setInverted(False)
i01_head_upperLip.setSpeed(50.0)
i01_head_upperLip.setRest(90.0)
i01_head_upperLip.setPin(26)
i01_head_upperLip.setAutoDisable(True)

# Servo Config : i01_head_eyebrowRight
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_eyebrowRight.setPosition(90)
i01_head_eyebrowRight.map(0.0,180.0,0.0,180.0)
i01_head_eyebrowRight.setInverted(False)
i01_head_eyebrowRight.setSpeed(50.0)
i01_head_eyebrowRight.setRest(90.0)
i01_head_eyebrowRight.setPin(11)
i01_head_eyebrowRight.setAutoDisable(True)

# Servo Config : i01_head_eyebrowLeft
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_eyebrowLeft.setPosition(90)
i01_head_eyebrowLeft.map(0.0,180.0,0.0,180.0)
i01_head_eyebrowLeft.setInverted(True)
i01_head_eyebrowLeft.setSpeed(50.0)
i01_head_eyebrowLeft.setRest(90.0)
i01_head_eyebrowLeft.setPin(10)
i01_head_eyebrowLeft.setAutoDisable(True)

# Servo Config : i01_rightHand_index
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightHand_index.setPosition(2)
i01_rightHand_index.map(0.0,180.0,0.0,180.0)
i01_rightHand_index.setInverted(False)
i01_rightHand_index.setSpeed(100.0)
i01_rightHand_index.setRest(2.0)
i01_rightHand_index.setPin(3)
i01_rightHand_index.setAutoDisable(True)

# Servo Config : i01_leftArm_bicep
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftArm_bicep.setPosition(0)
i01_leftArm_bicep.map(0.0,90.0,0.0,90.0)
i01_leftArm_bicep.setInverted(False)
i01_leftArm_bicep.setSpeed(50.0)
i01_leftArm_bicep.setRest(0.0)
i01_leftArm_bicep.setPin(8)
i01_leftArm_bicep.setAutoDisable(True)

# Servo Config : i01_rightArm_rotate
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightArm_rotate.setPosition(90)
i01_rightArm_rotate.map(40.0,180.0,40.0,180.0)
i01_rightArm_rotate.setInverted(False)
i01_rightArm_rotate.setSpeed(50.0)
i01_rightArm_rotate.setRest(90.0)
i01_rightArm_rotate.setPin(9)
i01_rightArm_rotate.setAutoDisable(True)

# Arduino Config : i01_left
i01_left.setVirtual(False)
# we have the following ports : [COM3.UART, COM4.UART, COM4, COM3]
i01_left.connect(leftPort)
i01_left.setBoardMega()
# make sure the pins are set before attaching
i01_leftHand_thumb.setPin("2")
i01_leftHand_index.setPin("3")
i01_leftHand_majeure.setPin("4")
i01_leftHand_ringFinger.setPin("5")
i01_leftHand_pinky.setPin("6")
i01_leftHand_wrist.setPin("7")
i01_leftArm_shoulder.setPin("10")
i01_head_rothead.setPin("13")
i01_head_neck.setPin("12")
i01_leftArm_bicep.setPin("8")
i01_head_jaw.setPin("26")
i01_head_eyeY.setPin("24")
i01_leftArm_omoplate.setPin("11")
i01_head_eyeX.setPin("22")
i01_head_eyeLeftLR.setPin("22")
i01_head_eyeLeftUD.setPin("24")
i01_leftArm_rotate.setPin("9")
i01_torso_topStom.setPin("27")
i01_torso_midStom.setPin("28")
i01_torso_lowStom.setPin("29")
i01_left.attach("i01.leftHand.thumb")
i01_left.attach("i01.leftHand.index")
i01_left.attach("i01.leftHand.majeure")
i01_left.attach("i01.leftHand.ringFinger")
i01_left.attach("i01.leftHand.pinky")
i01_left.attach("i01.leftHand.wrist")
i01_left.attach("i01.leftArm.shoulder")
i01_left.attach("i01.head.rothead")
i01_left.attach("i01.head.neck")
i01_left.attach("i01.torso.lowStom")
i01_left.attach("i01.leftArm.bicep")
i01_left.attach("i01.head.jaw")
i01_left.attach("i01.head.eyeY")
i01_left.attach("i01.torso.midStom")
i01_left.attach("i01.leftArm.omoplate")
i01_left.attach("i01.head.eyeX")
i01_left.attach("i01.leftArm.rotate")
i01_left.attach("i01.torso.topStom")
i01_left.attach("i01.head.eyeLeftLR")
i01_left.attach("i01.head.eyeLeftUD")

i01_ultrasonicLeft.setTriggerPin(64)
i01_ultrasonicLeft.setEchoPin(63)
i01_ultrasonicLeft.attach("i01.left")

# Arduino Config : i01_controller3
i01_controller3.setVirtual(False)
# we have the following ports : [COM8.UART, COM8]
i01_controller3.connect(controller3Port)
i01_controller3.setBoardNano()

# PCA9685 Config : i01_PCA9685
if runtime.isStarted('i01.left'):
    i01_pca9685.setBus('1')
    i01_pca9685.save()
    i01_pca9685.attach('i01.left')
    i01_head_cheekRight.setPin("15")
    i01_head_cheekLeft.setPin("14")
    i01_head_forheadRight.setPin("13")
    i01_head_forheadLeft.setPin("12")
    i01_head_eyelidLeftUpper.setPin("6")
    i01_head_eyelidLeftLower.setPin("7")
    i01_head_eyelidRightUpper.setPin("8")
    i01_head_eyelidRightLower.setPin("9")
    i01_head_upperLip.setPin("29")
    i01_head_eyebrowRight.setPin("11")
    i01_head_eyebrowLeft.setPin("0")
    i01_pca9685.attach("i01.head.cheekRight")
    i01_pca9685.attach("i01.head.cheekLeft")
    i01_pca9685.attach("i01.head.forheadRight")
    i01_pca9685.attach("i01.head.forheadLeft")
    i01_pca9685.attach("i01.head.eyelidLeftUpper")
    i01_pca9685.attach("i01.head.eyelidLeftLower")
    i01_pca9685.attach("i01.head.eyelidRightUpper")
    i01_pca9685.attach("i01.head.eyelidRightLower")
    i01_pca9685.attach("i01.head.upperLip")
    i01_pca9685.attach("i01.head.eyebrowRight")
    i01_pca9685.attach("i01.head.eyebrowLeft")

else:
    runtime.warn('i01.left not started for PCA9685')


# make sure the pins are set before attaching
i01_neopixel.setPin(2)
i01_neopixel.setPixelCount(16)
i01_controller3.attach("i01.neopixel")
i01_pir.setPin("23")
i01_pir.attach("i01.left")


# Servo Config : i01_rightArm_shoulder
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightArm_shoulder.setPosition(30)
i01_rightArm_shoulder.map(0.0,180.0,0.0,180.0)
i01_rightArm_shoulder.setInverted(False)
i01_rightArm_shoulder.setSpeed(50.0)
i01_rightArm_shoulder.setRest(30.0)
i01_rightArm_shoulder.setPin(10)
i01_rightArm_shoulder.setAutoDisable(True)

# Servo Config : i01_leftHand_wrist
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftHand_wrist.setPosition(90)
i01_leftHand_wrist.map(0.0,180.0,0.0,180.0)
i01_leftHand_wrist.setInverted(True)
i01_leftHand_wrist.setSpeed(50.0)
i01_leftHand_wrist.setRest(90.0)
i01_leftHand_wrist.setPin(7)
i01_leftHand_wrist.setAutoDisable(True)

# Arduino Config : i01_right
i01_right.setVirtual(False)
# we have the following ports : [COM3.UART, COM4.UART, COM4, COM3]
i01_right.connect(rightPort)
i01_right.setBoardMega()
# make sure the pins are set before attaching
i01_rightHand_majeure.setPin("4")
i01_rightHand_ringFinger.setPin("5")
i01_rightHand_wrist.setPin("7")
i01_rightArm_bicep.setPin("8")
i01_head_rollNeck.setPin("12")
i01_rightArm_shoulder.setPin("10")
i01_rightHand_index.setPin("3")
i01_rightHand_thumb.setPin("2")
i01_rightArm_rotate.setPin("9")
i01_rightArm_omoplate.setPin("11")
i01_rightHand_pinky.setPin("6")
i01_head_eyeRightLR.setPin("22")
i01_head_eyeRightUD.setPin("24")
i01_right.attach("i01.rightHand.majeure")
i01_right.attach("i01.rightHand.ringFinger")
i01_right.attach("i01.rightHand.wrist")
i01_right.attach("i01.rightArm.bicep")
i01_right.attach("i01.head.rollNeck")
i01_right.attach("i01.head.eyelidLeft")
i01_right.attach("i01.head.eyelidRight")
i01_right.attach("i01.rightArm.shoulder")
i01_right.attach("i01.rightHand.index")
i01_right.attach("i01.rightHand.thumb")
i01_right.attach("i01.rightArm.rotate")
i01_right.attach("i01.rightArm.omoplate")
i01_right.attach("i01.rightHand.pinky")
i01_right.attach("i01.head.eyeRightLR")
i01_right.attach("i01.head.eyeRightUD")

i01_ultrasonicRight.setTriggerPin(64)
i01_ultrasonicRight.setEchoPin(63)
i01_ultrasonicRight.attach("i01.right")

# Servo Config : i01_torso_lowStom
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_torso_lowStom.setPosition(90)
i01_torso_lowStom.map(0.0,180.0,0.0,180.0)
i01_torso_lowStom.setInverted(False)
i01_torso_lowStom.setSpeed(50.0)
i01_torso_lowStom.setRest(90.0)
i01_torso_lowStom.setPin(29)
i01_torso_lowStom.setAutoDisable(True)

# Servo Config : i01_head_jaw
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_jaw.setPosition(0)
i01_head_jaw.map(0.0,180.0,10.0,25.0)
i01_head_jaw.setInverted(False)
i01_head_jaw.setSpeed(100.0)
i01_head_jaw.setRest(0.0)
i01_head_jaw.setPin(26)
i01_head_jaw.setAutoDisable(True)

# Servo Config : i01_leftHand_ringFinger
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftHand_ringFinger.setPosition(2)
i01_leftHand_ringFinger.map(0.0,180.0,0.0,180.0)
i01_leftHand_ringFinger.setInverted(False)
i01_leftHand_ringFinger.setSpeed(100.0)
i01_leftHand_ringFinger.setRest(2.0)
i01_leftHand_ringFinger.setPin(5)
i01_leftHand_ringFinger.setAutoDisable(True)

# Servo Config : i01_leftHand_pinky
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftHand_pinky.setPosition(2)
i01_leftHand_pinky.map(0.0,180.0,0.0,180.0)
i01_leftHand_pinky.setInverted(False)
i01_leftHand_pinky.setSpeed(100.0)
i01_leftHand_pinky.setRest(2.0)
i01_leftHand_pinky.setPin(6)
i01_leftHand_pinky.setAutoDisable(True)

# WebGui Config : webgui
webgui.autoStartBrowser(False)
webgui.setPort(8888)
webgui.setAddress("0.0.0.0")

# Servo Config : i01_leftArm_omoplate
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftArm_omoplate.setPosition(10)
i01_leftArm_omoplate.map(10.0,80.0,10.0,80.0)
i01_leftArm_omoplate.setInverted(False)
i01_leftArm_omoplate.setSpeed(50.0)
i01_leftArm_omoplate.setRest(10.0)
i01_leftArm_omoplate.setPin(11)
i01_leftArm_omoplate.setAutoDisable(True)

# Servo Config : i01_rightHand_pinky
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightHand_pinky.setPosition(2)
i01_rightHand_pinky.map(0.0,180.0,0.0,180.0)
i01_rightHand_pinky.setInverted(False)
i01_rightHand_pinky.setSpeed(100.0)
i01_rightHand_pinky.setRest(2.0)
i01_rightHand_pinky.setPin(6)
i01_rightHand_pinky.setAutoDisable(True)

# Servo Config : i01_head_eyeY
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_eyeY.setPosition(90)
i01_head_eyeY.map(0.0,180.0,60.0,120.0)
i01_head_eyeY.setInverted(False)
i01_head_eyeY.setSpeed(50.0)
i01_head_eyeY.setRest(90.0)
i01_head_eyeY.setPin(24)
i01_head_eyeY.setAutoDisable(True)

# Servo Config : i01_leftHand_thumb
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftHand_thumb.setPosition(2)
i01_leftHand_thumb.map(0.0,180.0,0.0,180.0)
i01_leftHand_thumb.setInverted(False)
i01_leftHand_thumb.setSpeed(100.0)
i01_leftHand_thumb.setRest(2.0)
i01_leftHand_thumb.setPin(2)
i01_leftHand_thumb.setAutoDisable(True)

# Servo Config : i01_rightArm_omoplate
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightArm_omoplate.setPosition(10)
i01_rightArm_omoplate.map(10.0,80.0,10.0,80.0)
i01_rightArm_omoplate.setInverted(False)
i01_rightArm_omoplate.setSpeed(50.0)
i01_rightArm_omoplate.setRest(10.0)
i01_rightArm_omoplate.setPin(11)
i01_rightArm_omoplate.setAutoDisable(True)

# Servo Config : i01_torso_midStom
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_torso_midStom.setPosition(90)
i01_torso_midStom.map(0.0,180.0,0.0,180.0)
i01_torso_midStom.setInverted(False)
i01_torso_midStom.setSpeed(50.0)
i01_torso_midStom.setRest(90.0)
i01_torso_midStom.setPin(28)
i01_torso_midStom.setAutoDisable(True)

# Servo Config : i01_rightHand_thumb
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightHand_thumb.setPosition(2)
i01_rightHand_thumb.map(0.0,180.0,0.0,180.0)
i01_rightHand_thumb.setInverted(False)
i01_rightHand_thumb.setSpeed(100.0)
i01_rightHand_thumb.setRest(2.0)
i01_rightHand_thumb.setPin(2)
i01_rightHand_thumb.setAutoDisable(True)

# Servo Config : i01_head_rothead
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_rothead.setPosition(90)
i01_head_rothead.map(0.0,180.0,30.0,150.0)
i01_head_rothead.setInverted(False)
i01_head_rothead.setSpeed(50.0)
i01_head_rothead.setRest(90.0)
i01_head_rothead.setPin(13)
i01_head_rothead.setAutoDisable(True)

# Servo Config : i01_head_neck
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_head_neck.setPosition(90)
i01_head_neck.map(0.0,180.0,20.0,160.0)
i01_head_neck.setInverted(False)
i01_head_neck.setSpeed(50.0)
i01_head_neck.setRest(90.0)
i01_head_neck.setPin(12)
i01_head_neck.setAutoDisable(True)

# Servo Config : i01_leftArm_shoulder
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_leftArm_shoulder.setPosition(30)
i01_leftArm_shoulder.map(0.0,180.0,0.0,180.0)
i01_leftArm_shoulder.setInverted(False)
i01_leftArm_shoulder.setSpeed(50.0)
i01_leftArm_shoulder.setRest(30.0)
i01_leftArm_shoulder.setPin(10)
i01_leftArm_shoulder.setAutoDisable(True)

# Servo Config : i01_rightHand_wrist
# sets initial position of servo before moving
# in theory this is the position of the servo when this file was created
i01_rightHand_wrist.setPosition(90)
i01_rightHand_wrist.map(0.0,180.0,0.0,180.0)
i01_rightHand_wrist.setInverted(False)
i01_rightHand_wrist.setSpeed(50.0)
i01_rightHand_wrist.setRest(90.0)
i01_rightHand_wrist.setPin(7)
i01_rightHand_wrist.setAutoDisable(True)

## sync the i2Head eyes with the default i01.eyes
if runtime.isStarted('i01.head') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightLR') and runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeRightUD'):
  i01_head_eyeX.sync(i01_head_eyeLeftLR)
  i01_head_eyeX.sync(i01_head_eyeRightLR)
  i01_head_eyeY.sync(i01_head_eyeLeftUD)
  i01_head_eyeY.sync(i01_head_eyeRightUD)
## sync the i2Head eyelids with the default i01.eyelids  
if runtime.isStarted('i01.head') and runtime.isStarted('i01.head.eyelidLeft') and runtime.isStarted('i01.head.eyelidRight') and runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidRightUpper'):
  i01_head_eyelidLeft.sync(i01_head_eyelidLeftUpper)
  i01_head_eyelidRight.sync(i01_head_eyelidRightUpper)

i01_mouth.setMute(False)

# We launch InMoov startup sound and the rest
i01_audioPlayer.playFileBlocking('resource/InMoov2/system/sounds/startupsound.mp3')
i01_neopixel.setColor(0, 40, 220)
i01_neopixel.setSpeed(30) 
i01_neopixel.playAnimation("Ironman")
# We add opencv settings
i01_opencv.setGrabberType("OpenCV")
i01_opencv.nativeViewer=False
i01_opencv.webViewer=True

jme = i01.startSimulator()
#i01.loadGestures("resource/InMoov2/gestures")

#RobotCanMoveHeadWhileSpeaking = True

#i01.startChatBot()
# This launch the chatbot for the first initialization
#if str(i01_chatBot.getPredicate("Friend","firstinit"))=="unknown" or str(i01_chatBot.getPredicate("Friend","firstinit"))=="started":
  #i01_chatBot.setPredicate("default","topic","default")
  #i01_chatBot.getResponse("FIRST_INIT")
#else:
  #i01_chatBot.getResponse("WAKE_UP")
