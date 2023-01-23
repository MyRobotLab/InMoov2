def trackHumans():
  if runtime.isStarted('i01.opencv'):
    i01_head_rollNeck.setAutoDisable(False)
    i01_head_rollNeck.moveToBlocking(90)
    i01.setHeadSpeed(500.0,500.0,500.0,500.0,500.0)
    i01_opencv.removeFilters()
    i01.getHeadTracking()
    i01.startPeer("headTracking")
    i01_headTracking.enable()
  else:
    i01.warn("i01.opencv needs to be started to start tracking!")

#def trackHumans(noFaceRecognizerOverride=True):
