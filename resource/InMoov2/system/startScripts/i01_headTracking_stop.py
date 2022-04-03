#########################################
# i01_headTracking_stop.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

# create a pid
i01_opencv.removeFilter("FaceDetectDNN")
runtime.release("i01.pid")
runtime.release("i01.headTracking")
