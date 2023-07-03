if runtime.isStarted('i01.chatBot'):
  i01_chatBot.getResponse("NEW_INIT_USER")
else:runtime.warn('chatBot needs to be started')
