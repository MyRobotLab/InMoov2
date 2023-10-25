if runtime.isStarted('i01.opencv'):
  if i01.getConfig().openCVFlipPicture==0:i01_opencv.removeFilter("Flip")
