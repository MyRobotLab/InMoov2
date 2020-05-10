# -- coding: utf-8 --
# ##############################################################################
# ERRORS FILE
# ##############################################################################

def errorSpokenFunc(errorType,param=""):
  global RobotIsErrorMode 
  RobotIsErrorMode=1
  i01.speakAlert(i01.localize(errorType)+str(param))