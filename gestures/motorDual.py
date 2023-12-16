def motorDual():
  if runtime.isStarted('i01.motorRight') and runtime.isStarted('i01.motorLeft'):
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.getResponse("MOTOR_READY")
  else:
    i01_motorRight = runtime.start("i01.motorRight","MotorDualPwm")
    i01_motorLeft = runtime.start("i01.motorLeft","MotorDualPwm")
    i01_motorRight.getConfig()
    i01_motorLeft.getConfig()
    i01_chatBot.getResponse("MOTOR_READY")

# def motorsOn():
# def motorsOff():

def motorsForward():
  if runtime.isStarted('i01.motorRight') and runtime.isStarted('i01.motorLeft'):
    i01_motorRight.unlock()
    i01_motorLeft.unlock()
    i01_motorRight.move(0.5)
    i01_motorLeft.move(0.5)
  else:i01_chatBot.getResponse("MOTOR_NOT_READY")

def motorsBackward():
  if runtime.isStarted('i01.motorRight') and runtime.isStarted('i01.motorLeft'):
    i01_motorRight.unlock()
    i01_motorLeft.unlock()
    i01_motorRight.move(-0.5)
    i01_motorLeft.move(-0.5)
  else:i01_chatBot.getResponse("MOTOR_NOT_READY")

def motorsStop():
  if runtime.isStarted('i01.motorRight') and runtime.isStarted('i01.motorLeft'):
    i01_motorRight.stopAndLock()
    i01_motorLeft.stopAndLock()
  else:i01_chatBot.getResponse("MOTOR_NOT_READY")

def motorsTurnLeft():
  if runtime.isStarted('i01.motorRight') and runtime.isStarted('i01.motorLeft'):
    i01_motorRight.unlock()
    i01_motorRight.move(0.5)
    sleep(5)
  else:i01_chatBot.getResponse("MOTOR_NOT_READY")

def motorsTurnRight():
  if runtime.isStarted('i01.motorRight') and runtime.isStarted('i01.motorLeft'):
    i01_motorLeft.unlock()
    i01_motorLeft.move(-0.5)
    sleep(5)
  else:i01_chatBot.getResponse("MOTOR_NOT_READY")

# def motorsSlowDown():
#   if runtime.isStarted('i01.motorRight') and runtime.isStarted('i01.motorLeft'):
  #   i01_motorRight.setSpeed(-10)
  #   i01_motorLeft.setSpeed(-10)
#   else:i01_chatBot.getResponse("MOTOR_NOT_READY")
# def motorsSpeedUp():
#   if runtime.isStarted('i01.motorRight') and runtime.isStarted('i01.motorLeft'):
  #   i01_motorRight.setSpeed(+10)
  #   i01_motorLeft.setSpeed(+10)
#   else:i01_chatBot.getResponse("MOTOR_NOT_READY")