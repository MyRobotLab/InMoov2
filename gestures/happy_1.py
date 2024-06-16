def happy_1():
  #i01.startedGesture()
  if runtime.isStarted('i01.head'):
    i01.setHeadSpeed(22.0, 22.0)
    i01.moveHead(84,88)
  if runtime.isStarted('i01.leftArm'):  
    i01.moveArm("left",5,82,36,10)
    i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  if runtime.isStarted('i01.rightArm'):  
    i01.setArmSpeed("right", 43.0, 43.0, 43.0, 100.0)
    i01.moveArm("right",74,112,61,29)
  if runtime.isStarted('i01.leftHand'):
    i01.setHandSpeed("left", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
    i01.moveHand("left",0,88,135,94,96,90)
  if runtime.isStarted('i01.rightHand'):  
    i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
    i01.moveHand("right",81,79,118,47,0,90)
  sleep(5)
  i01.finishedGesture()
  rest()
