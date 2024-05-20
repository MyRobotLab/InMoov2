#########################################
# i01_gpt3_start.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True) 

if runtime.isStarted('i01.gpt3'):
    if runtime.isStarted('i01.chatBot'):
        i01_chatBot.setPredicate("gpt3", "enabled")
        i01_chatBot.savePredicates()
