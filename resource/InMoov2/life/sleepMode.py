# ##############################################################################
#                 ROBOT SLEEP MODE
# ##############################################################################

###############################################################################
# check if robot can sleep or wakeup
# only based on pir at this time
###############################################################################

def sleepModeWakeUp():
  i01_ear.clearLock()
  WaitXsecondBeforeRelaunchTracking=-10
  ear.setAutoListen(setAutoListen)
  if isPirActivated:
      PirControlerArduino.enablePin(PirPin,1)
      SleepTimer.startClock(True)
  
  if i01.RobotIsStarted:
    
    imagedisplay.exitFS()
    sleep(1)
    imagedisplay.closeAll()
    
    #display(RuningFolder+'/system/pictures/loading_1024-600.jpg')
    
    rdmWakup=random.randint(1,3)
    if rdmWakup==1:
      sleep(0.5)
      if PlayCustomSoundIfDetection:i01_audioPlayer.playFile(RuningFolder+'/system/sounds/Notifications/'+random.choice(os.listdir(RuningFolder+'/system/sounds/Notifications')),False)
    elif rdmWakup==2:
      if isNeopixelActivated:i01.setNeopixelAnimation("Larson Scanner", 255, 255, 0, 1)
      sleep(2)
      if isNeopixelActivated:i01.stopNeopixelAnimation()
    else: welcomeMessage()
    #optional switchon nervoboard
    switchOnAllNervo()
    if isEyeLidsActivated:
      eyelids.eyelidLeft.moveTo(0)
      eyelids.eyelidRight.moveTo(0)
      eyelids.autoBlink(True)
          #head up
    if isHeadActivated:
      head.neck.setSpeed(50)
      head.neck.moveToBlocking(head.neck.getRest())
  else:
    welcomeMessage()
  i01.RobotIsSleeping=False
  if isNeopixelActivated:i01.stopNeopixelAnimation()
  fullspeed()


def sleepModeSleep():
  if not ForceMicroOnIfSleeping:ear.setAutoListen(False)
  i01_ear.lockOutAllGrammarExcept(lockPhrase)
  stopTracking()
  imagedisplay.exitFS()
  sleep(1)
  imagedisplay.closeAll()
  i01.RobotIsSleeping=True
  i01.halfSpeed()
  rest()
  i01.waitTargetPos()
  #display sleeping robot on screen
  display(RuningFolder+'/system/pictures/sleeping_2_1024-600.jpg')
  #head down
  if isEyeLidsActivated:
    eyelids.autoBlink(False)
    eyelids.eyelidLeft.moveTo(180)
    eyelids.eyelidRight.moveTo(180)
  if isHeadActivated:
    head.neck.setSpeed(40)
    head.neck.moveTo(10)
  i01.waitTargetPos()
  i01.disable()
  switchOffAllNervo()
  if isNeopixelActivated:i01.stopNeopixelAnimation()
  sleep(2)
  if isNeopixelActivated:i01.setNeopixelAnimation("Color Wipe", 10, 12, 12, 50)
  
  #restart pir poling
  if isPirActivated:
    PirControlerArduino.enablePin(PirPin,1)
    
def wakeUpModeInsult():
  WaitXsecondBeforeRelaunchTracking=-10
  ear.setAutoListen(setAutoListen)
  i01_ear.clearLock()
  if isPirActivated:
      PirControlerArduino.enablePin(PirPin,1)
      SleepTimer.startClock(True)
  
  if i01.RobotIsStarted: 
    imagedisplay.exitFS()
    sleep(1)
    imagedisplay.closeAll()
    if isNeopixelActivated:i01.setNeopixelAnimation("Larson Scanner", 0, 255, 0, 1)
    #optional switchon nervoboard
    switchOnAllNervo()
    if isEyeLidsActivated:
      eyelids.eyelidLeft.moveTo(0)
      eyelids.eyelidRight.moveTo(0)
      eyelids.autoBlink(True)
          #head up
    if isHeadActivated:
      head.neck.setSpeed(50)
      head.neck.moveToBlocking(head.neck.getRest())
  else:
    if talkToInmoovFrQueue("MRLALIVE")=="OK":i01.speakBlocking(i01.localize("OsSynced"))
    relax()
  i01.RobotIsSleeping=False
  if isNeopixelActivated:i01.stopNeopixelAnimation()
  relax()
  fullspeed()

def sleepModeInsult():
  if not ForceMicroOnIfSleeping:ear.setAutoListen(False)
  stopTracking()
  imagedisplay.exitFS()
  sleep(1)
  imagedisplay.closeAll()
  #unlockInsult located in ear.py
  i01_ear.lockOutAllGrammarExcept(unlockInsult)
  i01.halfSpeed()
  rest()
  i01.waitTargetPos()
  #display sleeping robot on screen
  displayPic(RuningFolder+'/system/pictures/sleeping_2_1024-600.jpg')
  #head down
  if isEyeLidsActivated:
    eyelids.autoBlink(False)
    eyelids.eyelidLeft.moveTo(180)
    eyelids.eyelidRight.moveTo(180)
  if isHeadActivated:
    head.neck.setSpeed(80)
    head.neck.moveTo(10)
  i01.waitTargetPos()
  if isRightHandActivated or isLeftHandActivated:
    handsclose()
  i01.disable()
  switchOffAllNervo()
  sleep(2)
  if isPirActivated:
    PirControlerArduino.disablePin(PirPin)
  sleep(1)
  if isNeopixelActivated:i01.setNeopixelAnimation("Ironman", 255, 0, 0, 1)
    
def welcomeMessage():
  
  if isChatBotActivated:
    if str(i01_chatBot.getPredicate("Friend","firstinit"))=="unknown" or str(i01_chatBot.getPredicate("Friend","firstinit"))=="started":
      i01_chatBot.setPredicate("Friend","topic","default")
      i01_chatBot.getResponse("FIRST_INIT")
    else:
      i01_chatBot.getResponse("WAKE_UP")
  else:
    i01.speakBlocking(i01.localize("ready"))
  i01.RobotIsStarted=True

global WaitXsecondBeforeRelaunchTracking
WaitXsecondBeforeRelaunchTracking=-10
global autoTrackingStarted
autoTrackingStarted=0

def humanDetected():
  global WaitXsecondBeforeRelaunchTracking
  WaitXsecondBeforeRelaunchTracking+=1
  global autoTrackingStarted
  if isPirActivated:
    SleepTimer.restartClock(True)
    if (isOpenCvActivated and UsePirToActivateTracking):
      if (not i01_vision.isTracking() and WaitXsecondBeforeRelaunchTracking>=5):
        WaitXsecondBeforeRelaunchTracking=0
        if isNeopixelActivated:i01.setNeopixelAnimation("Larson Scanner", 255, 0, 255, 1)
        autoTrackingStarted=1
        trackHumans()      
      TrackingTimer.restartClock(True)
    
def SleepTimerRoutine(timedata):
  if not i01.RobotIsSleeping:
    if isNeopixelActivated:i01.setNeopixelAnimation("Larson Scanner", 0, 0, 255, 1)
    PirControlerArduino.disablePin(PirPin)
    #sleep function to call
    SleepTimer.stopClock()  
    TrackingTimer.stopClock()
    sleepModeSleep()
  
def TrackingTimerRoutine(timedata):
  global autoTrackingStarted
  global WaitXsecondBeforeRelaunchTracking
  print "TrackingTimer stopped"
  if i01_vision.isTracking():
    WaitXsecondBeforeRelaunchTracking=-5
    if autoTrackingStarted:
      autoTrackingStarted=0
      stopTracking()
    if isNeopixelActivated:i01.stopNeopixelAnimation()
  TrackingTimer.stopClock()    
  
#pir starting  
if isPirActivated:
  SleepTimer = Runtime.createAndStart("SleepTimer","Clock")
  SleepTimer.addListener("pulse", python.name, "SleepTimerRoutine")
  SleepTimer.setInterval(SleepTimeout)
  TrackingTimer = Runtime.createAndStart("TrackingTimer","Clock")
  TrackingTimer.addListener("pulse", python.name, "TrackingTimerRoutine")
  TrackingTimer.setInterval(TrackingTimeout)
  PirControlerArduino.addListener("publishPinArray","python","publishPinPir")
  PirControlerArduino.enablePin(PirPin,1)
