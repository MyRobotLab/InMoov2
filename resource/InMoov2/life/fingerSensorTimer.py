# ##############################################################################
#            *** ROBOT FINGER SENSOR TIMER ***
# ##############################################################################
if rightHandSensorActivated==1 or leftHandSensorActivated==1:
  sensorTimer = runtime.start("sensorTimer","Clock")
  sensorTimer.addListener("pulse", python.name, "sensorTimerRoutine")
  sensorTimer.addListener("clockStarted", python.name, "sensorTimerStart")  
  sensorTimer.addListener("clockStopped", python.name, "sensorTimerStop")

  #loop every 1000ms
  sensorTimer.setInterval(1000)

def sensorTimerStart():
  if rightHandSensorActivated:
    print "====TimerSensorON===="
  if leftHandSensorActivated:
    print "====TimerSensorON===="

def sensorTimerStop():
  if rightHandSensorActivated:
    rightHandSensorOFF()

  if leftHandSensorActivated:
    leftHandSensorOFF()

def sensorTimerRoutine(timedata):
  if rightHandSensorActivated:
    rightHandSensorON()
  if leftHandSensorActivated:
    leftHandSensorON()
