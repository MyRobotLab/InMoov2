#########################################
# i01_gpt3_start.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True) 

i01_gpt3 = runtime.start('i01.gpt3','Gpt3')
i01.warn("gpt3 needs an api key from OpenAI.com!")
i01_mouth = runtime.start('i01.mouth','LocalSpeech')
i01_ear = runtime.start('i01.ear','WebkitSpeechRecognition')

if runtime.isStarted('i01.chatBot'):
    i01_gpt3.attach('i01.mouth')
else:
    i01_gpt3.attach('i01.mouth')
    i01_ear.attach('i01.gpt3')
    i01_mouth.attach('i01.ear')
