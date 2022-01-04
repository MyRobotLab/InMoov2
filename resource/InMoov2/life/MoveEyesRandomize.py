# ##############################################################################
#            *** ROBOT MOVE THE EYES ( ex WHILE SPEAKIN ) ***
# ##############################################################################
  
MoveEyesTimer = Runtime.start("MoveEyesTimer","Clock")

def MoveEyes(timedata):
  #redefine next loop
  MoveEyesTimer.setInterval(random.randint(500,2000))
  #if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsSleeping and not i01_opencv.isCapturing():
  if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsSleeping:
    if isHeadActivated:
      if isOpenCvActivated:
        if not i01_opencv.isCapturing():
          i01_head.eyeX.setSpeed(random.randint(30,110))
          i01_head.eyeY.setSpeed(random.randint(30,110))
          #wait servo last move
          if not i01_head.eyeX.isMoving():i01_head.eyeX.moveTo(random.uniform(20,160))
          if not i01_head.eyeY.isMoving():i01_head.eyeY.moveTo(random.uniform(20,160))
      else:    
        i01_head.eyeX.setSpeed(random.randint(30,110))
        i01_head.eyeY.setSpeed(random.randint(30,110))
        #wait servo last move
        if not i01_head.eyeX.isMoving():i01_head.eyeX.moveTo(random.uniform(20,160))
        if not i01_head.eyeY.isMoving():i01_head.eyeY.moveTo(random.uniform(20,160))
    else:
      MoveEyesTimer.stopClock()

#initial function
def MoveEyesStart():
  if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsSleeping and not i01_opencv.isCapturing():
    if not isHeadActivated:MoveEyesTimer.stopClock()
    
def MoveEyesStop():
  
  if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsSleeping and not i01_opencv.isCapturing():
    if isHeadActivated:
      i01_head.eyeX.rest()
      i01_head.eyeY.rest()
    
MoveEyesTimer.addListener("pulse", python.name, "MoveEyes")
MoveEyesTimer.addListener("clockStarted", python.name, "MoveEyesStart")  
MoveEyesTimer.addListener("clockStopped", python.name, "MoveEyesStop")