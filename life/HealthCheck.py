# ##############################################################################
#                 TIMERS ACTION
# ##############################################################################

###############################################################################
# Timer function to autostart webkit microphone every 10seconds
# only if robot not actualy speaking
###############################################################################

if runtime.isStarted('i01'):
  if i01.getConfig().heartbeat==1:
  #if i01_fsm.getCurrentState()=="systemCheck":
    heartbeat = runtime.start("heartbeat","Clock")
    heartbeat.setInterval(60000)
    if i01.getConfig().batteryInSystem:
      batterieLevel=100
      errorBat=1
      try:
        if runtime.getBatteryLevel():
          batterieLevel = runtime.getBatteryLevel()
          print ("battery :",batterieLevel)
          errorBat=0
      except:
        pass
      heartbeat.addListener("pulse", python.name, "heartbeat_def")    
      heartbeat.startClock()


def heartbeat_def(timedata):
  global batterieLevel

  if not errorBat:
    if runtime.getBatteryLevel():batterieLevel = runtime.getBatteryLevel()
  i01.setBatteryLevel(int(batterieLevel))
  print("battery :",batterieLevel)
  
  heartbeat.stopClock()

print("HealthCheck.py loaded")
