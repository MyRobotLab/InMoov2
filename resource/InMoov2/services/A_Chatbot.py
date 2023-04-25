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
    # This launch the chatbot for the first initialization
  if str(i01_chatBot.getPredicate("Human","firstinit"))=="unknown" or str(i01_chatBot.getPredicate("Human","firstinit"))=="started":
    i01_chatBot.setPredicate("default","topic","default")
    i01_chatBot.getResponse("FIRST_INIT")
  else:
    i01_chatBot.getResponse("WAKE_UP")
