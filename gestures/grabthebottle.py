def grabthebottle():
  #i01.startedGesture()
  i01.setHandSpeed("left", 100.0, 36, 36, 36, 100.0, 36)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(50, 36)
  i01.setTorsoSpeed(100.0,36,100.0)
  i01.moveHead(20,107)
  i01.moveArm("left",77,85,45,20)
  i01.moveArm("right",5,90,30,10)
  if leftHandSensorStarted==1:
    global leftThumbPressure
    global leftIndexPressure
    global leftMajeurePressure
    global leftRingFingerPressure
    global leftPinkyPressure
    leftHandSensorON()
    sleep(1.5)
    leftThumbPressure=1 # Pressure range between 0-3
    leftIndexPressure=1
    leftMajeurePressure=1
    leftRingFingerPressure=1
    leftPinkyPressure=1
    i01.leftHand.moveTo(180,138,140,164,180,60)
    sleep(2)
    leftHandSensorOFF()
    i01.finishedGesture()
  else:
    i01.moveHand("left",180,138,140,164,180,60)
    i01.moveHand("right",0,0,0,0,0,90)
    i01.moveTorso(90,84,90)
    sleep(1)
    i01.finishedGesture()

