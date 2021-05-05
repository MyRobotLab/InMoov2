#file : InMoov.minimalFingerStarter.py
# MRL version >= Nixie
# this script is provided as a basic guide
# most parts can be run by uncommenting them
# InMoov2 now can be started in modular pieces through the webgui
# although this script is very short you can still
# do voice control of a FingerStarter or hand
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work

# Change to the port that you use
rightPort = "COM9"
##############
runtime = Runtime.getInstance()
runtime.setAllLocales('en-US')
#to tweak the default voice
Voice="Mark" #Male US voice 
#Voice="cmu-slt-hsmm" #Default female for MarySpeech
mouth = Runtime.createAndStart('i01.mouth', 'MarySpeech')
#mouth.installComponentsAcceptLicense(Voice)
mouth.setVoice(Voice)
##############
# starting InMoov service
i01 = Runtime.start('i01', 'InMoov2')
#Force Arduino to connect (fix Todo)
right = Runtime.createAndStart("i01.right", "Arduino")
right.connect(rightPort)
##############
# Starting parts
i01.startEar()
# Start the webgui service without starting the browser
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")
# As an alternative you can use the line below to show all services in the browser. In that case you should comment out all lines above that starts with webgui. 
# webgui = Runtime.createAndStart("webgui","WebGui")
##############
i01.startMouth()
##############
i01_rightHand = Runtime.start('i01.rightHand', 'InMoov2Hand')
# Tweaking defaults settings of right hand index finger
i01_rightHand_index = Runtime.start('i01.rightHand.index', 'Servo')
# Setting the arduino pin
i01_rightHand_index.setPin("3")
# Mapping by setting your servo limits
i01_rightHand_index.map(0,180,42,160)
# Rest position
i01_rightHand_index.setRest(0)
# We set the hand with autoDisable
i01_rightHand.setAutoDisable(True)
##############
i01.startRightHand(rightPort)

# We attach the servo to the arduino
i01_right.attach("i01.rightHand.index")
##############
# Verbal commands
#always listen
#i01_ear.setAutoListen(True)

i01_ear.addCommand("attach your finger", "i01.rightHand.index", "enable")
i01_ear.addCommand("disconnect your finger", "i01.rightHand.index", "disable")
i01_ear.addCommand("rest", "i01.rightHand.index", "rest")## Hardcoded gesture
i01_ear.addCommand("open your finger", "python", "fingeropen")
i01_ear.addCommand("close your finger", "python", "fingerclose")
i01_ear.addCommand("finger to the middle", "python", "fingermiddle")
i01_ear.addCommand("capture gesture", i01_ear.getName(), "captureGesture")
i01_ear.addCommand("manual", i01_ear.getName(), "lockOutAllGrammarExcept", "voice control")
i01_ear.addCommand("voice control", i01_ear.getName(), "clearLock")

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley
# ear.addConfirmations("yes","correct","yeah","ya")
# ear.addNegations("no","wrong","nope","nah")

i01_ear.startListening()

def fingeropen():
  i01_rightHand_index.setSpeed(20)## Low Speed
  i01.moveHand("right",0,0,0,0,0,0)## Thumb,index,majeure,ringfinger,pinky,wrist
  i01_mouth.speak("ok I open my finger")

def fingerclose():
  i01_rightHand_index.setSpeed(50)## Medium Speed
  i01.moveHand("right",180,180,180,180,180,90)
  i01_mouth.speak("my finger is closed")

def fingermiddle():
  i01_rightHand_index.setSpeed(100)## Maximum Speed
  i01.moveHand("right",90,90,90,90,90,90)
  i01_mouth.speak("ok you have my attention")

