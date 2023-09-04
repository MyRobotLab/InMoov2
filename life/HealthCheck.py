# ##############################################################################
#                 TIMERS ACTION
# ##############################################################################

###############################################################################
# Timer function to autostart webkit microphone every 10seconds
# only if robot not actualy speaking
###############################################################################
if healthCheckActivated==1:
#if i01_fsm.getCurrentState()=="systemCheck":
  healthCheck = runtime.start("healthCheck","Clock")
  healthCheck.setInterval(60000)
  if batteryInSystem==1:
    batterieLevel=100
    errorBat=1
    try:
      if runtime.getBatteryLevel():
        batterieLevel = runtime.getBatteryLevel()
        print "battery :",batterieLevel
        errorBat=0
    except:
      pass
    healthCheck.addListener("pulse", python.name, "healthCheck_def")    
    healthCheck.startClock()


def healthCheck_def(timedata):
  global batterieLevel

  if not errorBat:
    if runtime.getBatteryLevel():batterieLevel = runtime.getBatteryLevel()
  i01.setBatteryLevel(int(batterieLevel))
  print "battery :",batterieLevel
  
  healthCheck.stopClock()
