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
  sleepTimer.setInterval(sleepTimeout)


#analog pin listener read the pir
def publishSense(event):
  if runtime.isStarted("i01.pir"):
    #publishPin=1
    if event:
      print "I should wake up"
      #if not i01.RobotIsSleeping and i01.RobotIsStarted:
      if runtime.isStarted('i01.fsm'):
        #if not i01_fsm.getCurrentState()=="sleeping" and i01_fsm.getCurrentState()=="awake" or "systemCheck": 
          #i01_pir.disable()
          #humanDetected()
        
      #wakeup action
      #if i01.RobotIsSleeping:
        #if i01_fsm.getCurrentState()=="sleeping":
        i01_pir.disable()
        sleepModeWakeUp()
          
  else:
    errorSpokenFunc("ALERT",", p,i,r is not started")
    