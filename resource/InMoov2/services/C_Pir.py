# ##############################################################################
#            *** PIR SENSOR ***
# ##############################################################################

# exemple after 5 minutes of inactivity we call the function sleepModeSleep()
# and if human is detected and if the robot sleeping we call sleepModeWakeUp()


# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  



# ##############################################################################
#                 SERVICE START
# ##############################################################################
#pir timer to avoid human detection notification every seconds...


#analog pin listener read the pir
def publishPinPir(pins):
  if runtime.isStarted("i01.pir"):
    pir=i01_pir
    PirPin=pir.getConfig().pin
    PirControlerArduino=pir.getConfig().controller
  else:
    i01.speakBlocking(i01.localize("PIRNOWORKY"))
    runtime.error("pir error, not started") 
  

  for pin in range(0, len(pins)):
    
    #human detected
    if pins[pin].value>0:
      #if not i01.RobotIsSleeping and i01.RobotIsStarted:
      if runtime.isStarted('i01.fsm'):
        if not i01_fsm.getCurrentState()=="sleeping" and i01_fsm.getCurrentState()=="awake" or "systemCheck": 
          humanDetected()
      
      #wakeup action
      #if i01.RobotIsSleeping:
      if runtime.isStarted('i01.fsm'):
        if i01_fsm.getCurrentState()=="sleeping":
          i01_pir.disablePin(pirPin)
          sleepModeWakeUp()
