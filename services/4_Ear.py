# ##############################################################################
#                 EAR SERVICE FILE
# ##############################################################################  


# ##############################################################################
#                SET SERVICE
# ##############################################################################

def initEar():
  i01_ear.getConfig()
  lockPhrase = i01_ear.getConfig().wakeWord
  i01_ear.setWakeWordTimeout(5000)
  if lockPhrase==None:
    i01_ear.setWakeWord('wake up')
  python.subscribe(i01_ear.getName(),"recognized")  

#if runtime.isStarted('i01.ear'):
  #ear=i01_ear
  #lockPhrase=ear.getConfig().wakeWord
  #unlockInsult="forgive me"
#else:
  #i01_ear=runtime.start("i01.ear", "WebkitSpeechRecognition")
  #ear=i01_ear
  #lockPhrase=ear.getConfig().wakeWord  

# ##############################################################################
# MRL SERVICE TWEAKS
# ##############################################################################

# this function catch the ear listening

global lastRecognized
lastRecognized=""
def publishRecognized(text):
  if text!="":
    global lastRecognized
    lastRecognized=text
    #if i01.RobotIsStarted:
    if runtime.isStarted('i01.fsm'):
      if i01_fsm.getCurrent()=="applyingConfig" or "systemCheck":
        if runtime.isStarted('i01.chatBot'):
          if i01_fsm.getCurrent()=="sleeping" and unicode(text,'utf-8')==lockPhrase:sleepModeWakeUp()
          if i01_fsm.getCurrent()=="awake" and text!=lockPhrase:
            if runtime.isStarted('i01.chatBot'):
              i01_chatBot.getResponse(text)
            humanDetected()