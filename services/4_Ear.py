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
  python.subscribe(i01_ear.getName(),"publishRecognized")  

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
def onRecognized(text):
  if text!="":
    global lastRecognized
    lastRecognized=text
    #if i01.RobotIsStarted:
    #if unicode(text,'utf-8')==unlockInsult:wakeUpModeInsult()
    #if runtime.isStarted('i01.chatBot'):
      #if i01_chatBot.onText()=="SYSTEM_EVENT WAKE" and unicode(text,'utf-8')==lockPhrase:sleepModeWakeUp()
      #if i01_chatBot.onText()=="SYSTEM_EVENT WAKE" and text!=lockPhrase:
        #i01_chatBot.getResponse(text)
    humanDetected()

if i01.getConfig().forceMicroOnIfSleeping==1:
  watchMicro = runtime.start("watchMicro","Clock")
  # set our watchMicro to fire if its not reset within a second
  watchMicro.setInterval(60000) 
  # add the stop command which will stop the robot from moving
  watchMicro.addClockEvent("python","exec", "restartListening()")
  # start the clock
  watchMicro.startClock()

# define the method that will stop the robot
def restartListening():
  if runtime.isStarted('i01.ear'):
    if not i01_ear.isListening():
      i01_ear.startListening()
      print("restarting listening")
    else:
      pass
  else:
      pass
