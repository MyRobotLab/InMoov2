# ##############################################################################
#            *** OPEN CV ***
# ##############################################################################


# ##############################################################################
#                 SET SERVICE
# ##############################################################################

#i01_opencv = Runtime.create("i01.opencv", "OpenCV")
def initOpencv():
  i01_opencv.getConfig()
  if flipPicture==1:i01_opencv.addFilter("Flip")
  python.subscribe("i01.opencv", "publishRecognizedFace")

def initTracking():
  if runtime.isStarted('i01.headTracking'):
    i01_headTracking.getConfig()
  if runtime.isStarted('i01.eyeTracking'):
    i01_eyeTracking.getConfig()
  trackingTimer = runtime.start("trackingTimer","Clock")
  trackingTimer.addListener("pulse", python.name, "trackingTimerRoutine")
  trackingTimer.setInterval(trackingTimeout)  
  

def onRecognizedFace(name):
  #print(name)
  # robot reaction if recognized face ( todo beter reaction... )
  if runtime.isStarted('i01.opencv'):
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.startSession(unicode(name,'utf-8'))
      i01_opencv.removeFilter("FaceRecognizer")
      i01_chatBot.getResponse("SYSTEM_SAY_HELLO")
  else:
    errorSpokenFunc("ALERT",", opencv is not started")
