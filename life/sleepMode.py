# ##############################################################################
#                 ROBOT SLEEP MODE
# ##############################################################################

###############################################################################
# check if robot can sleep or wakeup
# only based on pir at this time
###############################################################################
import random

if runtime.isStarted('i01.pir'):
   sleepTimer = runtime.start("sleepTimer","Clock")
   sleepTimer.addListener("pulse", python.name, "sleepTimerRoutine")
   sleepTimer.setInterval(i01.getConfig().sleepTimeoutMs)

if runtime.isStarted('i01.headTracking') or runtime.isStarted('i01.eyeTracking'):
   trackingTimer = runtime.start("trackingTimer","Clock")
   trackingTimer.addListener("pulse", python.name, "trackingTimerRoutine")
   trackingTimer.setInterval(i01.getConfig().trackingTimeoutMs)

def sleepModeWakeUp():
  if runtime.isStarted('i01.fsm'):
    i01_fsm.fire("wake")
  if runtime.isStarted('i01.chatBot'):
      i01_chatBot.setPredicate('botState', 'awake')
  if runtime.isStarted('i01.llm'):
    i01_llm.wake()   
  if runtime.isStarted('i01.mouth'):
    initMouth()
  if runtime.isStarted('i01.ear'):
    #initEar()
    i01_ear.setAwake(True)
    WaitXsecondBeforeRelaunchTracking=-10
    i01_ear.startRecording()
  if runtime.isStarted('i01.pir'):
    initPir()
    if i01.getConfig().pirWakeUp==1:
      sleepTimer.startClock()
      #i01_ear.setWakeWordTimeout(i01_ear.getConfig().wakeWordIdleTimeoutSeconds)
      i01_pir.enable()
    else:  
      i01_pir.disable()
  #if RobotIsStarted==1:
  #if runtime.isStarted('i01.fsm'):
    #if i01_fsm.getState()=="idle":
    
  if runtime.isStarted('i01.imageDisplay'):
    i01_imageDisplay.closeAll()
  
  #display(RuningFolder+'/system/pictures/loading_1024-600.jpg')
  
  if runtime.isStarted('i01.neoPixel'):
    i01_neoPixel.setAnimation("Larson Scanner", 255, 255, 0, 25)
    sleep(2)
    i01_neoPixel.clear()
  #optional switchon nervoboard
  #switchOnAllNervo()
  if runtime.isStarted('i01.head.eyelidLeft') and runtime.isStarted('i01.head.eyelidRight'):
    i01_head_eyelidLeft.rest()
    i01_head_eyelidRight.rest()
    #i01_head_eyelids.autoBlink(True)
        #head up
  if runtime.isStarted('i01.head'):
    i01_head_neck.setSpeed(50)
    i01_head_neck.moveToBlocking(i01_head_neck.getRest())
  if i01.getConfig().pirPlaySounds==1:
    if runtime.isStarted("i01.audioPlayer"):
      i01_audioPlayer.playFile('resource/InMoov2/system/sounds/Notifications/start.wav', False)
  if i01.getConfig().customSound==1:
    if runtime.isStarted("i01.audioPlayer"):
      i01_audioPlayer.playFile('resource/InMoov2/system/sounds/Notifications/'+random.choice(os.listdir('resource/InMoov2/system/sounds/Notifications')),False)
  if runtime.isStarted('i01.opencv'):
    if i01.getConfig().pirEnableTracking==1:
      trackHumans()
    if i01.getConfig().openCVFaceRecognizerActivated==1:
      facerecognizer()
    else:
      welcomeMessage()
  else:
     welcomeMessage()
 
  if runtime.isStarted('i01'):fullspeed()


def sleepModeSleep():
  if runtime.isStarted('i01.random'):
    i01_random.disable()
  if runtime.isStarted('i01.ear'):
    initEar()
    i01_ear.setAwake(False)
    #print("sleeping")
  if runtime.isStarted('i01.headTracking'):
    initTracking()
    stopTrackHumans()
  if runtime.isStarted('i01.opencv'):
    i01_opencv.stopCapture()  
  if runtime.isStarted('i01.imageDisplay'):
    i01_imageDisplay.closeAll()
  if runtime.isStarted('i01.fsm'):  
    i01_fsm.fire("sleep")
  if runtime.isStarted('i01.chatBot'):
    i01_chatBot.setPredicate('botState', 'sleeping')
  i01.halfSpeed()
  rest()
  i01.waitTargetPos()
  #display sleeping robot on screen
  if runtime.isStarted('i01.imageDisplay'):
    i01_imageDisplay.display('resource/InMoov2/system/pictures/sleeping_2_1024-600.jpg')
  #head down
  if runtime.isStarted('i01.head.eyelidLeft') and runtime.isStarted('i01.head.eyelidRight'):
    #i01_head_eyelids.autoBlink(False)
    i01_head_eyelidLeft.moveTo(0)
    i01_head_eyelidRight.moveTo(0)
  if runtime.isStarted('i01.head'):
    i01_head_neck.setSpeed(40)
    i01_head_neck.moveTo(10)
  i01.waitTargetPos()
  i01.disable()
  #switchOffAllNervo()
  if runtime.isStarted('i01.neoPixel'):i01_neoPixel.clear()
  sleep(2)
  if runtime.isStarted('i01.neoPixel'):i01_neoPixel.setAnimation("Larson Scanner", 17, 126, 57, 1)
  if runtime.isStarted('i01.audioPlayer'):
    i01_audioPlayer.stopPlaylist()
    i01_audioPlayer.stop()
  
  #restart pir poling
  if runtime.isStarted('i01.pir'):
    if i01.getConfig().pirWakeUp==1:
      initPir()
      i01_pir.enable()
    else:
      i01_pir.disable()
    
def wakeUpModeInsult():
  if runtime.isStarted('i01.ear'):
    WaitXsecondBeforeRelaunchTracking=-10
    i01_ear.setWakeWord(i01_ear.getConfig().wakeWord)
    i01_ear.apply()
    i01_ear.setAwake(True)
    i01_ear.startRecording()
    if runtime.isStarted('i01.pir'):
      if i01.getConfig().pirWakeUp==1:
        initPir()
        sleepTimer.startClock()
        #i01_ear.setWakeWordTimeout(i01_ear.getConfig().wakeWordIdleTimeoutSeconds)
      else:
        i01_pir.disable()
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.setPredicate('botState', 'awake')
    #if RobotIsStarted==1:  
    if runtime.isStarted('i01.imageDisplay'):
      i01_imageDisplay.closeAll()
    if runtime.isStarted('i01.neoPixel'):i01_neoPixel.setAnimation("Larson Scanner", 0, 255, 0, 25)
      #optional switchon nervoboard
      #switchOnAllNervo()
    if runtime.isStarted('i01.head.eyelidLeft') and runtime.isStarted('i01.head.eyelidRight'):
      i01_head_eyelidLeft.rest()
      i01_head_eyelidRight.rest()
        #i01_head_eyelids.autoBlink(True)
    if runtime.isStarted('i01.head'):
      i01_head_neck.setSpeed(50)
      i01_head_neck.moveToBlocking(i01_head_neck.getRest())
    #RobotIsSleeping=False
    if runtime.isStarted('i01.fsm'):
      i01_fsm.fire("wake")
    if runtime.isStarted('i01.neoPixel'):i01_neoPixel.clear()
    if runtime.isStarted('i01'):
      relax()
      fullspeed()

def sleepModeInsult():
  if runtime.isStarted('i01.ear'):
    initEar()
    i01_ear.setAwake(False)
    #unlockInsult located in ear.py
    i01_ear.setWakeWord(i01.getConfig().unlockInsult)
    if runtime.isStarted('i01.headTracking'):
      initTracking()
      stopTrackHumans()
    i01.halfSpeed()
    rest()
    i01.waitTargetPos()
    #display sleeping robot on screen
    if runtime.isStarted('i01.imageDisplay'):
      i01_imageDisplay.closeAll()
      sleep(1)
      i01_imageDisplay.display('resource/InMoov2/system/pictures/sleeping_2_1024-600.jpg')
    #head down
    if runtime.isStarted('i01.head.eyelidLeft') and runtime.isStarted('i01.head.eyelidRight'):
      #i01_head_eyelids.autoBlink(False)
      i01_head_eyelidLeft.moveTo(0)
      i01_head_eyelidRight.moveTo(0)
    if runtime.isStarted('i01.head'):
      i01_head_neck.setSpeed(80)
      i01_head_neck.moveTo(10)
    i01.waitTargetPos()
    if runtime.isStarted('i01.rightHand') or runtime.isStarted('i01.leftHand'):
      handsclose()
    i01.disable()
    #switchOffAllNervo()
    sleep(2)
    if runtime.isStarted('i01.fsm'):
      i01_fsm.fire("sleep")
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.setPredicate('botState', 'sleeping')  
    #restart pir poling
    if runtime.isStarted('i01.pir'):
      if i01.getConfig().pirWakeUp==1:
        i01_pir.disable()
    sleep(1)
    if runtime.isStarted('i01.neoPixel'):i01_neoPixel.setAnimation("Ironman", 255, 0, 0, 50)
    
def welcomeMessage():
  if runtime.isStarted('i01.mouth'):
    initMouth()
  if runtime.isStarted('i01.fsm'):
    i01_fsm.fire("wake")
  if runtime.isStarted('i01.ear'):
    i01_ear.setAwake(True)
    i01_ear.startRecording()  
  if runtime.isStarted('i01.chatBot'):
    if str(i01_chatBot.getPredicate("human","firstinit"))=="unknown" or str(i01_chatBot.getPredicate("human","firstinit"))=="started":
      i01_chatBot.setPredicate("human","topic","default")
      i01_chatBot.getResponse("FIRST_INIT")
    else:
      i01_chatBot.getResponse("WAKE_UP")
  else:
    if runtime.isStarted('i01'):
      runtime.info("i01 is ready")
  if runtime.isStarted('i01.llm'):
    initLlm()     

global WaitXsecondBeforeRelaunchTracking
WaitXsecondBeforeRelaunchTracking=-10

def humanDetected():
  global WaitXsecondBeforeRelaunchTracking
  WaitXsecondBeforeRelaunchTracking+=1
  if runtime.isStarted('i01.pir'):
    if i01.getConfig().pirWakeUp==1:
      initPir()
      sleepTimer.restartClock()
      #i01_ear.setWakeWordTimeout(i01_ear.getConfig().wakeWordIdleTimeoutSeconds)
  if runtime.isStarted('i01.fsm'):
    if not i01_fsm.getState()=="isTracking" and WaitXsecondBeforeRelaunchTracking>=5:
      WaitXsecondBeforeRelaunchTracking=0
      if runtime.isStarted('i01.headTracking'):
        initTracking()
        if i01.getConfig().pirEnableTracking==1:
          trackHumans()
          trackingTimer.restartClock()
      #if i01.getConfig().openCVFaceRecognizerActivated==1:facerecognizer()
    else:
      i01_fsm.fire("idle")
      #print "idle state"
      #print WaitXsecondBeforeRelaunchTracking
    
def sleepTimerRoutine(timedata):
  if runtime.isStarted('i01.fsm'):
    if not i01_fsm.getState()=="sleep":
      if runtime.isStarted('i01.neoPixel'):i01_neoPixel.setAnimation("Color Wipe", 17,  126, 57, 20)
      if runtime.isStarted("i01.pir"):
        i01_pir.disable()
        #pirControlerArduino.disablePin(pirPin)
      #sleep function to call
      sleepTimer.stopClock()
      #i01_ear.setAwake(True)
      if runtime.isStarted('i01.headTracking'):
        initTracking()   
        trackingTimer.stopClock()   
      sleepModeSleep()
  
def trackingTimerRoutine(timedata):
  global WaitXsecondBeforeRelaunchTracking
  if runtime.isStarted('i01.fsm'):
    if i01_fsm.getState()=="isTracking":
      WaitXsecondBeforeRelaunchTracking=-5
      if runtime.isStarted('i01.headTracking'):
        initTracking()
        stopTrackHumans()
        #print "trackingTimer stopped"
        #print WaitXsecondBeforeRelaunchTracking
        trackingTimer.stopClock()
      if runtime.isStarted('i01.neoPixel'):i01_neoPixel.clear()

print("sleepMode.py loaded")
