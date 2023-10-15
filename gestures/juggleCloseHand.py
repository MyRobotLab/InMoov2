def juggleCloseHand():
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
  sleep(1)
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
  #move right and away and catch
  sleep(5)
  i01.setHandVelocity("left", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setHandVelocity("right", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.moveArm("right",70,100,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  ###############################
  #move right down with ball
  sleep(0.6)
  i01.moveArm("right",20,100,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  ###############################
  #move right to inside with ball
  sleep(0.6)
  i01.moveArm("right",20,60,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  i01.moveArm("left",50,80,55,16)
  i01.moveHand("left",180,130,120,140,160,150)
  ###############################
  #move right up inside and throw ball
  sleep(0.6)
  i01.moveArm("right",70,60,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  i01.moveArm("left",40,100,45,16)
  i01.moveHand("left",180,130,120,140,160,150)

  ###############################
  #right hand lift
  sleep(0.2)
  i01.setHandVelocity("right", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setHandVelocity("left", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right",-1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("left",-1.0, -1.0, -1.0, -1.0)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,80,85)
  i01.moveArm("right",45,73,66,16)
  i01.moveArm("left",60,55,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,87,90)
  sleep(0.4)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveHand("right",180,130,120,140,160,11)
  ###############################
  #move left and away and catch
  sleep(0.3)
  i01.moveArm("left",70,100,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  ###############################
  #move left down with ball
  sleep(0.6)
  i01.moveArm("left",20,100,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  ###############################
  #move left to inside with ball
  sleep(0.6)
  i01.moveArm("left",20,60,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  i01.moveArm("right",50,80,55,16)
  i01.moveHand("right",180,130,120,140,160,11)
  ###############################
  #move left up inside and throw ball
  sleep(0.6)
  i01.moveArm("left",70,60,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  i01.moveArm("right",40,100,45,16)


  ###############################
  #left hand lift
  sleep(0.1)
  i01.setHandVelocity("left", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setHandVelocity("right", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("left",-1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right",-1.0, -1.0, -1.0, -1.0)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,110,85)
  i01.moveArm("left",45,73,66,16)
  i01.moveArm("right",60,55,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,87,90)
  sleep(0.3)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveHand("left",180,130,120,140,160,150)
  ###############################
  #move right and away and catch
  sleep(0.2)
  i01.moveArm("right",70,100,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  ###############################
  #move right down with ball
  sleep(0.6)
  i01.moveArm("right",20,100,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  ###############################
  #move right to inside with ball
  sleep(0.6)
  i01.moveArm("right",20,60,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  i01.moveArm("left",50,80,55,16)
  i01.moveHand("left",180,130,120,140,160,150)
  ###############################
  #move right up inside and throw ball
  sleep(0.6)
  i01.moveArm("right",70,60,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  i01.moveArm("left",40,100,45,16)
  i01.moveHand("left",180,130,120,140,160,150)

  ###############################
  #right hand lift
  sleep(0.2)
  i01.setHandVelocity("right", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setHandVelocity("left", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right",-1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("left",-1.0, -1.0, -1.0, -1.0)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,80,85)
  i01.moveArm("right",45,73,66,16)
  i01.moveArm("left",60,55,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,87,90)
  sleep(0.4)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveHand("right",180,130,120,140,160,11)
  ###############################
  #move left and away and catch
  sleep(0.3)
  i01.moveArm("left",70,100,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  ###############################
  #move left down with ball
  sleep(0.6)
  i01.moveArm("left",20,100,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  ###############################
  #move left to inside with ball
  sleep(0.6)
  i01.moveArm("left",20,60,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  i01.moveArm("right",50,80,55,16)
  i01.moveHand("right",180,130,120,140,160,11)
  ###############################
  #move left up inside and throw ball
  sleep(0.6)
  i01.moveArm("left",70,60,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  i01.moveArm("right",40,100,45,16)


  ###############################
  #left hand lift
  sleep(0.1)
  i01.setHandVelocity("left", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setHandVelocity("right", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("left",-1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right",-1.0, -1.0, -1.0, -1.0)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,110,85)
  i01.moveArm("left",45,73,66,16)
  i01.moveArm("right",60,55,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,87,90)
  sleep(0.3)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveHand("left",180,130,120,140,160,150)
  ###############################
  #move right and away and catch
  sleep(0.2)
  i01.moveArm("right",70,100,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  ###############################
  #move right down with ball
  sleep(0.6)
  i01.moveArm("right",20,100,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  ###############################
  #move right to inside with ball
  sleep(0.6)
  i01.moveArm("right",20,60,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  i01.moveArm("left",50,80,55,16)
  i01.moveHand("left",180,130,120,140,160,150)
  ###############################
  #move right up inside and throw ball
  sleep(0.6)
  i01.moveArm("right",70,60,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  i01.moveArm("left",40,100,45,16)
  i01.moveHand("left",180,130,120,140,160,150)

  ###############################
  #right hand lift
  sleep(0.2)
  i01.setHandVelocity("right", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setHandVelocity("left", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right",-1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("left",-1.0, -1.0, -1.0, -1.0)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,80,85)
  i01.moveArm("right",45,73,66,16)
  i01.moveArm("left",60,55,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,87,90)
  sleep(0.4)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveHand("right",180,130,120,140,160,11)
  ###############################
  #move left and away and catch
  sleep(0.3)
  i01.moveArm("left",70,100,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  ###############################
  #move left down with ball
  sleep(0.6)
  i01.moveArm("left",20,100,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  ###############################
  #move left to inside with ball
  sleep(0.6)
  i01.moveArm("left",20,60,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  i01.moveArm("right",50,80,55,16)
  i01.moveHand("right",180,130,120,140,160,11)
  ###############################
  #move left up inside and throw ball
  sleep(0.6)
  i01.moveArm("left",70,60,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  i01.moveArm("right",40,100,45,16)


  ###############################
  #left hand lift
  sleep(0.1)
  i01.setHandVelocity("left", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setHandVelocity("right", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("left",-1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right",-1.0, -1.0, -1.0, -1.0)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,110,85)
  i01.moveArm("left",45,73,66,16)
  i01.moveArm("right",60,55,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,87,90)
  sleep(0.3)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveHand("left",180,130,120,140,160,150)
  ###############################
  #move right and away and catch
  sleep(0.2)
  i01.moveArm("right",70,100,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  ###############################
  #move right down with ball
  sleep(0.6)
  i01.moveArm("right",20,100,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  ###############################
  #move right to inside with ball
  sleep(0.6)
  i01.moveArm("right",20,60,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  i01.moveArm("left",50,80,55,16)
  i01.moveHand("left",180,130,120,140,160,150)
  ###############################
  #move right up inside and throw ball
  sleep(0.6)
  i01.moveArm("right",70,60,66,16)
  i01.moveHand("right",180,130,120,140,160,11)
  i01.moveTorso(95,90,90)
  i01.moveArm("left",40,100,45,16)
  i01.moveHand("left",180,130,120,140,160,150)

  ###############################
  #right hand lift
  sleep(0.2)
  i01.setHandVelocity("right", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setHandVelocity("left", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right",-1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("left",-1.0, -1.0, -1.0, -1.0)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,80,85)
  i01.moveArm("right",45,73,66,16)
  i01.moveArm("left",60,55,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,87,90)
  sleep(0.4)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveHand("right",180,130,120,140,160,11)
  ###############################
  #move left and away and catch
  sleep(0.3)
  i01.moveArm("left",70,100,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  ###############################
  #move left down with ball
  sleep(0.6)
  i01.moveArm("left",20,100,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  ###############################
  #move left to inside with ball
  sleep(0.6)
  i01.moveArm("left",20,60,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  i01.moveArm("right",50,80,55,16)
  i01.moveHand("right",180,130,120,140,160,11)
  ###############################
  #move left up inside and throw ball
  sleep(0.6)
  i01.moveArm("left",70,60,66,16)
  i01.moveHand("left",180,130,120,140,160,150)
  i01.moveTorso(95,90,90)
  i01.moveArm("right",40,100,45,16)
  sleep(0.5) 
  i01.finishedGesture()