#########################################
# i01_llm_stop.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True) 

llm = runtime.getService('i01.chatBot')
if chatBot:
   chatBot.setPredicate("llm","")
   chatBot.savePredicates()

llm = runtime.getService('i01.llm')
if llm:
   config = llm.getConfig()
   config.system = "You are a helpful robot."
   llm.apply(config)
   llm.save()
   llm.broadcastState()
