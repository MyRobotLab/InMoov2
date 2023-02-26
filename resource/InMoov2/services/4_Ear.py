# ##############################################################################
#                 EAR SERVICE FILE
# ##############################################################################  


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################
#i01_ear=runtime.create("i01.ear", "WebkitSpeechRecognition")
if runtime.isStarted('i01.ear'):
  ear=i01_ear
  lockPhrase=ear.getConfig().wakeWord
unlockInsult="forgive me"

# ##############################################################################
# MRL SERVICE TWEAKS
# ##############################################################################

# this function catch the ear listening

global lastRecognized
lastRecognized=""
def onRecognized(text):
  if text!="":
    global lastRecognized
    lastRecognized=text
    #if i01.RobotIsStarted:
    if runtime.isStarted('i01.fsm'):
      if i01_fsm.getCurrentState(wake):  
        if runtime.isStarted('i01.chatBot'):
          if i01_fsm.getCurrentState()=="sleeping" and unicode(text,'utf-8')==lockPhrase:sleepModeWakeUp()
          if i01_fsm.getCurrentState()=="wake" and not unicode(text,'utf-8')==lockPhrase:humanDetected()
