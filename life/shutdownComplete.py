# ##############################################################################
#                 COMPUTER SHUTDOWN MODE
# ##############################################################################

###############################################################################
# function called it swing cross used or magical single keyword 'ROBOT COMPLETE SHUTDOWN'
###############################################################################
python.subscribe(runtime,"shutdown")

def shutdownComplete():
  if runtime.isStarted('i01.chatBot'):
    i01_chatBot.getResponse("SYSTEM_EVENT SHUTDOWNCOMPLETE")
  else:
    runtime.info(str(i01_chatBot.getResponse("SYSTEM_EVENT SHUTDOWNCOMPLETE")))
  sleep(2)
  runtime.execute("cmd.exe","/c","shutdown.exe /s /t 30 /f")
  shutdown()

print("shutdownComplete.py loaded")