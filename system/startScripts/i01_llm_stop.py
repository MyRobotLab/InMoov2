#########################################
# i01_llm_stop.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True) 

chatBot = runtime.getService('i01.chatBot')
if chatBot:
   chatBot.setPredicate("llm","")
   chatBot.savePredicates()

llm = runtime.getService('i01.llm')
htmlFilter = runtime.getService('i01.htmlFilter')
if llm:
   config = llm.getConfig()
   config.system = "You are a helpful robot."
   if htmlFilter:
      htmlFilter.subscribe(llm.getName(), "publishText", "onText")
   llm.removeListener('publishText', 'python', 'onFilterText')   
   llm.save()
   llm.apply(config)
   llm.broadcastState()
