def facerecognizer(): 
  #you need to train at least 2 FACES !
  if i01.getConfig().openCVFaceRecognizerActivated==1:
    if runtime.isStarted('i01.opencv'):
      i01_opencv.capture()
      i01_opencv.addFilter("FaceRecognizer")
      i01_opencv.setActiveFilter("FaceRecognizer")
      fr = i01_opencv.getFilter("FaceRecognizer")
      fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
      fr.train()# it takes some time to train and be able to recognize face
      fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
      python.subscribe("i01.opencv", "publishRecognizedFace")
    else:
      i01.warn('facerecognizer not starting because no opencv')
      if runtime.isStarted('i01.chatBot'):
        i01_chatBot.setPredicate("topic", "firstinit")
        i01_chatBot.getResponse("NOTMEMORIZED")
  else:
    i01.warn('facerecognizer is OFF')
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.getResponse("NOTFACERECOGNIZED")
  i01.finishedGesture()
