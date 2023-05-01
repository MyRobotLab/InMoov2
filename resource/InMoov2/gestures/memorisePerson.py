from org.myrobotlab.opencv import OpenCVFilterFaceRecognizer

def YesName(name):
  print "name confirmed:"
  print(name)
  if runtime.isStarted('i01.neoPixel'):
    i01_neoPixel.setAnimation("Color Wipe", 100, 5, 10, 15) 
  if runtime.isStarted('i01.chatBot'):
    if runtime.isStarted('i01.opencv'):
      i01.cameraOn()
      i01_opencv.addFilter("FaceRecognizer")
      i01_opencv.setActiveFilter("FaceRecognizer")
      if runtime.isStarted('i01.head'):
          i01.setHeadSpeed(70, 70, 70)
          i01.moveHead(90,90,20)
          sleep(1.3)
          i01.moveHead(90,90,170)
          sleep(2)
          i01.moveHead(90,90,90)
      # set the name on the filter that will be used for the saved examples
      fr = i01_opencv.getFilter("FaceRecognizer")
      fr.setTrainName(unicode(name,'utf-8'))
      #fr.setTrainName(name)
      # set the filter to be in training mode (Where it learns new images)
      fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
      # now that we have new examples, let's re-train the face recognizer with all our examples.
      sleep(2)
      fr.train()
      # after we've retrained the model.. start recognizing again
      fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
      i01_opencv.disableFilter("FaceRecognizer")
      i01_opencv.removeFilter("FaceRecognizer")
      i01.finishedGesture()
    else:
      i01.warn('facerecognizer not starting because no opencv')

def memorisePerson(name):
  if faceRecognizerActivated==1:
    print(name)
    if runtime.isStarted('i01.neoPixel'):
      i01_neoPixel.setAnimation("Color Wipe", 100, 5, 10, 15) 
    if runtime.isStarted('i01.chatBot'):
      if runtime.isStarted('i01.opencv'):
        i01.cameraOn()
        i01_opencv.addFilter("FaceRecognizer")
        i01_opencv.setActiveFilter("FaceRecognizer")
        # if runtime.isStarted('i01.head'):
        #   i01.setHeadSpeed(70, 70, 70)
        #   i01.moveHead(90,90,20)
        #   sleep(1.3)
        #   i01.moveHead(90,90,170)
        #   sleep(2)
        #   i01.moveHead(90,90,90)
        # set the name on the filter that will be used for the saved examples
        fr = i01_opencv.getFilter("FaceRecognizer")
        fr.setTrainName(unicode(name,'utf-8'))
        #fr.setTrainName(name)
        # set the filter to be in training mode (Where it learns new images)
        fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
        # now that we have new examples, let's re-train the face recognizer with all our examples.
        fr.train()
        # after we've retrained the model.. start recognizing again
        fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
        i01_opencv.disableFilter("FaceRecognizer")
        i01_opencv.removeFilter("FaceRecognizer")
        i01_chatBot.getResponse("SYSTEM_SAY_HELLO")
        i01.finishedGesture()
      else:
        i01.warn('facerecognizer not starting because no opencv')
