def juggle():
  #i01.startedGesture()
  rest()
  sleep(2)  
  i01.setHandSpeed("right", 0.99, 0.99, 0.99, 0.99, 0.99, 0.99)
  i01.setArmSpeed("right", 0.99, 0.99, 0.99, 0.99)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,70,110)
  i01.moveArm("left",5,84,30,15)
  i01.moveArm("right",40,73,66,16)
  i01.moveTorso(95,93,90)
  sleep(0.3)
  i01.moveHand("left",100,50,40,20,20,90)
  i01.moveHand("right",180,160,160,160,160,11)
  ###############################
  #1-throw right to left
  sleep(1.2)
  i01.moveArm("left",30,73,66,16)
  i01.moveArm("right",60,75,66,16)
  i01.moveHand("right",50,20,20,20,20,11)
  #left hand lift
  sleep(0.1)
  i01.setHandVelocity("left", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setHandVelocity("right", -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("left",-1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right",-1.0, -1.0, -1.0, -1.0)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,110,85)
  i01.moveArm("left",60,73,66,16)
  i01.moveArm("right",20,60,66,16)
  i01.moveHand("right",50,20,20,20,20,11)
  i01.moveTorso(95,87,90)
  sleep(0.3)
  i01.moveHand("right",50,20,20,20,20,11)
  i01.moveHand("left",180,160,160,160,160,150)
  ###############################
  #2-throw left to right
  sleep(0.3)
    #left arm goes down
  i01.moveArm("left",40,75,66,16)
  sleep(0.8)
    #left arm throws up
  i01.moveArm("right",30,73,66,16)
  i01.moveArm("left",60,75,66,16)
    #Right hand catch
  sleep(0.2)
  i01.moveHead(20,70,110)
  i01.moveArm("right",60,73,66,16)
  i01.moveArm("left",20,60,66,16)
  i01.moveHand("left",50,20,20,20,20,90)
  i01.moveTorso(95,93,90)
  sleep(0.3)
  i01.moveHand("left",50,20,20,20,20,90)
  i01.moveHand("right",150,140,140,140,140,11)
  ###############################
  #3-throw Right to left
  sleep(0.3)
    #left arm goes down
  i01.moveArm("right",40,75,66,16)
  sleep(0.8)
    #left arm throws up
  i01.moveArm("left",30,73,66,16)
  i01.moveArm("right",60,75,66,16)
    #Right hand catch
  sleep(0.2)
  i01.moveHead(20,110,110)
  i01.moveArm("left",60,73,66,16)
  i01.moveArm("right",20,60,66,16)
  i01.moveHand("right",50,20,20,20,20,11)
  i01.moveTorso(95,87,90)
  sleep(0.3)
  i01.moveHand("right",50,20,20,20,20,11)
  i01.moveHand("left",150,140,140,140,140,150)
  ###############################
  #4-throw left to right
  sleep(0.3)
    #left arm goes down
  i01.moveArm("left",40,75,66,16)
  sleep(0.8)
    #left arm throws up
  i01.moveArm("right",30,73,66,16)
  i01.moveArm("left",60,75,66,16)
    #Right hand catch
  sleep(0.2)
  i01.moveHead(20,70,110)
  i01.moveArm("right",60,73,66,16)
  i01.moveArm("left",20,60,66,16)
  i01.moveHand("left",50,20,20,20,20,90)
  i01.moveTorso(95,93,90)
  sleep(0.3)
  i01.moveHand("left",50,20,20,20,20,90)
  i01.moveHand("right",150,140,140,140,140,11)
  ###############################
  #5-throw Right to left
  sleep(0.3)
    #left arm goes down
  i01.moveArm("right",40,75,66,16)
  sleep(0.8)
    #left arm throws up
  i01.moveArm("left",30,73,66,16)
  i01.moveArm("right",60,75,66,16)
    #Right hand catch
  sleep(0.2)
  i01.moveHead(20,110,110)
  i01.moveArm("left",60,73,66,16)
  i01.moveArm("right",20,60,66,16)
  i01.moveHand("right",50,20,20,20,20,11)
  i01.moveTorso(95,87,90)
  sleep(0.3)
  i01.moveHand("right",50,20,20,20,20,11)
  i01.moveHand("left",150,140,140,140,140,150)
  ###############################
  #6-throw left to right
  sleep(0.3)
    #left arm goes down
  i01.moveArm("left",40,75,66,16)
  sleep(0.8)
    #left arm throws up
  i01.moveArm("right",30,73,66,16)
  i01.moveArm("left",60,75,66,16)
    #Right hand catch
  sleep(0.2)
  i01.moveHead(20,70,110)
  i01.moveArm("right",60,73,66,16)
  i01.moveArm("left",20,60,66,16)
  i01.moveHand("left",50,20,20,20,20,90)
  i01.moveTorso(95,93,90)
  sleep(0.3)
  i01.moveHand("left",50,20,20,20,20,90)
  i01.moveHand("right",150,140,140,140,140,11)
  ###############################
  #7-throw Right to left
  sleep(0.3)
    #left arm goes down
  i01.moveArm("right",40,75,66,16)
  sleep(0.8)
    #left arm throws up
  i01.moveArm("left",30,73,66,16)
  i01.moveArm("right",60,75,66,16)
    #Right hand catch
  sleep(0.2)
  i01.moveHead(20,110,110)
  i01.moveArm("left",60,73,66,16)
  i01.moveArm("right",20,60,66,16)
  i01.moveHand("right",50,20,20,20,20,11)
  i01.moveTorso(95,87,90)
  sleep(0.3)
  i01.moveHand("right",50,20,20,20,20,11)
  i01.moveHand("left",150,140,140,140,140,150)
  sleep(1)
  relax()
  i01.finishedGesture()