#########################################
# i01_eyeTracking_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

if runtime.isStarted('i01.opencv'):
    if not runtime.isStarted('i01.headTracking'):
        i01_opencv.removeFilters()
        i01_eyeTracking.enable()
    else:i01_eyeTracking.enable()
else:
    i01_eyeTracking.enable()
