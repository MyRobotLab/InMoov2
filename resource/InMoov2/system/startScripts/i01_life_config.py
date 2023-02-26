#########################################
# i01_life_config.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

import os
configFilename="i01.life.yml"
def saveConfig(configFilename):
    configPath='data/InMoov2/'
    configFile = configFilename
    configWriter = 0
    configWriter = open(configPath+configFile, "w+")
    L =[
    "# !!org.myrobotlab.service.config.LifeConfig\n"
    "\n"
    "# Settings for the robots life\n"
    "# False:0\n"
    "# True:1\n"
    "\n"
    "[HEALTHCHECK]\n"
    "healthCheckActivated=True\n"
    "TimerValue=60000\n"
    "BatteryInSystem=False\n"
    "\n"
    "[WAKE]\n"
    "unlockInsult=forgive me\n"
    "wakeUpWord=wake up\n"
    "\n"
    "# ramdom move the head\n"
    "[MOVEHEADRANDOM]\n"
    "RobotCanMoveHeadWhileSpeaking=True\n"
    "ForceMicroOnIfSleeping=True\n"
    "\n"
    "[SLEEPMODE]\n"
    "Activated=True\n"
    "pirWakeUp=True\n"
    "pirEnableTracking=False\n"
    "\n"
    "# Sleep 5 minutes after last presence detected\n"
    "SleepTimeout=300000\n"
    "\n"
    "# Turn off tracking 20 seconds after last presence detected\n"
    "TrackingTimeout=10000\n"
    ]
    configWriter.writelines(L)
    configWriter.close()

saveConfig(configFilename)
