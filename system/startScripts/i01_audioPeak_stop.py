#########################################
# i01_audioPeak_stop.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True) 

audioFile = runtime.getService('i01.mouth.audioFile')
if audioFile:
    config = audioFile.getConfig()
    audioFile.removeListener('publishPeak', 'i01.head.jaw', 'moveTo')
    audioFile.removeListener('publishPeak', 'i01.head.upperLip', 'moveTo')
    audioFile.save()
    audioFile.apply(config)
    audioFile.broadcastState()
