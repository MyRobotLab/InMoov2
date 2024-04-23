# ##############################################################################
#            *** ROBOT MOVE THE EYES ( ex WHILE SPEAKIN ) ***
# ##############################################################################
  
MoveEyesTimer = runtime.start("MoveEyesTimer","Clock")

def MoveEyes(timedata):
  #redefine next loop
  MoveEyesTimer.setInterval(random.randint(500,2000))
  #if i01.RobotCanMoveEyesRandom and i01.RobotCanMoveRandom and not i01.RobotIsSleeping and not i01_opencv.isCapturing():
  if RobotCanMoveEyesRandom and RobotCanMoveRandom and not RobotIsSleeping:
    if runtime.isStarted('i01.head'):
      if runtime.isStarted('i01.opencv'):
        if not i01_opencv.isCapturing():
          i01_head_eyeX.setSpeed(random.randint(30,110))
          i01_head_eyeY.setSpeed(random.randint(30,110))
          #wait servo last move
          if not i01_head_eyeX.isMoving():i01_head_eyeX.moveTo(random.uniform(20,160))
          if not i01_head_eyeY.isMoving():i01_head_eyeY.moveTo(random.uniform(20,160))
      else:    
        i01_head_eyeX.setSpeed(random.randint(30,110))
        i01_head_eyeY.setSpeed(random.randint(30,110))
        #wait servo last move
        if not i01_head_eyeX.isMoving():i01_head_eyeX.moveTo(random.uniform(20,160))
        if not i01_head_eyeY.isMoving():i01_head_eyeY.moveTo(random.uniform(20,160))
    else:
      MoveEyesTimer.stopClock()

#initial function
def MoveEyesStart():
  if RobotCanMoveEyesRandom and RobotCanMoveRandom and not RobotIsSleeping and not i01_opencv.isCapturing():
    if not runtime.isStarted('i01.head'):MoveEyesTimer.stopClock()
    
def MoveEyesStop():
  
  if RobotCanMoveEyesRandom and RobotCanMoveRandom and not RobotIsSleeping and not i01_opencv.isCapturing():
    if runtime.isStarted('i01.head'):
      i01_head_eyeX.rest()
      i01_head_eyeY.rest()
    
MoveEyesTimer.addListener("pulse", python.name, "MoveEyes")
MoveEyesTimer.addListener("clockStarted", python.name, "MoveEyesStart")  
MoveEyesTimer.addListener("clockStopped", python.name, "MoveEyesStop")
print("MoveEyesRandomize.py loaded")