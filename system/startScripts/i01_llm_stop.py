#########################################
# i01_llm_stop.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True) 

if runtime.isStarted('i01.chatBot'):
   i01_chatBot.setPredicate("llm","")
   i01_chatBot.savePredicates()
