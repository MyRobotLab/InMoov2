def trackPoint():
  i01.cameraOn()
  i01.trackPoint()
  try:gui.setActiveTab("i01.opencv")
  except:pass
  i01_head_rollNeck.setAutoDisable(False)
  i01_head_rollNeck.moveToBlocking(90)
  i01.setHeadSpeed(100.0,100.0,100.0,100.0,100.0)
  #i01.headPid.setPID("x",12,5,0.1)
  #i01.headPid.setPID("y",12,5,0.1)