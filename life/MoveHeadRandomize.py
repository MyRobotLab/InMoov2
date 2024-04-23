# ##############################################################################
#            *** ROBOT MOVE THE HEAD ( ex WHILE SPEAKIN ) ***
# ##############################################################################
  
MoveHeadTimer = runtime.start("MoveHeadTimer","Clock")

def MoveHead(timedata):
  #redefine next loop
  MoveHeadTimer.setInterval(random.randint(200,1000))
  #if i01.RobotCanMoveHeadRandom and i01.RobotCanMoveRandom and not i01.RobotIsSleeping and not i01_opencv.isCapturing():
  if RobotCanMoveHeadRandom and RobotCanMoveRandom and not RobotIsSleeping:
    if runtime.isStarted('i01.head') and RobotCanMoveHeadWhileSpeaking==1:
      if runtime.isStarted('i01.opencv'):
        if not i01_opencv.isCapturing():
          i01.setHeadSpeed(random.randint(8,20),random.randint(8,20),random.randint(8,20))
          #wait servo last move
          if not i01_head_rothead.isMoving():i01_head_rothead.moveTo(random.uniform(65,115))
          if not i01_head_neck.isMoving():i01_head_neck.moveTo(random.uniform(70,110))
          #if not i01_head.rollNeck.isMoving():i01_head.rollNeck.moveTo(random.uniform(70,110))
      else:
        i01.setHeadSpeed(random.randint(8,20),random.randint(8,20),random.randint(8,20))
        #wait servo last move
        if not i01_head_rothead.isMoving():i01_head_rothead.moveTo(random.uniform(65,115))
        if not i01_head_neck.isMoving():i01_head_neck.moveTo(random.uniform(70,110))
        #if not i01_head.rollNeck.isMoving():i01_head.rollNeck.moveTo(random.uniform(70,110))
    else:
      MoveHeadTimer.stopClock()
  
#initial function
def MoveHeadStart():
  
  print("moveheadstart")
  if RobotCanMoveHeadRandom and RobotCanMoveRandom and not RobotIsSleeping and not i01_opencv.isCapturing():
    if not runtime.isStarted('i01.head'):MoveHeadTimer.stopClock()
    #if RobotCanMoveHeadWhileSpeaking==0:MoveHeadTimer.stopClock()
    
def MoveHeadStop():
  
  if RobotCanMoveHeadRandom and RobotCanMoveRandom and not RobotIsSleeping and not i01_opencv.isCapturing():
    if runtime.isStarted('i01.head'):
      i01.setHeadSpeed(25,25,25)
      i01_head.rest()
      i01.setHeadSpeed(40,40,40)
      i01_head_jaw.setSpeed(500.0)
      
    
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStarted", python.name, "MoveHeadStart")  
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStop")
print("MoveHeadRandomize.py loaded")