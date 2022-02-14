# ##############################################################################
#                 TIMERS ACTION
# ##############################################################################

###############################################################################
# Timer function to autostart webkit microphone every 10seconds
# only if robot not actualy speaking
###############################################################################
if HealthCheckActivated==1:
  HealthCheck = Runtime.start("HealthCheck","Clock")
  HealthCheck.setInterval(60000)
  if BatteryInSystem==1:
    batterieLevel=100
    errorBat=1
    try:
      if Runtime.getBatteryLevel():
        batterieLevel = Runtime.getBatteryLevel()
        print "battery :",batterieLevel
        errorBat=0
    except:
      pass
    HealthCheck.addListener("pulse", python.name, "HealthCheck_def")    
    HealthCheck.startClock()


def HealthCheck_def(timedata):
  global batterieLevel

  if not errorBat:
    if Runtime.getBatteryLevel():batterieLevel = Runtime.getBatteryLevel()
  i01.setBatteryLevel(int(batterieLevel))
  print "battery :",batterieLevel
  
  if RobotIsErrorMode==1:
    if error_red:
      if runtime.isStarted('i01.neopixel'):
        i01.setNeopixelAnimation("Flash Random", 255, 0, 0, 5)
      
  else:HealthCheck.stopClock()
