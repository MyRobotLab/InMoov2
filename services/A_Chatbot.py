# ##############################################################################
#                 CHATBOT PROGRAM.AB SERVICE
# ##############################################################################

# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
def initChatBot():
  i01_chatBot.getConfig()

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

if runtime.isStarted('i01.chatBot'):
  initChatBot()
    # This is also done via the welcomeMessage()
  if str(i01_chatBot.getPredicate("human","firstinit"))=="unknown" or str(i01_chatBot.getPredicate("human","firstinit"))=="started":
    i01_chatBot.setPredicate("human","topic","default")
    i01_chatBot.getResponse("FIRST_INIT")
  else:
    i01_chatBot.startSession(str(i01_chatBot.getPredicate("human","lastUsername")))
    i01_chatBot.getResponse("WAKE_UP")
