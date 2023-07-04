# ##############################################################################
#                 CONFIGPARSER FILE
# ##############################################################################

#shared parse function
def CheckFileExist(File):
  global RobotIsErrorMode
  if not os.path.isfile(File+'.config'):
    shutil.move(File+'.config.default',File+'.config')
    print "config file created : ",File+'.config'


CheckFileExist(RuningFolder+'config/' + '_InMoov')
LaunchSwingGui=True
   
BasicConfig = ConfigParser.ConfigParser(allow_no_value = True)
BasicConfig.read(RuningFolder+'config/' + '_InMoov.config')

# PARSE THE CONFIG FILE
ScriptType=BasicConfig.get('MAIN', 'ScriptType')

try:
  MyLanguage=BasicConfig.get('TTS', 'MyLanguage')
  Language=MyLanguage

except:
  pass
  
try:
  Language=BasicConfig.get('MAIN', 'Language')
except:
  pass

              
if Language=="fr-FR" or Language=="en-US" or Language=="nl-NL" or Language=="es-ES" or Language=="de-DE" or Language=="ru-RU" or Language=="hi-IN" or Language=="it-IT" or Language=="fi-FI" or Language=="pt-PT" or Language=="tr-TR" or Language=="cn-ZH":
  global LanguageError
  languageError=False
  print("language in configs: "+str(Language))
  Runtime.setAllLocales(Language)
else:
  languageError=True
 
    

DEBUG=BasicConfig.getboolean('MAIN', 'debug')
IsMute=BasicConfig.getboolean('VOCAL', 'IsMute')
LoadingPicture=BasicConfig.getboolean('GENERAL', 'LoadingPicture')
StartupSound=BasicConfig.getboolean('GENERAL', 'StartupSound')
IuseLinux=BasicConfig.getboolean('GENERAL', 'IuseLinux')
LaunchSwingGui=BasicConfig.getboolean('GENERAL', 'LaunchSwingGui')
BetaVersion=BasicConfig.getboolean('GENERAL', 'BetaVersion')

#for noworky
log.info("_inmoov.config")
log.info("ScriptType : "+str(ScriptType))
log.info("Language : "+str(Language))
