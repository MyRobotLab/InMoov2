# ##############################################################################
#                 CONFIGPARSER FILE
# ##############################################################################

#shared parse function
def CheckFileExist(File):
  global RobotIsErrorMode
  #FIXME
  try:
    os.path.isfile(File)
      #shutil.move(File+'.config.default',File+'.config')
    #log.info("Reading: "+str(File))
  except:
    log.info("File does not exist: "+str(File))
    pass 

# PARSE THE CONFIG FILE, WE NEED TO GET THE SELECTED CONFIG IN THE UI
print ("Selected config : "+str(ConfigType))

CheckFileExist(str(ConfigType)+'runtime.yml')
   
RuntimeConfig = CodecUtils.readServiceConfig(str(ConfigType)+'runtime.yml')
Language=RuntimeConfig.locale

#Moved language stuff into localize.py
    

#DEBUG=BasicConfig.getboolean('debug')
#IsMute=BasicConfig.getboolean('IsMute')
#LoadingPicture=BasicConfig.getboolean('LoadingPicture')
#StartupSound=BasicConfig.getboolean('StartupSound')
#LaunchWebGui=BasicConfig.getboolean('LaunchWebGui')
#BetaVersion=BasicConfig.getboolean('BetaVersion')

#for noworky
log.info("inmoov2.config")
log.info("ConfigType : "+str(ConfigType))
log.info("Language : "+str(Language))
