def unhappy():
  if runtime.isStarted('i01.neoPixel'):
    i01_neoPixel.setAnimation("Color Wipe", 20, 0, 0, 50)
    sleep(2)
  #i01.startedGesture()
  i01.setHandSpeed("left", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setTorsoSpeed(100.0, 100.0, 100.0)
  i01.moveHead(85,40)
  i01.moveArm("left",79,42,23,41)
  i01.moveArm("right",71,40,14,39)
  i01.moveHand("left",180,180,180,180,180,47)
  i01.moveHand("right",99,130,152,154,145,180)
  i01.moveTorso(90,90,90)
  i01.finishedGesture()

