# ##############################################################################
#            *** ROBOT MOVE THE HEAD ( ex WHILE SPEAKIN ) ***
# ##############################################################################
  
MoveHeadTimer = Runtime.start("MoveHeadTimer","Clock")

def MoveHead(timedata):
  #redefine next loop
  MoveHeadTimer.setInterval(random.randint(200,1000))
  #if i01.RobotCanMoveHeadRandom and i01.RobotCanMoveRandom and not i01.RobotIsSleeping and not i01_opencv.isCapturing():
  if i01.RobotCanMoveHeadRandom and i01.RobotCanMoveRandom and not i01.RobotIsSleeping:
    if isHeadActivated and RobotCanMoveHeadWhileSpeaking==1:
      if isOpenCvActivated:
        if not i01_opencv.isCapturing():
          i01.setHeadSpeed(random.randint(8,20),random.randint(8,20),random.randint(8,20))
          #wait servo last move
          if not i01_head.rothead.isMoving():i01_head.rothead.moveTo(random.uniform(65,115))
          if not i01_head.neck.isMoving():i01_head.neck.moveTo(random.uniform(70,110))
          #if not i01_head.rollNeck.isMoving():i01_head.rollNeck.moveTo(random.uniform(70,110))
      else:
        i01.setHeadSpeed(random.randint(8,20),random.randint(8,20),random.randint(8,20))
        #wait servo last move
        if not i01_head.rothead.isMoving():i01_head.rothead.moveTo(random.uniform(65,115))
        if not i01_head.neck.isMoving():i01_head.neck.moveTo(random.uniform(70,110))
        #if not i01_head.rollNeck.isMoving():i01_head.rollNeck.moveTo(random.uniform(70,110))
    else:
      MoveHeadTimer.stopClock()
  
#initial function
def MoveHeadStart():
  
  print "moveheadstart"
  if i01.RobotCanMoveHeadRandom and i01.RobotCanMoveRandom and not i01.RobotIsSleeping and not i01_opencv.isCapturing():
    if not isHeadActivated:MoveHeadTimer.stopClock()
    #if RobotCanMoveHeadWhileSpeaking==0:MoveHeadTimer.stopClock()
    
def MoveHeadStop():
  
  if i01.RobotCanMoveHeadRandom and i01.RobotCanMoveRandom and not i01.RobotIsSleeping and not i01_opencv.isCapturing():
    if isHeadActivated:
      i01.setHeadSpeed(25,25,25)
      i01_head.rest()
      i01.setHeadSpeed(40,40,40)
      i01_head.jaw.setSpeed(500.0)
      
    
MoveHeadTimer.addListener("pulse", python.name, "MoveHead")
MoveHeadTimer.addListener("clockStarted", python.name, "MoveHeadStart")  
MoveHeadTimer.addListener("clockStopped", python.name, "MoveHeadStop")
