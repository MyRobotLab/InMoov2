#########################################
# i01_audioPeak_start.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True) 

audioFile = runtime.getService('i01.mouth.audioFile')
if audioFile:
    config = audioFile.getConfig()
    if runtime.isStarted('i01.head.jaw'):
        i01_head_jaw.subscribe(audioFile.getName(), "publishPeak", "moveTo")
    if runtime.isStarted('i01.head.upperLip'):
        i01_head_upperLip.subscribe(audioFile.getName(), "publishPeak", "moveTo")
    audioFile.apply(config)
    audioFile.save()
    audioFile.broadcastState()
    if runtime.isStarted('i01.mouthControl'):
        runtime.release('i01.mouthControl')