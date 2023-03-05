# ##############################################################################
#            *** PIR SENSOR ***
# ##############################################################################


# ##############################################################################
#                 SET SERVICE
# ##############################################################################

publishPin=0

#analog pin listener read the pir
def publishPinPir(pins):
  publishPin=1
  if runtime.isStarted("i01.pir"):
    pir=i01_pir
    pirPin=pir.getConfig().pin
    pirControlerArduino=pir.getConfig().controller
  else:
    i01.speakBlocking(i01.localize("PIRNOWORKY"))
    errorSpokenFunc("ALERT",", p,i,r is not started")
    if error_red==1:
      if runtime.isStarted('i01.neopixel'):
        i01.setNeopixelAnimation("Flash Random", 255, 0, 0, 5) 
  

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
