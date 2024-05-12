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
        ## sync the eyes with the default i01.eyes
        if runtime.isStarted('i01.head') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightLR') and runtime.isStarted('i01.head.eeyeLeftUD') and runtime.isStarted('i01.head.eyeRightUD'):
            i01_head_eyeX.sync(i01_head_eyeLeftLR)
            i01_head_eyeX.sync(i01_head_eyeRightLR)
            i01_head_eyeY.sync(i01_head_eyeLeftUD)
            i01_head_eyeY.sync(i01_head_eyeRightUD)
        i01_eyeTracking.enable()
    else:
        if runtime.isStarted('i01.head') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightLR') and runtime.isStarted('i01.head.eeyeLeftUD') and runtime.isStarted('i01.head.eyeRightUD'):
            i01_head_eyeX.sync(i01_head_eyeLeftLR)
            i01_head_eyeX.sync(i01_head_eyeRightLR)
            i01_head_eyeY.sync(i01_head_eyeLeftUD)
            i01_head_eyeY.sync(i01_head_eyeRightUD)
        i01_eyeTracking.enable()

else:
    ## sync the eyes with the default i01.eyes
    if runtime.isStarted('i01.head') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightLR') and runtime.isStarted('i01.head.eeyeLeftUD') and runtime.isStarted('i01.head.eyeRightUD'):
      i01_head_eyeX.sync(i01_head_eyeLeftLR)
      i01_head_eyeX.sync(i01_head_eyeRightLR)
      i01_head_eyeY.sync(i01_head_eyeLeftUD)
      i01_head_eyeY.sync(i01_head_eyeRightUD)
    i01_eyeTracking.enable() 
