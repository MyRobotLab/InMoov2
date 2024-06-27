# ##############################################################################
#            *** OPEN CV ***
# ##############################################################################


# ##############################################################################
#                 SET SERVICE
# ##############################################################################

def initOpencv():
  opencv = runtime.getService("i01.opencv")
  opencv.getConfig()
  python.subscribe("opencv", "publishRecognizedFace")

def initTracking():
  headTracking = runtime.getService("i01.headTracking")
  if headTracking:
    headTracking.getConfig()
  eyeTracking = runtime.getService("i01.eyeTracking")
  if eyeTracking:
    eyeTracking.getConfig()
  trackingTimer = runtime.start("trackingTimer","Clock")
  trackingTimer.addListener("pulse", python.name, "trackingTimerRoutine")
  trackingTimer.setInterval(i01.getConfig().trackingTimeoutMs)  
  

def onRecognizedFace(name):
  #print(name)
  # robot reaction if recognized face ( todo beter reaction... )
  opencv = runtime.getService("i01.opencv")
  chatBot = runtime.getService("i01.chatBot")
  if opencv:
    opencv.removeFilter("FaceRecognizer")
    sleep(1)
    opencv.stopCapture()
    if chatBot:
      chatBot.startSession(unicode(name,'utf-8'))
      chatBot.getResponse("SYSTEM_SAY_HELLO")
      print("recognized:" + name)
  else:
    if chatBot:
      chatBot.getResponse("ALERT")
      chatBot.getResponse("SYSTEM_ERROR_OPENCV_1")
