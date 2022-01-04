# ##############################################################################
#            *** ROBOT MOVE THE BODY ***
# ##############################################################################
  
MoveBodyTimer = Runtime.start("MoveBodyTimer","Clock")

def MoveBody(timedata):

  if i01.RobotCanMoveRandom and i01.RobotCanMoveBodyRandom and not i01.RobotIsSleeping:
  
    #if (ScriptType=="Full" or ScriptType=="Virtual"):
      #redefine next loop
    MoveBodyTimer.setInterval(random.randint(3000,8000))
 
    if isLeftHandActivated:
      i01.setHandSpeed("left", random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25))
      if not i01_leftHand.thumb.isMoving():i01_leftHand.thumb.moveTo(random.uniform(10,160))
      if not i01_leftHand.index.isMoving():i01_leftHand.index.moveTo(random.uniform(10,60))
      if not i01_leftHand.majeure.isMoving():i01_leftHand.majeure.moveTo(random.uniform(10,60))
      if not i01_leftHand.ringFinger.isMoving():i01_leftHand.ringFinger.moveTo(random.uniform(10,60))
      if not i01_leftHand.pinky.isMoving():i01_leftHand.pinky.moveTo(random.uniform(10,60))
      if not i01_leftHand.wrist.isMoving():i01_leftHand.wrist.moveTo(random.uniform(5,40))
    if isRightHandActivated:
      i01.setHandSpeed("right", random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25))
      if not i01_rightHand.thumb.isMoving():i01_rightHand.thumb.moveTo(random.uniform(10,160))
      if not i01_rightHand.index.isMoving():i01_rightHand.index.moveTo(random.uniform(10,60))
      if not i01_rightHand.majeure.isMoving():i01_rightHand.majeure.moveTo(random.uniform(10,90))
      if not i01_rightHand.ringFinger.isMoving():i01_rightHand.ringFinger.moveTo(random.uniform(10,60))
      if not i01_rightHand.pinky.isMoving():i01_rightHand.pinky.moveTo(random.uniform(10,60))
      if not i01_rightHand.wrist.isMoving():i01_rightHand.wrist.moveTo(random.uniform(130,175))
    if isLeftArmActivated:
      i01.setArmSpeed("left", random.randint(2,5), random.randint(2,5), random.randint(2,5), random.randint(2,5))
      if not i01_leftArm.bicep.isMoving():i01_leftArm.bicep.moveTo(random.uniform(0,5))
      if not i01_leftArm.shoulder.isMoving():i01_leftArm.shoulder.moveTo(random.uniform(25,30))
      if not i01_leftArm.rotate.isMoving():i01_leftArm.rotate.moveTo(random.uniform(85,95))
      if not i01_leftArm.omoplate.isMoving():i01_leftArm.omoplate.moveTo(random.uniform(10,15))
    if isRightArmActivated:
      i01.setArmSpeed("right", random.randint(2,5), random.randint(2,5), random.randint(2,5), random.randint(2,5))
      if not i01_rightArm.bicep.isMoving():i01_rightArm.bicep.moveTo(random.uniform(0,5))
      if not i01_rightArm.shoulder.isMoving():i01_rightArm.shoulder.moveTo(random.uniform(25,30))
      if not i01_rightArm.rotate.isMoving():i01_rightArm.rotate.moveTo(random.uniform(85,95))
      if not i01_rightArm.omoplate.isMoving():i01_rightArm.omoplate.moveTo(random.uniform(10,15))
    if isTorsoActivated:
      i01.setTorsoSpeed(random.randint(2,5), random.randint(2,5), random.randint(2,5))
      if not i01_torso.topStom.isMoving():i01_torso.topStom.moveTo(random.uniform(85,95))
      if not i01_torso.midStom.isMoving():i01_torso.midStom.moveTo(random.uniform(88,93))

    else:
      MoveBodyTimer.stopClock()
  
#initial function
def MoveBodyStart():
  
  if i01.RobotCanMoveRandom and i01.RobotCanMoveBodyRandom and not i01.RobotIsSleeping:
  
    #if (ScriptType=="Full" or ScriptType=="Virtual"):
    print "MoveBodyStart"
    #head.setAcceleration(20)
    head.enableAutoDisable(0)
    
def MoveBodyStopped():
  
  if i01.RobotCanMoveRandom and i01.RobotCanMoveBodyRandom and not i01.RobotIsSleeping:
  
    #if (ScriptType=="Full" or ScriptType=="Virtual"):
    print "MoveBodyStopped"
    i01.halfSpeed()
    i01.rest()

MoveBodyTimer.addListener("pulse", python.name, "MoveBody")
MoveBodyTimer.addListener("clockStarted", python.name, "MoveBodyStart")  
MoveBodyTimer.addListener("clockStopped", python.name, "MoveBodyStopped")