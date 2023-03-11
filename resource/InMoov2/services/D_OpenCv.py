# ##############################################################################
#            *** OPEN CV ***
# ##############################################################################


# ##############################################################################
#                 SET SERVICE
# ##############################################################################

#i01_opencv = Runtime.create("i01.opencv", "OpenCV")
if runtime.isStarted('i01.opencv'):
  opencv=i01_opencv
  opencv.getConfig()
  if flipPicture==1:opencv.addFilter("Flip")
  python.subscribe("i01.opencv", "publishRecognizedFace")
  

def onRecognizedFace(name):
  #print(name)
  # robot reaction if recognized face ( todo beter reaction... )
  if runtime.isStarted('i01.opencv'):
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.startSession(unicode(name,'utf-8'))
      i01_opencv.disableFilter("FaceRecognizer")
      i01_chatBot.getResponse("SYSTEM_SAY_HELLO")
      i01_opencv.removeFilter("FaceRecognizer")
  else:
    errorSpokenFunc("ALERT",", opencv is not started")
    if error_red==1:
      if runtime.isStarted('i01.neopixel'):
        i01.setNeopixelAnimation("Flash Random", 255, 0, 0, 5)    
