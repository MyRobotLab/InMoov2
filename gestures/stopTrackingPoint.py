def stopTrackingPoint():
  if runtime.isStarted("i01.opencv"):
    if runtime.isStarted('i01.fsm'):
      i01_fsm.fire("stopTrack")
    i01_opencv.removeFilter("LKOpticalTrack")
    i01_head_rollNeck.setAutoDisable(True)
    i01_opencv.stopCapture()
