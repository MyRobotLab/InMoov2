def stopTrackHumans():
  if runtime.isStarted("i01.opencv"):
    if runtime.isStarted('i01.fsm'):
      i01_fsm.fire("stopTrack")
    if runtime.isStarted("i01.headTracking"):
      i01_headTracking.disable()
    if runtime.isStarted("i01.eyeTracking"):
      i01_eyeTracking.disable()
    if runtime.isStarted("i01.head"):
      i01_head_rollNeck.disable()
      i01_head_rollNeck.setAutoDisable(True)
    i01_opencv.removeFilters()
    i01_opencv.stopCapture()
    i01.finishedGesture()
