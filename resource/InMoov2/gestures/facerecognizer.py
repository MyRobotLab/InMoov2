def facerecognizer(): 
  #you need to train at least 2 FACES !
  if runtime.isStarted('i01.opencv'):
    i01.cameraOn()
    i01_opencv.addFilter("FaceRecognizer")
    fr = i01_opencv.getFilter("FaceRecognizer")
    fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
    fr.train()# it takes some time to train and be able to recognize face
    fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
    i01.finishedGesture()
  else:
    errorSpokenFunc('OPENCVNOWORKY')  
