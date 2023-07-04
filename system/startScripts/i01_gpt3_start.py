#########################################
# i01_gpt3_start.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True) 

i01.startPeer('gpt3')
i01.warn("gpt3 needs an api key from OpenAI.com!")
if runtime.isStarted('i01.gpt3'):
    if runtime.isStarted('i01.chatBot'):
        i01_chatBot.setPredicate("gpt3", "enabled")
        i01_chatBot.savePredicates()
        if runtime.isStarted('i01.mouth'):
            i01_gpt3.attach('i01.mouth')
        else:
            i01.startPeer('mouth')
            i01_gpt3.attach('i01.mouth')  
    else:
        i01.startPeer('mouth')
        i01.startPeer('ear')
        i01_gpt3.attach('i01.mouth')
        i01_ear.attach('i01.gpt3')
