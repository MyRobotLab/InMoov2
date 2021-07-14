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
  i01_chatBot=Runtime.start("i01.chatBot", "ProgramAB")
  #htmlFilter=Runtime.start("htmlFilter", "HtmlFilter")
  #i01_chatBot.addTextListener(htmlFilter)
  #htmlFilter.addListener("publishText", "i01", "speak")
  #i01_chatBot.attach(i01_ear)
  i01.startChatBot()
  #isChatBotActivated=True

  # This launch the chatbot for the first initialization
#if str(i01_chatBot.getPredicate("Friend","firstinit"))=="unknown" or str(i01_chatBot.getPredicate("Friend","firstinit"))=="started":
  #i01_chatBot.setPredicate("default","topic","default")
  #i01_chatBot.getResponse("FIRST_INIT")
#else:
  #i01_chatBot.getResponse("WAKE_UP")
