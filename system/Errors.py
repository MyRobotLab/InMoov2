# -- coding: utf-8 --
# ##############################################################################
# ERRORS FILE
# ##############################################################################

def errorSpokenFunc(errorType,param=""):
  if error_red==1:
      if runtime.isStarted('i01.neoPixel'):
        RobotIsErrorMode=1
        i01_neoPixel.setAnimation("Theater Chase", 255, 0, 0, 50)
  if runtime.isStarted('i01.mouth'):
    i01_mouth.speakBlocking(i01.localize(errorType)+str(param))
    if runtime.isStarted('i01.neoPixel'):
      i01_neoPixel.clear()
      RobotIsErrorMode=0
  else:
    runtime.error(errorType + str(param))
