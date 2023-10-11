#########################################
# i01_headTracking_stop.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

i01_headTracking.disable()
if not runtime.isStarted('i01.eyeTracking'):
  i01_opencv.removeFilters()
  i01_opencv.stopCapture()
