# ##############################################################################
#                 CHATBOT PROGRAM.AB SERVICE
# ##############################################################################

# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')
CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
isChatBotActivated=ThisServicePartConfig.getboolean('MAIN', 'isChatBotActivated')

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

if isChatBotActivated:
  #i01_chatBot=Runtime.start("i01.chatBot", "ProgramAB")
  #htmlFilter=Runtime.start("htmlFilter", "HtmlFilter")
  #i01_chatBot.addTextListener(htmlFilter)
  #htmlFilter.addListener("publishText", "i01", "speak")
  #i01_chatBot.attach(i01_ear)
  i01.startChatBot()
  #FIXME there is missing things in InMoov2 we had in InMoov
