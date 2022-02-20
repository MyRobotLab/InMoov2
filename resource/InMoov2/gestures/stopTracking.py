def stopTracking():
  if runtime.isStarted("i01.opencv"):
    if (i01_opencv.isCapturing()):
      i01_opencv.stopTracking()
      i01_head_rollNeck.setAutoDisable(True)
