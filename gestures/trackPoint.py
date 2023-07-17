def trackPoint():
  if runtime.isStarted('i01.opencv'):
    i01_head_rollNeck.setAutoDisable(False)
    i01_head_rollNeck.moveToBlocking(90)
    i01.setHeadSpeed(500.0,500.0,500.0,500.0,500.0)
    i01_opencv.removeFilters()
    try:gui.setActiveTab("i01.opencv")
    except:pass
    i01_opencv.addFilter("LKOpticalTrack")
    tr = i01_opencv.getFilter("LKOpticalTrack")
    tr.addPoint(280, 280)
    i01_opencv.capture()
  else:
    i01.warn("i01.opencv needs to be started!")
