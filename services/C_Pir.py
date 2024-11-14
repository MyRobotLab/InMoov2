# ##############################################################################
#            *** PIR SENSOR ***
# ##############################################################################


# ##############################################################################
#                 SET SERVICE
# ##############################################################################

def initPir():
  pir=i01_pir
  pir.getConfig()
  #pirPin=pir.getConfig().pin
  #pirControlerArduino=pir.getConfig().controller
  pir.addListener("publishSense",python.name,"publishSense")
  # pir.addListener("publishPirOn",python.name,"publishPirOn")
  # pir.addListener("publishPirOff",python.name,"publishPirOff")
  sleepTimer = runtime.start("sleepTimer","Clock")
  sleepTimer.addListener("pulse", python.name, "sleepTimerRoutine")
  sleepTimer.setInterval(i01.getConfig().sleepTimeoutMs)

# analog pin listener read the pir
def publishSense(event):
  if runtime.isStarted("i01.pir"):
    if event:
      print "pir detected something"
      initPir()
      if runtime.isStarted('i01.fsm'):
        if i01_fsm.getState()=="idle" or "setup" or "wake":
          #i01_pir.disable()
          humanDetected()
        #wakeup action
        if i01_fsm.getState()=="sleep":
          i01_pir.disable()
          sleepModeWakeUp()
      else:
        i01_pir.disable()
        sleepModeWakeUp()

# def publishPirOn():
#   if runtime.isStarted("i01.pir"):
#     print "pir detected something"
#   else:
#     if runtime.isStarted('i01.chatBot'):
#       i01_chatBot.getResponse("ALERT")
#       i01_chatBot.getResponse("SYSTEM_ERROR_PIR_1")

# def publishPirOff():
#   if runtime.isStarted("i01.pir"):
#     print "pir idle"
#   else:
#     if runtime.isStarted('i01.chatBot'):
#       i01_chatBot.getResponse("ALERT")
#       i01_chatBot.getResponse("SYSTEM_ERROR_PIR_1")

