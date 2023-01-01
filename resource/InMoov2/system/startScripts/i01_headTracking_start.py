#########################################
# i01_headTracking_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

if runtime.isStarted('i01.opencv'):
    i01_opencv.removeFilter("FaceDetectDNN")
    i01_headTracking.enable()
else:
    i01_headTracking.enable()   