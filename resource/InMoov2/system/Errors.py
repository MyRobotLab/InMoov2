# -- coding: utf-8 --
# ##############################################################################
# ERRORS FILE
# ##############################################################################

def errorSpokenFunc(errorType,param=""):
  global RobotIsErrorMode 
  RobotIsErrorMode=1
  if runtime.isStarted('i01.mouth'):
    i01_mouth.speakBlocking(i01.localize(errorType)+str(param))
  if error_red==1:
      if runtime.isStarted('i01.neopixel'):
        i01.setNeopixelAnimation("Flash Random", 255, 0, 0, 5)  
  else:
    runtime.error(errorType + str(param))
