def grabtheglass():
  #i01.startedGesture()
  i01.setHandSpeed("left", 19, 19, 100.0, 100.0, 100.0, 100.0)
  i01.setHandSpeed("right", 100.0, 19, 19, 100.0, 100.0, 36)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(22.0, 22.0)
  i01.setTorsoSpeed(100.0,43.0,100.0)
  i01.moveHead(20,68)
  i01.moveArm("left",77,85,45,15)
  i01.moveArm("right",48,91,72,20)
  i01.moveHand("left",180,138,140,164,180,50)
  if rightHandSensorStarted==1:
    global rightThumbPressure
    global rightIndexPressure
    global rightMajeurePressure
    global rightRingFingerPressure
    global rightPinkyPressure
    rightHandSensorON()
    sleep(1.5)
    rightThumbPressure=1 # Pressure range between 0-3
    rightIndexPressure=1
    rightMajeurePressure=1
    rightRingFingerPressure=1
    rightPinkyPressure=1
    i01.rightHand.moveTo(140,112,127,105,143,140)
    sleep(2)
    rightHandSensorOFF()
    i01.finishedGesture()
  else:
    i01.moveHand("right",140,112,127,105,143,140)
    i01.moveTorso(105,105,90)
    sleep(1)
    i01.finishedGesture()

