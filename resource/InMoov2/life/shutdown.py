# ##############################################################################
#                 ROBOT SHUTDOWN MODE
# ##############################################################################

###############################################################################
# function called it swing cross used or magical single keyword 'shutdown' 'extinction' 'afsluiten'
###############################################################################

def shutdown():
  i01.speakBlocking(i01.localize("SHUTDOWN"))
  #if isEyeLidsActivated:
    #i01_head.autoBlink(False)
    #i01_head_eyelidLeft.moveTo(180)
    #i01_head_eyelidRight.moveTo(180)
  if isNeopixelActivated:  
    i01.stopNeopixelAnimation()
  runtime.shutdown()
