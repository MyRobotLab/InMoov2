def trackHumans():
  if runtime.isStarted('i01.opencv'):
    if runtime.isStarted('i01.fsm'):
      i01_fsm.fire("track")
    if runtime.isStarted('i01.head'):  
      i01_head_rollNeck.setAutoDisable(False)
      i01_head_rollNeck.enable()
      i01_head_rollNeck.moveTo(90)
      i01.setHeadSpeed(500.0,500.0,500.0,500.0,500.0)
    i01_opencv.removeFilters()
    i01.startPeer("headTracking")
    #i01.startPeer("eyeTracking")
    sleep(2)
    if runtime.isStarted('i01.headTracking'):
      i01_headTracking.enable()
    if runtime.isStarted('i01.eyeTracking'):
      i01_eyeTracking.enable()  
  else:
    i01.warn("i01.opencv needs to be started to start tracking!")

#def trackHumans(noFaceRecognizerOverride=True):
