# ##############################################################################
#                 ROBOT SHUTDOWN MODE
# ##############################################################################

###############################################################################
# function called it swing cross used or magical single keyword 'shutdown' 'extinction' 'afsluiten'
###############################################################################

def shutdown():
  if runtime.isStarted('i01.chatBot'):
    i01_chatBot.getResponse("SYSTEM_EVENT SHUTDOWN")
  else:
    runtime.info(str(i01_chatBot.getResponse("SYSTEM_EVENT SHUTDOWN")))
  sleep(4)
  if runtime.isStarted('i01.head.eyelids'):
    i01_head.autoBlink(False)
    i01_head_eyelidLeft.moveTo(180)
    i01_head_eyelidRight.moveTo(180)
  if runtime.isStarted('i01.neopixel'):  
    i01.stopNeopixelAnimation()
  runtime.shutdown()

print("shutdown.py loaded")