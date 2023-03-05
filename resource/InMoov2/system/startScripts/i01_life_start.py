#########################################
# i01_life_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

import ConfigParser
import os
ThisServicePart = 'data/InMoov2/i01.life.yml'

def CheckFileExist(File):
  if not os.path.isfile(File):
    execfile('resource/InMoov2/system/startScripts/i01_life_config.py')
    #i01.info("config file created : data/InMoov2/i01.life.yml")

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart)

healthCheckActivated=ThisServicePartConfig.getboolean('HEALTHCHECK', 'healthCheckActivated')
TimerValue=ThisServicePartConfig.getint('HEALTHCHECK', 'TimerValue')
BatteryInSystem=ThisServicePartConfig.getboolean('HEALTHCHECK', 'BatteryInSystem')

RobotCanMoveHeadWhileSpeaking=ThisServicePartConfig.getboolean('MOVEHEADRANDOM', 'RobotCanMoveHeadWhileSpeaking')
ForceMicroOnIfSleeping=ThisServicePartConfig.getboolean('MOVEHEADRANDOM', 'ForceMicroOnIfSleeping')

Activated=ThisServicePartConfig.getboolean('SLEEPMODE', 'Activated')
unlockInsult=unicode(ThisServicePartConfig.get('WAKE', 'unlockInsult'),'utf-8')
wakeUpWord=unicode(ThisServicePartConfig.get('WAKE', 'wakeUpWord'),'utf-8')
UsePirToWakeUp=ThisServicePartConfig.getboolean('SLEEPMODE', 'pirWakeUp')
UsePirToActivateTracking=ThisServicePartConfig.getboolean('SLEEPMODE', 'pirEnableTracking')
SleepTimeout=ThisServicePartConfig.getint('SLEEPMODE', 'SleepTimeout')
TrackingTimeout=ThisServicePartConfig.getint('SLEEPMODE', 'TrackingTimeout')

#ThisElementPart = 'data/config/InMoov2_Full/i01.ear.yml'

#ThisElementPartConfig = ConfigParser.ConfigParser()
#config.read(ThisElementPart)
#wakeWord=unicode(config.get(ThisElementPart,'wakeWord'),'utf-8')

#with open('data/config/InMoov2_Full/i01.ear.yml', "r") as yamlfile:
    #data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    #print("Read successful")
#print(data[0]['wakeWord'])
#wakeWord=get(ear.getConfig().wakeWord)
#good way:
#print(ear.getConfig().wakeWord)