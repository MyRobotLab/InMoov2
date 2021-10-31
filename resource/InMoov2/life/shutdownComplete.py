# ##############################################################################
#                 COMPUTER SHUTDOWN MODE
# ##############################################################################

###############################################################################
# function called it swing cross used or magical single keyword 'ROBOT COMPLETE SHUTDOWN'
###############################################################################
python.subscribe(runtime,"shutdown")

def shutdownComplete():
  i01.speakBlocking(i01.localize("SHUTDOWNCOMPLETE"))
  runtime.execute("cmd.exe","/c","shutdown.exe /s /t 30 /f")
  shutdown()
  
