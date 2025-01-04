# -- coding: utf-8 --
# ##############################################################################
#                 EAR SERVICE FILE
# ##############################################################################  


# ##############################################################################
#                SET SERVICE
# ##############################################################################
en = 'en-US'
fi = 'fi-FI'
fr = 'fr-FR'
hi = 'hi-IN'
es = 'es-ES'
de = 'de-DE'
it = 'it-IT'
nl = 'nl-NL'
pl = 'pl-PL'
pt = 'pt-PT'
ru = 'ru-RU'
tr = 'tr-TR'
def initEar():
  i01_ear.getConfig()
  lockPhrase = i01_ear.getConfig().wakeWord
  i01_ear.setWakeWordTimeout(5000)
  if lockPhrase==None:
    if runtime.getLocale().getTag() == en:
      i01_ear.setWakeWord(u'wake up')
    if runtime.getLocale().getTag() == fi:
      i01_ear.setWakeWord(u'herää')
    if runtime.getLocale().getTag() == fr:
      i01_ear.setWakeWord(u'réveille-toi')
    if runtime.getLocale().getTag() == hi:
      i01_ear.setWakeWord(u'उठो')
    if runtime.getLocale().getTag() == es:
      i01_ear.setWakeWord(u'despiértate')
    if runtime.getLocale().getTag() == de:
      i01_ear.setWakeWord(u'aufwachen')
    if runtime.getLocale().getTag() == it:
      i01_ear.setWakeWord(u'svegliati')
    if runtime.getLocale().getTag() == nl:
      i01_ear.setWakeWord(u'waker worden')
    if runtime.getLocale().getTag() == pl:
      i01_ear.setWakeWord(u'budzić się')
    if runtime.getLocale().getTag() == pt:
      i01_ear.setWakeWord(u'acorde')
    if runtime.getLocale().getTag() == ru:
      i01_ear.setWakeWord(u'просыпайся')
    if runtime.getLocale().getTag() == tr:
      i01_ear.setWakeWord(u'uyanmak')
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
  watchMicro.addClockEvent("python","exec", "restartListening()")
  # start the clock
  watchMicro.startClock()
if i01.getConfig().forceMicroOnIfSleeping==0:
  runtime.release("watchMicro")  

def earON():
  if runtime.isStarted('i01.ear'):
    i01_ear.setAwake(True)
    i01_ear.startRecording()
  else:  
    ear = runtime.start("i01.ear","WebkitSpeechRecognition")
    ear.startListening()
  if i01.getConfig().forceMicroOnIfSleeping==1:
    if runtime.isStarted('watchMicro'):
      pass
    else:
      watchMicro = runtime.start("watchMicro","Clock")
      # set our watchMicro to fire if its not reset within a second
      watchMicro.setInterval(60000) 
      watchMicro.addClockEvent("python","exec", "restartListening()")
      # start the clock
      watchMicro.startClock()

    
def earOFF():
  initEar()
  if runtime.isStarted('watchMicro'):
    runtime.release('watchMicro')
  if runtime.isStarted('i01.ear'):
    i01_ear.setAwake(False)


# define the method that will restart the listening
def restartListening():
  if runtime.isStarted('i01.ear'):
    if not i01_ear.isListening():
      i01_ear.startListening()
      print("restarting listening")
    else:
      pass
  else:
      pass
