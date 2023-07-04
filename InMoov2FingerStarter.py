#file : InMoov2.minimalFingerStarter.py
# MRL version >= Nixie
# this script is provided as a basic guide
# most parts can be run by uncommenting them
# InMoov now can be started in modular pieces through the UI and configs
# although this script is very short you can still
# do voice control of a FingerStarter or hand
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work
# Make sure chrome can use your microphone

# Change to the port that you use
rightPort = "COM9"
##############
#to tweak the default voice
Voice="Mark" #Male US voice 
#Voice="Poppy" #Female for MarySpeech
mouth = runtime.start("i01.mouth", "MarySpeech")
#mouth.installComponentsAcceptLicense(Voice)
mouth.setVoice(Voice)
##############
# starting InMoov2 service
i01 = Runtime.create("i01", "InMoov2")
#Force Arduino to connect (fix Todo)
right = runtime.start("i01.right", "Arduino")
right.connect(rightPort)
##############
# Starting parts
i01.startEar()
##############
i01.startMouth()
##############
i01_rightHand_index = Runtime.create('i01.rightHand.index', 'Servo')

# Tweaking defaults settings of right hand
# Mapping by setting your servo limits (minIn, maxIn, minOut, maxOut)
i01_rightHand_index.map(0,180,0,180)
# Rest position
i01_rightHand_index.setRest(0)
# Setting pin
i01_rightHand_index.setPin(3)
# Setting speed
i01_rightHand_index.setSpeed(45)
# Setting port
i01_rightHand_index.attach(right)
##############
i01 = runtime.start("i01","InMoov2")
##############
i01_rightHand_index = runtime.start('i01.rightHand.index', 'Servo')

# By default InMoov2 servos are autoEnable(True)
#i01.rightHand.setAutoEnable(False)
##############
# Verbal commands
# These commands do not use the chatbot, which can give a lot more interactions.
i01_ear.addCommand("attach your finger", "i01.rightHand.index", "enable")
i01_ear.addCommand("disconnect your finger", "i01.rightHand.index", "disable")
i01_ear.addCommand("rest", "i01.rightHand.index", "rest")## Hardcoded gesture
i01_ear.addCommand("open your finger", "python", "fingeropen")
i01_ear.addCommand("close your finger", "python", "fingerclose")
i01_ear.addCommand("finger to the middle", "python", "fingermiddle")
i01_ear.addCommand("capture gesture", i01_ear.getName(), "captureGesture")## Hardcoded function
i01_ear.addCommand("manual", i01_ear.getName(), "lockOutAllGrammarExcept", "voice control")## Hardcoded function
i01_ear.addCommand("voice control", i01_ear.getName(), "clearLock")## Hardcoded function

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley
# ear.addComfirmations("yes","correct","yeah","ya")
# ear.addNegations("no","wrong","nope","nah")

i01_ear.startListening()

def fingeropen():
  i01_rightHand_index.setSpeed(20)## Low speed
  i01_rightHand_index.moveTo(0)## Thumb,index,majeure,ringfinger,pinky,wrist
  i01_mouth.speak("ok I open my finger")

def fingerclose():
  i01_rightHand_index.setSpeed(100)## Medium speed
  i01_rightHand_index.moveTo(180)
  i01_mouth.speak("my finger is closed")

def fingermiddle():
  i01_rightHand_index.setSpeed(500)## Maximum speed
  i01_rightHand_index.moveTo(90)
  i01_mouth.speak("ok you have my attention")

