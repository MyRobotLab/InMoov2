#########################################
# i01_llm_start.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True) 

if runtime.isStarted('i01.llm'):
    if runtime.isStarted('i01.chatBot'):
        i01_chatBot.setPredicate("llm", "enabled")
        i01_chatBot.savePredicates()
    execfile("resource/InMoov2/services/L_Llm.py")    
