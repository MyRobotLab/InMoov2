# ##############################################################################
#                 EAR SERVICE FILE
# ##############################################################################

# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart = str(ConfigType)+'i01.ear.yml'

CheckFileExist(ThisServicePart)


ThisServicePartConfig = CodecUtils.readServiceConfig(ThisServicePart)

EarEngine=ThisServicePartConfig.type
#setContinuous=ThisServicePartConfig.getboolean('MAIN', 'setContinuous')
#setAutoListen=ThisServicePartConfig.getboolean('MAIN', 'setAutoListen')
ForceMicroOnIfSleeping=True
#lockPhrase=ThisServicePartConfig.wakeWord
unlockInsult="forgive me"
try:
  #ForceMicroOnIfSleeping=ThisServicePartConfig.getboolean('MAIN', 'ForceMicroOnIfSleeping')
  lockPhrase=unicode(ThisServicePartConfig.wakeWord,'utf-8')
except:
  pass

#for noworky
log.info("4_Ear.py")  
log.info("lockPhrase : "+str(ThisServicePartConfig.wakeWord))
log.info("unlockInsult : "+str(unlockInsult))

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################
i01_ear=Runtime.start("i01.ear", EarEngine)
ear=i01_ear

# ##############################################################################
# MRL SERVICE TWEAKS
# ##############################################################################

# this function catch the ear listening

global lastRecognized
lastRecognized=""
def onRecognized(text):
  #RobotneedUpdate : fix about first question do you want to update
  if text!="":
    global lastRecognized
    lastRecognized=text
    if i01.RobotIsStarted:
      if isChatBotActivated:
        if i01.RobotIsSleeping and unicode(text,'utf-8')==lockPhrase:sleepModeWakeUp()
      if not i01.RobotIsSleeping and not unicode(text,'utf-8')==lockPhrase:
        humanDetected()
