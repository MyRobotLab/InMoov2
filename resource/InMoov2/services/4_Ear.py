# ##############################################################################
#                 EAR SERVICE FILE
# ##############################################################################

# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')

EarEngine=ThisServicePartConfig.get('MAIN', 'EarEngine')
setContinuous=ThisServicePartConfig.getboolean('MAIN', 'setContinuous')
setAutoListen=ThisServicePartConfig.getboolean('MAIN', 'setAutoListen')
ForceMicroOnIfSleeping=True
lockPhrase="wake up"
unlockInsult="forgive me"
try:
  ForceMicroOnIfSleeping=ThisServicePartConfig.getboolean('MAIN', 'ForceMicroOnIfSleeping')
  lockPhrase=unicode(ThisServicePartConfig.get('MAIN', 'MagicCommandToWakeUp'),'utf-8')
except:
  pass

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################
i01_ear=runtime.create("i01.ear", EarEngine)
#ear=i01_ear

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
