def whoisthis():
  if runtime.isStarted('i01.neopixel'):
    i01.setNeopixelAnimation("Color Wipe", 100, 5, 10, 15) 
  if runtime.isStarted('i01.chatBot'):
    if runtime.isStarted('i01.opencv'):
      i01.cameraOn()
      fr=i01.opencv.setActiveFilter("FaceRecognizer")
      # set the name on the filter that will be used for the saved examples
      #fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
      fr.train#Name = name
      fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
      sleep(6)
      i01.setHeadSpeed(70, 70, 70)
      i01.moveHead(90,90,20)
      sleep(1.3)
      i01.moveHead(90,90,170)
      sleep(2)
      i01.moveHead(90,90,90)
      onRecognizedFace(name)
    else:
      errorSpokenFunc('OPENCVNOWORKY')

