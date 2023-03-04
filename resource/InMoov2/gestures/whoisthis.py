def whoisthis():
  if runtime.isStarted('i01.neopixel'):
    i01.setNeopixelAnimation("Color Wipe", 100, 5, 10, 15) 
  if runtime.isStarted('i01.chatBot'):
    if runtime.isStarted('i01.opencv'):
      i01.cameraOn()
      i01_opencv.addFilter("FaceRecognizer")
      i01_opencv.setActiveFilter("FaceRecognizer")
      fr=i01_opencv.getFilter("FaceRecognizer")
      # set the name on the filter that will be used for the saved examples
      fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
      fr.train()
      fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
      sleep(6)
      i01.setHeadSpeed(70, 70, 70)
      i01.moveHead(90,90,20)
      sleep(1.3)
      i01.moveHead(90,90,170)
      sleep(2)
      i01.moveHead(90,90,90)
      python.subscribe("i01.opencv", "publishRecognizedFace")
    else:
      errorSpokenFunc('OPENCVNOWORKY')
    i01.finishedGesture()

