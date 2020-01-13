# ##############################################################################
#                 ROBOT SHUTDOWN MODE
# ##############################################################################

###############################################################################
# function called it swing cross used or magical single keyword 'shutdown' 'extinction' 'afsluiten'
###############################################################################

def shutdown():
  if i01.isEyeLidsActivated():
    eyelids.autoBlink(False)
    eyelids.eyelidleft.moveTo(180)
    eyelids.eyelidright.moveTo(180)
  if i01.isNeopixelActivated():  
    i01.stopNeopixelAnimation()
  runtime.shutdown()
