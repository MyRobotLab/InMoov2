#########################################
# i01_life_config.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

import os
ThisFilePart = 'data/InMoov2/i01.life.yml'
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
    "healthCheckActivated=False\n"
    "timerValue=60000\n"
    "batteryInSystem=False\n"
    "\n"
    "[WAKE]\n"
    "unlockInsult=forgive me\n"
    "\n"
    "# ramdom move the head\n"
    "[MOVEHEADRANDOM]\n"
    "robotCanMoveHeadWhileSpeaking=True\n"
    "forceMicroOnIfSleeping=True\n"
    "\n"
    "[SLEEPMODE]\n"
    "pirWakeUp=True\n"
    "pirEnableTracking=False\n"
    "# Sleep 5 minutes after last presence detected\n"
    "sleepTimeout=300000\n"
    "# Turn off tracking 20 seconds after last presence detected\n"
    "trackingTimeout=10000\n"
    "\n"
    "[AUDIO]\n"
    "startupSound=True\n"
    "customSound=True\n"
    "audioSignalProcessing=False\n"
    "analogPinFromSoundCard=53\n"
    "howManyPollsBySecond=2\n"
    "\n"
    "[NEOPIXEL]\n"
    "boot_green=True\n"
    "download_blue=True\n"
    "error_red=True\n"
    "flash_when_speak=True\n"
    "\n"
    "[OPENCV]\n"
    "flipPicture=False\n"
    "faceRecognizerActivated=True\n"
    ]
    configWriter.writelines(L)
    configWriter.close()


def CheckLifeExist(File):
  if not os.path.isfile(File):
    saveConfig(configFilename)
    runtime.info("custom file created : data/InMoov2/i01.life.yml")

CheckLifeExist(ThisFilePart)
