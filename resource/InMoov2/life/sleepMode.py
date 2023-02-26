# ##############################################################################
#                 ROBOT SLEEP MODE
# ##############################################################################

###############################################################################
# check if robot can sleep or wakeup
# only based on pir at this time
###############################################################################
import random

def sleepModeWakeUp():
  i01_ear.clearLock()
  WaitXsecondBeforeRelaunchTracking=-10
  i01_ear.setAutoListen(True)
  if runtime.isStarted('i01.pir'):
      PirControlerArduino.enablePin(PirPin,1)
      SleepTimer.startClock(True)
  
  #if RobotIsStarted==1:
  if i01_fsm.getCurrentState()=="awake" or "systemCheck":
    
    #i01_imageDisplay.exitFS()
    sleep(1)
    i01_imageDisplay.closeAll()
    
    #display(RuningFolder+'/system/pictures/loading_1024-600.jpg')
    
    rdmWakup=random.randint(1,3)
    if rdmWakup==1:
      sleep(0.5)
      i01_audioPlayer.playFile('resource/InMoov2/system/sounds/Notifications/'+random.choice(os.listdir('resource/InMoov2/system/sounds/Notifications')),False)
    elif rdmWakup==2:
      if runtime.isStarted('i01.neopixel'):i01.setNeopixelAnimation("Larson Scanner", 255, 255, 0, 1)
      sleep(2)
      if runtime.isStarted('i01.neopixel'):i01.stopNeopixelAnimation()
    else: welcomeMessage()
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
    welcomeMessage()
    #RobotIsSleeping=False
    i01_fsm.fire("wake")
  if runtime.isStarted('i01.neopixel'):i01.stopNeopixelAnimation()
  fullspeed()


def sleepModeSleep():
  i01_ear.setAutoListen(False)
  i01_ear.lockOutAllGrammarExcept(i01_ear.getConfig().wakeWord)
  stopTrackHumans()
  #i01_imageDisplay.exitFS()
  sleep(1)
  i01_imageDisplay.closeAll()
  i01_fsm.fire("sleep")
  i01.halfSpeed()
  rest()
  i01.waitTargetPos()
  #display sleeping robot on screen
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
  if runtime.isStarted('i01.neopixel'):i01.stopNeopixelAnimation()
  sleep(2)
  if runtime.isStarted('i01.neopixel'):i01.setNeopixelAnimation("Color Wipe", 10, 12, 12, 50)
  
  #restart pir poling
  if runtime.isStarted('i01.pir'):
    PirControlerArduino.enablePin(PirPin,1)
    
def wakeUpModeInsult():
  WaitXsecondBeforeRelaunchTracking=-10
  i01_ear.setAutoListen(True)
  i01_ear.clearLock()
  if runtime.isStarted('i01.pir'):
      PirControlerArduino.enablePin(PirPin,1)
      SleepTimer.startClock(True)
  
  #if RobotIsStarted==1:
  if i01_fsm.getCurrentState()=="applyingConfig" or "systemCheck":  
    #i01_imageDisplay.exitFS()
    sleep(1)
    i01_imageDisplay.closeAll()
    if runtime.isStarted('i01.neopixel'):i01.setNeopixelAnimation("Larson Scanner", 0, 255, 0, 1)
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
    if talkToInmoovFrQueue("MRLALIVE")=="OK":i01.speakBlocking(i01.localize("OsSynced"))
    relax()
  #RobotIsSleeping=False
  i01_fsm.fire("wake")
  if runtime.isStarted('i01.neopixel'):i01.stopNeopixelAnimation()
  relax()
  fullspeed()

def sleepModeInsult():
  i01_ear.setAutoListen(False)
  stopTrackHumans()
  #i01_imageDisplay.exitFS()
  sleep(1)
  i01_imageDisplay.closeAll()
  #unlockInsult located in ear.py
  i01_ear.lockOutAllGrammarExcept(unlockInsult)
  i01.halfSpeed()
  rest()
  i01.waitTargetPos()
  #display sleeping robot on screen
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
  if runtime.isStarted('i01.pir'):
    PirControlerArduino.disablePin(PirPin)
  sleep(1)
  if runtime.isStarted('i01.neopixel'):i01.setNeopixelAnimation("Ironman", 255, 0, 0, 1)
    
def welcomeMessage():
  
  if runtime.isStarted('i01.chatBot'):
    if str(i01_chatBot.getPredicate("Friend","firstinit"))=="unknown" or str(i01_chatBot.getPredicate("Friend","firstinit"))=="started":
      i01_chatBot.setPredicate("Friend","topic","default")
      i01_chatBot.getResponse("FIRST_INIT")
    else:
      i01_chatBot.getResponse("WAKE_UP")
  else:
    i01.speakBlocking(i01.localize("ready"))
  #RobotIsStarted=True
  i01_fsm.fire("systemCheck")

global WaitXsecondBeforeRelaunchTracking
WaitXsecondBeforeRelaunchTracking=-10
global autoTrackingStarted
autoTrackingStarted=0

def humanDetected():
  global WaitXsecondBeforeRelaunchTracking
  WaitXsecondBeforeRelaunchTracking+=1
  global autoTrackingStarted
  if runtime.isStarted('i01.pir'):
    SleepTimer.restartClock(True)
    if runtime.isStarted('i01.pir'):
      if (not i01_opencv.isTracking() and WaitXsecondBeforeRelaunchTracking>=5):
        WaitXsecondBeforeRelaunchTracking=0
        if runtime.isStarted('i01.neopixel'):i01.setNeopixelAnimation("Larson Scanner", 255, 0, 255, 1)
        autoTrackingStarted=1
        trackHumans()      
      TrackingTimer.restartClock(True)
    
def SleepTimerRoutine(timedata):
  #if RobotIsSleeping==0:
  if not i01_fsm.getCurrentState()=="sleeping":
    if runtime.isStarted('i01.neopixel'):i01.setNeopixelAnimation("Larson Scanner", 0, 0, 255, 1)
    PirControlerArduino.disablePin(PirPin)
    #sleep function to call
    SleepTimer.stopClock()  
    TrackingTimer.stopClock()
    sleepModeSleep()
  
def TrackingTimerRoutine(timedata):
  global autoTrackingStarted
  global WaitXsecondBeforeRelaunchTracking
  print "TrackingTimer stopped"
  if i01_opencv.isTracking():
    WaitXsecondBeforeRelaunchTracking=-5
    if autoTrackingStarted:
      autoTrackingStarted=0
      stopTrackHumans()
    if runtime.isStarted('i01.neopixel'):i01.stopNeopixelAnimation()
  TrackingTimer.stopClock()    
  
#pir starting  
if runtime.isStarted('i01.pir'):
  SleepTimer = runtime.start("SleepTimer","Clock")
  SleepTimer.addListener("pulse", python.name, "SleepTimerRoutine")
  SleepTimer.setInterval(SleepTimeout)
  TrackingTimer = runtime.start("TrackingTimer","Clock")
  TrackingTimer.addListener("pulse", python.name, "TrackingTimerRoutine")
  TrackingTimer.setInterval(TrackingTimeout)
  PirControlerArduino.addListener("publishPinArray","python","publishPinPir")
  PirControlerArduino.enablePin(PirPin,1)
