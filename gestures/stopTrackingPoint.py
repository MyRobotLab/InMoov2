def stopTrackingPoint():
  if runtime.isStarted("i01.opencv"):
    i01_opencv.removeFilter("LKOpticalTrack")
    i01_head_rollNeck.setAutoDisable(True)
    i01_opencv.stopCapture()
