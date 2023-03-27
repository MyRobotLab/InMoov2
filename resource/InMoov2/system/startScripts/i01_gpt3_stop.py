#########################################
# i01_gpt3_stop.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True) 

# release service gpt3
Runtime.releaseService("i01.gpt3")
Runtime.releaseService("i01.gpt3.http")
if runtime.isStarted('i01.chatBot'):
   #i01_chatBot.getResponse("STOPPINGGPT3")
   i01_chatBot.setPredicate("gpt3","")
   i01_chatBot.savePredicates()
