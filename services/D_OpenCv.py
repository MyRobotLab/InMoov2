# ##############################################################################
#            *** OPEN CV ***
# ##############################################################################


# ##############################################################################
#                 SET SERVICE
# ##############################################################################

#i01_opencv = Runtime.create("i01.opencv", "OpenCV")
opencv = runtime.getService('i01.opencv')
def initOpencv():
  opencv.getConfig()
  python.subscribe("opencv", "publishRecognizedFace")

def initTracking():
  if runtime.isStarted('i01.headTracking'):
    i01_headTracking.getConfig()
  if runtime.isStarted('i01.eyeTracking'):
    i01_eyeTracking.getConfig()
  trackingTimer = runtime.start("trackingTimer","Clock")
  trackingTimer.addListener("pulse", python.name, "trackingTimerRoutine")
  trackingTimer.setInterval(i01.getConfig().trackingTimeoutMs)  
  

def onRecognizedFace(name):
  #print(name)
  # robot reaction if recognized face ( todo beter reaction... )
  if runtime.isStarted('i01.opencv'):
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.startSession(unicode(name,'utf-8'))
      opencv.removeFilter("FaceRecognizer")
      i01_chatBot.getResponse("SYSTEM_SAY_HELLO")
      opencv.stopCapture()
      print("recognized:" + name)
  else:
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.getResponse("ALERT")
      i01_chatBot.getResponse("SYSTEM_ERROR_OPENCV_1")
