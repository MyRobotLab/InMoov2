
ThisServicePart = 'data/InMoov2/i01.life.yml'

def CheckFileExist(File):
  if not os.path.isfile(File):
    execfile('resource/InMoov2/system/startScripts/i01_life_config.py')
    i01.info("config file created : data/InMoov2/i01.life.yml")

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart)

healthCheckActivated=ThisServicePartConfig.getboolean('HEALTHCHECK', 'healthCheckActivated')
timerValue=ThisServicePartConfig.getint('HEALTHCHECK', 'timerValue')
batteryInSystem=ThisServicePartConfig.getboolean('HEALTHCHECK', 'batteryInSystem')

robotCanMoveHeadWhileSpeaking=ThisServicePartConfig.getboolean('MOVEHEADRANDOM', 'robotCanMoveHeadWhileSpeaking')
forceMicroOnIfSleeping=ThisServicePartConfig.getboolean('MOVEHEADRANDOM', 'forceMicroOnIfSleeping')

unlockInsult=unicode(ThisServicePartConfig.get('WAKE', 'unlockInsult'),'utf-8')

pirWakeUp=ThisServicePartConfig.getboolean('SLEEPMODE', 'pirWakeUp')
pirEnableTracking=ThisServicePartConfig.getboolean('SLEEPMODE', 'pirEnableTracking')
sleepTimeout=ThisServicePartConfig.getint('SLEEPMODE', 'sleepTimeout')
trackingTimeout=ThisServicePartConfig.getint('SLEEPMODE', 'trackingTimeout')

startupSound=ThisServicePartConfig.getboolean('AUDIO', 'startupSound')
customSound=ThisServicePartConfig.getboolean('AUDIO', 'customSound')
audioSignalProcessing=ThisServicePartConfig.getboolean('AUDIO', 'audioSignalProcessing')
analogPinFromSoundCard=ThisServicePartConfig.getint('AUDIO', 'analogPinFromSoundCard')
howManyPollsBySecond=ThisServicePartConfig.getint('AUDIO', 'howManyPollsBySecond')

boot_green=ThisServicePartConfig.getboolean('NEOPIXEL', 'boot_green')
download_blue=ThisServicePartConfig.getboolean('NEOPIXEL', 'download_blue')
error_red=ThisServicePartConfig.getboolean('NEOPIXEL', 'error_red')
flash_when_speak=ThisServicePartConfig.getboolean('NEOPIXEL', 'flash_when_speak')

flipPicture=ThisServicePartConfig.getboolean('OPENCV', 'flipPicture')
faceRecognizerActivated=ThisServicePartConfig.getboolean('OPENCV', 'faceRecognizerActivated')

