#########################################
# i01_audioPeak_stop.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True) 

audioFile = runtime.getService('i01.mouth.audioFile')
if audioFile:
    audioFile.removeListener('publishPeak', 'i01.head.jaw')
    audioFile.removeListener('publishPeak', 'i01.head.upperLip')
    audioFile.save()
    audioFile.broadcastState()