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
print ("Selected config : "+str(ScriptType))

CheckFileExist(str(ScriptType)+'i01.chatBot.yml')
   
ChatBotConfig = CodecUtils.readServiceConfig(str(ScriptType)+'i01.chatBot.yml')
Language=ChatBotConfig.currentBotName

if Language=="fr-FR":
  languageError=False
  Runtime.setAllLocales(Language)
if Language=="en-US":
  languageError=False
  Runtime.setAllLocales(Language)
if Language=="es-ES":
  languageError=False
  Runtime.setAllLocales(Language)
if Language=="de-DE":
  languageError=False
  Runtime.setAllLocales(Language)
if Language=="nl-NL":
  languageError=False
  Runtime.setAllLocales(Language)
if Language=="ru-RU":
  languageError=False
  Runtime.setAllLocales(Language)
if Language=="hi-IN":
  languageError=False
  Runtime.setAllLocales(Language)
if Language=="it-IT":
  languageError=False
  Runtime.setAllLocales(Language)
if Language=="fi-FI":
  languageError=False
  Runtime.setAllLocales(Language)
if Language=="pt-PT":
  languageError=False
  Runtime.setAllLocales(Language)
if Language=="tr-TR":
  languageError=False
  Runtime.setAllLocales(Language)
if Language=="cn-ZH": 
  languageError=False
  Runtime.setAllLocales(Language)

#FIXME
if Language==None:
  languageError=True
  Runtime.setAllLocales('en-US')
    

#Debug=BasicConfig.getboolean('debug')
#IsMute=BasicConfig.getboolean('IsMute')
#LoadingPicture=BasicConfig.getboolean('LoadingPicture')
#StartupSound=BasicConfig.getboolean('StartupSound')
#LaunchWebGui=BasicConfig.getboolean('LaunchWebGui')
#BetaVersion=BasicConfig.getboolean('BetaVersion')

#for noworky
log.info("inmoov2.config")
log.info("ScriptType : "+str(ScriptType))
log.info("Language : "+str(Language))
