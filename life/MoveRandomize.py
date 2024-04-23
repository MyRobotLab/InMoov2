# ##############################################################################
#            *** WHOLE ROBOT MOVE RANDOM ***
# ##############################################################################
  
MoveRandomTimer = runtime.start("MoveRandomTimer","Clock")

def MoveRandom(timedata):

  MoveRandomTimer.setInterval(random.randint(10000,30000))

  if random.randint(0,1)==1:
    if RobotCanMoveEyesRandom:RobotCanMoveEyesRandom=False
    else:
      RobotCanMoveEyesRandom=True
      if not MoveEyesTimer.isClockRunning:MoveEyesTimer.startClock()
    
  if random.randint(0,1)==1:
    if RobotCanMoveBodyRandom:
      RobotCanMoveBodyRandom=False
      RobotCanMoveHeadRandom=False
    else:
      RobotCanMoveBodyRandom=True
      RobotCanMoveHeadRandom=True
      if not MoveBodyTimer.isClockRunning:MoveBodyTimer.startClock()
      if not MoveHeadTimer.isClockRunning:MoveHeadTimer.startClock()

      
  #little pause
  if random.randint(0,4)==4:
    if RobotCanMoveRandom and not RobotIsSleeping:
      if runtime.isStarted('i01.opencv'):
        if not i01_opencv.isCapturing():
          RobotCanMoveHeadRandom=False
          RobotCanMoveBodyRandom=False
          relax()
          i01.waitTargetPos()
      else:
        RobotCanMoveHeadRandom=False
        RobotCanMoveBodyRandom=False
        relax()
        i01.waitTargetPos()
      
  if random.randint(0,3)==3:RobotCanMoveEyesRandom=False

def MoveRandomStart():
  MoveBodyTimer.startClock()
  MoveEyesTimer.startClock()
  MoveHeadTimer.startClock()
    
def MoveRandomStop():
  MoveBodyTimer.stopClock()
  MoveEyesTimer.stopClock()
  MoveHeadTimer.stopClock()
  RobotCanMoveHeadRandom=True
  RobotCanMoveBodyRandom=True
  RobotCanMoveEyesRandom=True
  relax()
  i01.waitTargetPos()    
    
MoveRandomTimer.addListener("pulse", python.name, "MoveRandom")
MoveRandomTimer.addListener("clockStopped", python.name, "MoveRandomStop")
MoveRandomTimer.addListener("clockStarted", python.name, "MoveRandomStart")

print("MoveRandomize.py loaded")