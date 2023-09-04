def whoisthis():
  if runtime.isStarted('i01.neoPixel'):
    i01_neoPixel.setAnimation("Color Wipe", 100, 5, 10, 15) 
  if runtime.isStarted('i01.chatBot'):
    if runtime.isStarted('i01.opencv'):
      if runtime.isStarted('i01.head'):
        i01.setHeadSpeed(70, 70, 70)
        i01.moveHead(90,90,20)
        sleep(1.3)
        i01.moveHead(90,90,170)
        sleep(2)
        i01.moveHead(90,90,90)
      i01_opencv.capture()
      i01_opencv.addFilter("FaceRecognizer")
      fr=i01_opencv.getFilter("FaceRecognizer")
      # set the name on the filter that will be used for the saved examples
      fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
      fr.train()
      fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
      python.subscribe("i01.opencv", "publishRecognizedFace")
      sleep(5)
      i01_opencv.removeFilter("FaceRecognizer")
      i01_opencv.stopCapture()
      i01.finishedGesture()
    else:
      if runtime.isStarted('i01.chatBot'):
        i01_chatBot.getResponse("ALERT")
        i01_chatBot.getResponse("SYSTEM_ERROR_OPENCV_1")
