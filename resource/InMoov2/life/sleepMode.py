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
   sleepTimer.setInterval(sleepTimeout)

if runtime.isStarted('i01.headTracking') or runtime.isStarted('i01.eyeTracking'):
   trackingTimer = runtime.start("trackingTimer","Clock")
   trackingTimer.addListener("pulse", python.name, "trackingTimerRoutine")
   trackingTimer.setInterval(trackingTimeout)  

def sleepModeWakeUp():
  i01_fsm.fire("wake")
  if runtime.isStarted('i01.mouth'):
    initMouth()
  if runtime.isStarted('i01.ear'):
    initEar()
    i01_ear.setAwake(True)
    WaitXsecondBeforeRelaunchTracking=-10
    i01_ear.startRecording()
  if runtime.isStarted('i01.pir'):
      if pirWakeUp==1:
        initPir()
        sleepTimer.startClock()
      else:  
        i01_pir.disable()
  #if RobotIsStarted==1:
  if i01_fsm.getCurrent()=="awake" or "systemCheck":
    
    if runtime.isStarted('i01.imageDisplay'):
      i01_imageDisplay.closeAll()
    
    #display(RuningFolder+'/system/pictures/loading_1024-600.jpg')
    
    if runtime.isStarted('i01.neoPixel'):
      i01_neoPixel.setAnimation("Larson Scanner", 255, 255, 0, 25)
      sleep(2)
      i01_neoPixel.stopAnimation()
    #optional switchon nervoboard
    #switchOnAllNervo()
    if runtime.isStarted('i01.eyeLids'):
      i01_head_eyelidLeft.moveTo(0)
      i01_head_eyelidRight.moveTo(0)
      i01_head_eyelids.autoBlink(True)
          #head up
    if runtime.isStarted('i01.head'):
      i01_head_neck.setSpeed(50)
      i01_head_neck.moveToBlocking(i01_head_neck.getRest())
    if customSound==1:
      i01_audioPlayer=runtime.start('i01_audioPlayer','AudioFile')
      i01_audioPlayer.playFile('resource/InMoov2/system/sounds/Notifications/'+random.choice(os.listdir('resource/InMoov2/system/sounds/Notifications')),False)
    elif runtime.isStarted('i01.opencv'):
          if faceRecognizerActivated==1:
             facerecognizer()
          else:
             welcomeMessage()     
    else:
       welcomeMessage()
   
    if runtime.isStarted('i01'):fullspeed()


def sleepModeSleep():
  if runtime.isStarted('i01.ear'):
    initEar()
    i01_ear.setAwake(False)
    print("sleeping")
    if runtime.isStarted('i01.headTracking'):
      initTracking()
      stopTrackHumans()
    if runtime.isStarted('i01.opencv'):
      i01_opencv.stopCapture()  
    if runtime.isStarted('i01.imageDisplay'):
      i01_imageDisplay.closeAll()
    i01_fsm.fire("sleep")
    i01.halfSpeed()
    rest()
    i01.waitTargetPos()
    #display sleeping robot on screen
    if runtime.isStarted('i01.imageDisplay'):
      i01_imageDisplay.display('resource/InMoov2/system/pictures/sleeping_2_1024-600.jpg')
    #head down
    if runtime.isStarted('i01.eyeLids'):
      i01_head_eyelids.autoBlink(False)
      i01_head_eyelidLeft.moveTo(180)
      i01_head_eyelidRight.moveTo(180)
    if runtime.isStarted('i01.head'):
      i01_head_neck.setSpeed(40)
      i01_head_neck.moveTo(10)
    i01.waitTargetPos()
    i01.disable()
    #switchOffAllNervo()
    if runtime.isStarted('i01.neoPixel'):i01_neoPixel.stopAnimation()
    sleep(2)
    if runtime.isStarted('i01.neoPixel'):i01_neoPixel.setAnimation("Color Wipe", 10, 12, 12, 20)
    if runtime.isStarted('i01.audioPlayer'):
      i01_audioPlayer.stopPlaylist()
      i01_audioPlayer.stop()
    
    #restart pir poling
    if runtime.isStarted('i01.pir'):
      if pirWakeUp==1:
        initPir()
        i01_pir.enable()
      else:
        i01_pir.disable()
    
def wakeUpModeInsult():
  if runtime.isStarted('i01.ear'):
    initEar()
    WaitXsecondBeforeRelaunchTracking=-10
    i01_ear.setAwake(True)
    i01_ear.unsetWakeWord(unlockInsult)
    i01_ear.startRecording()
    if runtime.isStarted('i01.pir'):
      if pirWakeUp==1:
        initPir()
        sleepTimer.startClock()
      else:
        i01_pir.disable()
    
    #if RobotIsStarted==1:
    if i01_fsm.getCurrent()=="applyingConfig" or "systemCheck":  
      if runtime.isStarted('i01.imageDisplay'):
        i01_imageDisplay.closeAll()
      if runtime.isStarted('i01.neoPixel'):i01_neoPixel.setAnimation("Larson Scanner", 0, 255, 0, 25)
      #optional switchon nervoboard
      #switchOnAllNervo()
      if runtime.isStarted('i01.eyeLids'):
        i01_head_eyelidLeft.moveTo(0)
        i01_head_eyelidRight.moveTo(0)
        i01_head_eyelids.autoBlink(True)
            #head up
      if runtime.isStarted('i01.head'):
        i01_head_neck.setSpeed(50)
        i01_head_neck.moveToBlocking(i01_head_neck.getRest())
    else:
      relax()
    #RobotIsSleeping=False
    i01_fsm.fire("wake")
    if runtime.isStarted('i01.neoPixel'):i01_neoPixel.stopAnimation()
    if runtime.isStarted('i01'):
      relax()
      fullspeed()

def sleepModeInsult():
  if runtime.isStarted('i01.ear'):
    initEar()
    i01_ear.setAwake(False)
    if runtime.isStarted('i01.headTracking'):
      initTracking()
      stopTrackHumans()
    if runtime.isStarted('i01.imageDisplay'):
      i01_imageDisplay.closeAll()
    #unlockInsult located in ear.py
    i01_ear.setWakeWord(unlockInsult)
    i01.halfSpeed()
    rest()
    i01.waitTargetPos()
    #display sleeping robot on screen
    if runtime.isStarted('i01.imageDisplay'):
      i01_imageDisplay.displayPic('resource/InMoov2/system/pictures/sleeping_2_1024-600.jpg')
    #head down
    if runtime.isStarted('i01.eyeLids'):
      i01_head_eyelids.autoBlink(False)
      i01_head_eyelidLeft.moveTo(180)
      i01_head_eyelidRight.moveTo(180)
    if runtime.isStarted('i01.head'):
      i01_head_neck.setSpeed(80)
      i01_head_neck.moveTo(10)
    i01.waitTargetPos()
    if runtime.isStarted('i01.rightHand') or runtime.isStarted('i01.leftHand'):
      handsclose()
    i01.disable()
    #switchOffAllNervo()
    sleep(2)
    #restart pir poling
    if runtime.isStarted('i01.pir'):
      if pirWakeUp==1:
        initPir()
        i01_pir.enable()
      else:
        i01_pir.disable()
    sleep(1)
    if runtime.isStarted('i01.neoPixel'):i01_neoPixel.setAnimation("Ironman", 255, 0, 0, 1)
    
def welcomeMessage():
  if runtime.isStarted('i01.mouth'):
    initMouth()
  if runtime.isStarted('i01.chatBot'):
    if str(i01_chatBot.getPredicate("human","firstinit"))=="unknown" or str(i01_chatBot.getPredicate("human","firstinit"))=="started":
      i01_chatBot.setPredicate("human","topic","default")
      i01_chatBot.getResponse("FIRST_INIT")
    else:
      i01_chatBot.getResponse("WAKE_UP")
  else:
    if runtime.isStarted('i01'):
      i01.speakBlocking(i01.localize("ready"))
  #RobotIsStarted=True
  i01_fsm.fire("systemCheck")

global WaitXsecondBeforeRelaunchTracking
WaitXsecondBeforeRelaunchTracking=-10

def humanDetected():
  global WaitXsecondBeforeRelaunchTracking
  WaitXsecondBeforeRelaunchTracking+=1
  if runtime.isStarted('i01.pir'):
    if pirWakeUp==1:
      initPir()
      sleepTimer.restartClock()
    if (not i01_headTracking and WaitXsecondBeforeRelaunchTracking>=5):
      WaitXsecondBeforeRelaunchTracking=0
      if runtime.isStarted('i01.neoPixel'):i01_neoPixel.setAnimation("Larson Scanner", 255, 0, 255, 25)
      if runtime.isStarted('i01.headTracking'):
        initTracking()
        if pirEnableTracking==1:
          trackHumans()
          trackingTimer.restartClock()
      if faceRecognizerActivated==1:facerecognizer()
    
def sleepTimerRoutine(timedata):
  #if RobotIsSleeping==0:
  if not i01_fsm.getCurrent()=="sleeping":
    if runtime.isStarted('i01.neoPixel'):i01_neoPixel.setAnimation("Larson Scanner", 17, 126, 57, 1)
    if runtime.isStarted("i01.pir"):
      i01_pir.disable()
      #pirControlerArduino.disablePin(pirPin)
    #sleep function to call
    sleepTimer.stopClock()
    if runtime.isStarted('i01.headTracking'):
      initTracking()   
      trackingTimer.stopClock()
    sleepModeSleep()
  
def trackingTimerRoutine(timedata):
  global WaitXsecondBeforeRelaunchTracking
  print "trackingTimer stopped"
  if i01_opencv.isTracking():
    WaitXsecondBeforeRelaunchTracking=-5
    if runtime.isStarted('i01.headTracking'):
      initTracking()
      stopTrackHumans()
      trackingTimer.stopClock()
    if runtime.isStarted('i01.neoPixel'):i01_neoPixel.stopAnimation()
