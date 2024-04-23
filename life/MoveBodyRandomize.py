# ##############################################################################
#            *** ROBOT MOVE THE BODY ***
# ##############################################################################
  
MoveBodyTimer = runtime.start("MoveBodyTimer","Clock")

def MoveBody(timedata):

  if RobotCanMoveRandom and RobotCanMoveBodyRandom and not RobotIsSleeping:
  
    #if (ScriptType=="Full" or ScriptType=="Virtual"):
      #redefine next loop
    MoveBodyTimer.setInterval(random.randint(3000,8000))
 
    if runtime.isStarted('i01.leftHand'):
      i01.setHandSpeed("left", random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25))
      if not i01_leftHand_thumb.isMoving():i01_leftHand_thumb.moveTo(random.uniform(10,160))
      if not i01_leftHand_index.isMoving():i01_leftHand_index.moveTo(random.uniform(10,60))
      if not i01_leftHand_majeure.isMoving():i01_leftHand_majeure.moveTo(random.uniform(10,60))
      if not i01_leftHand_ringFinger.isMoving():i01_leftHand_ringFinger.moveTo(random.uniform(10,60))
      if not i01_leftHand_pinky.isMoving():i01_leftHand_pinky.moveTo(random.uniform(10,60))
      if not i01_leftHand_wrist.isMoving():i01_leftHand_wrist.moveTo(random.uniform(5,40))
    if runtime.isStarted('i01.rightHand'):
      i01.setHandSpeed("right", random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25), random.randint(8,25))
      if not i01_rightHand_thumb.isMoving():i01_rightHand_thumb.moveTo(random.uniform(10,160))
      if not i01_rightHand_index.isMoving():i01_rightHand_index.moveTo(random.uniform(10,60))
      if not i01_rightHand_majeure.isMoving():i01_rightHand_majeure.moveTo(random.uniform(10,90))
      if not i01_rightHand_ringFinger.isMoving():i01_rightHand_ringFinger.moveTo(random.uniform(10,60))
      if not i01_rightHand_pinky.isMoving():i01_rightHand_pinky.moveTo(random.uniform(10,60))
      if not i01_rightHand_wrist.isMoving():i01_rightHand_wrist.moveTo(random.uniform(130,175))
    if runtime.isStarted('i01.leftArm'):
      i01.setArmSpeed("left", random.randint(2,5), random.randint(2,5), random.randint(2,5), random.randint(2,5))
      if not i01_leftArm_bicep.isMoving():i01_leftArm_bicep.moveTo(random.uniform(0,5))
      if not i01_leftArm_shoulder.isMoving():i01_leftArm_shoulder.moveTo(random.uniform(25,30))
      if not i01_leftArm_rotate.isMoving():i01_leftArm_rotate.moveTo(random.uniform(85,95))
      if not i01_leftArm_omoplate.isMoving():i01_leftArm_omoplate.moveTo(random.uniform(10,15))
    if runtime.isStarted('i01.rightArm'):
      i01.setArmSpeed("right", random.randint(2,5), random.randint(2,5), random.randint(2,5), random.randint(2,5))
      if not i01_rightArm_bicep.isMoving():i01_rightArm_bicep.moveTo(random.uniform(0,5))
      if not i01_rightArm_shoulder.isMoving():i01_rightArm_shoulder.moveTo(random.uniform(25,30))
      if not i01_rightArm_rotate.isMoving():i01_rightArm_rotate.moveTo(random.uniform(85,95))
      if not i01_rightArm_omoplate.isMoving():i01_rightArm_omoplate.moveTo(random.uniform(10,15))
    if runtime.isStarted('i01.torso'):
      i01.setTorsoSpeed(random.randint(2,5), random.randint(2,5), random.randint(2,5))
      if not i01_torso_topStom.isMoving():i01_torso_topStom.moveTo(random.uniform(85,95))
      if not i01_torso_midStom.isMoving():i01_torso_midStom.moveTo(random.uniform(88,93))

    else:
      MoveBodyTimer.stopClock()
  
#initial function
def MoveBodyStart():
  
  if RobotCanMoveRandom and RobotCanMoveBodyRandom and not RobotIsSleeping:
  
    #if (ScriptType=="Full" or ScriptType=="Virtual"):
    print "MoveBodyStart"
    #head.setAcceleration(20)
    head.enableAutoDisable(0)
    
def MoveBodyStopped():
  
  if RobotCanMoveRandom and RobotCanMoveBodyRandom and not RobotIsSleeping:
  
    #if (ScriptType=="Full" or ScriptType=="Virtual"):
    print "MoveBodyStopped"
    i01.halfSpeed()
    i01.rest()

MoveBodyTimer.addListener("pulse", python.name, "MoveBody")
MoveBodyTimer.addListener("clockStarted", python.name, "MoveBodyStart")  
MoveBodyTimer.addListener("clockStopped", python.name, "MoveBodyStopped")
print("MoveBodyRandomize.py loaded")