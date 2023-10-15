def CloseBothHandSlow():
  #i01.startedGesture() 
  rest()
  sleep(2)
  ###############################
  #reference movements:
  #https://youtu.be/kCt1bmSASCI
  ############################### 
  #1-set in position for oranges
  sleep(1.2)
  i01.setHandVelocity("left", 60, 60, 60, 60, 60, 60)
  i01.setHandVelocity("right", 60, 60, 60, 60, 60, 60)
  i01.setArmVelocity("left",-1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right",-1.0, -1.0, -1.0, -1.0)
  i01.moveArm("left",60,75,66,16)
  i01.moveArm("right",60,75,66,16)
  i01.moveHand("right",50,20,20,20,20,11)
  i01.moveHand("left",50,20,20,20,20,150)
  ###############################
  #close both hands
  sleep(3)
  i01.setArmVelocity("left",-1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right",-1.0, -1.0, -1.0, -1.0)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,110,85)
  i01.moveArm("left",60,55,66,16)
  i01.moveArm("right",60,55,66,16)
  i01.moveTorso(95,87,90)
  sleep(0.3)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveHand("left",180,130,120,140,160,150)
  ###############################
  i01.finishedGesture()