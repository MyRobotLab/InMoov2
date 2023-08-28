#########################################
# i01_gpt3_stop.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True) 

# release service gpt3
i01.releasePeer('gpt3')
if runtime.isStarted('i01.chatBot'):
   #i01_chatBot.getResponse("SYSTEM_EVENT STOPPED GPT3")
   i01_chatBot.setPredicate("gpt3","")
   i01_chatBot.savePredicates()
