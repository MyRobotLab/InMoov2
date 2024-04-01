# ##############################################################################
#            *** PIR SENSOR ***
# ##############################################################################


# ##############################################################################
#                 SET SERVICE
# ##############################################################################

#publishPin=0
def initPir():
  pir=i01_pir
  pir.getConfig()
  #pirPin=pir.getConfig().pin
  #pirControlerArduino=pir.getConfig().controller
  pir.addListener("publishSense",python.name,"publishSense")
  sleepTimer = runtime.start("sleepTimer","Clock")
  sleepTimer.addListener("pulse", python.name, "sleepTimerRoutine")
  sleepTimer.setInterval(i01.getConfig().sleepTimeoutMs)


#analog pin listener read the pir
def publishSense(event):
  if runtime.isStarted("i01.pir"):
    #publishPin=1
    if event:
      print "pir detected something"
      #if not i01.RobotIsSleeping and i01.RobotIsStarted:
      if runtime.isStarted('i01.fsm'):
        if not i01_fsm.getState()=="sleep" and i01_fsm.getState()=="idle" and "setup": 
          #i01_pir.disable()
          humanDetected()
        
        #wakeup action
        #if i01.RobotIsSleeping:
        if i01_fsm.getState()=="sleep":
          i01_pir.disable()
          sleepModeWakeUp()
      else:
        i01_pir.disable()
        sleepModeWakeUp()
          
  else:
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.getResponse("ALERT")
      i01_chatBot.getResponse("SYSTEM_ERROR_PIR_1")
    
