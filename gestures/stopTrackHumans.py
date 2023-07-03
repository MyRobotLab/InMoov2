def stopTrackHumans():
  if runtime.isStarted("i01.opencv"):
    if (i01_opencv.isCapturing()):
      i01_headTracking.disable()
      i01_head_rollNeck.setAutoDisable(True)
