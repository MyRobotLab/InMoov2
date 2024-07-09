from org.myrobotlab.opencv import OpenCVFilterFaceRecognizer

def YesName(name):
  print(name)
  if runtime.isStarted('i01.neoPixel'):
    i01_neoPixel.setAnimation("Color Wipe", 100, 5, 10, 15) 
  if runtime.isStarted('i01.chatBot'):
    opencv = i01.startPeer('opencv')
    if runtime.isStarted('i01.opencv'):
      opencv.capture()
      sleep(5)
      opencv.addFilter("FaceRecognizer")
      opencv.setActiveFilter("FaceRecognizer")
      if runtime.isStarted('i01.head'):
          i01.setHeadSpeed(70, 70, 70)
          i01.moveHead(90,90,20)
          sleep(1.3)
          i01.moveHead(90,90,170)
          sleep(2)
          i01.moveHead(90,90,90)
      # set the name on the filter that will be used for the saved examples
      fr = opencv.getFilter("FaceRecognizer")
      fr.setTrainName(unicode(name,'utf-8'))
      # set the filter to be in training mode (Where it learns new images)
      fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
      sleep(4)
      # now that we have new examples, let's re-train the face recognizer with all our examples.
      fr.train()
      # after we've retrained the model.. start recognizing again
      fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
      opencv.removeFilter("FaceRecognizer")
      sleep(1)
      opencv.stopCapture()
      i01_chatBot.getResponse("SYSTEM_SAY_HELLO")
      i01.finishedGesture()
    else:
      i01.warn('facerecognizer not starting because no opencv')

def memorisePerson(name):
  if i01.getConfig().openCVFaceRecognizerActivated==1:
    print(name)
    if runtime.isStarted('i01.neoPixel'):
      i01_neoPixel.clear()
      i01_neoPixel.setAnimation("Color Wipe", 100, 5, 10, 15)
    if runtime.isStarted('i01.chatBot'):
      opencv = i01.startPeer('opencv')
      if runtime.isStarted('i01.opencv'):
        opencv.capture()
        sleep(5)
        opencv.addFilter("FaceRecognizer")
        opencv.setActiveFilter("FaceRecognizer")
        # if runtime.isStarted('i01.head'):
        #   i01.setHeadSpeed(70, 70, 70)
        #   i01.moveHead(90,90,20)
        #   sleep(1.3)
        #   i01.moveHead(90,90,170)
        #   sleep(2)
        #   i01.moveHead(90,90,90)
        # set the name on the filter that will be used for the saved examples
        fr = opencv.getFilter("FaceRecognizer")
        fr.setTrainName(unicode(name,'utf-8'))
        #fr.setTrainName(name)
        # set the filter to be in training mode (Where it learns new images)
        fr.setMode(OpenCVFilterFaceRecognizer.Mode.TRAIN)
        sleep(4)
        # now that we have new examples, let's re-train the face recognizer with all our examples.
        fr.train()
        # after we've retrained the model.. start recognizing again
        fr.setMode(OpenCVFilterFaceRecognizer.Mode.RECOGNIZE)
        opencv.removeFilter("FaceRecognizer")
        sleep(1)
        opencv.stopCapture()
        i01_chatBot.getResponse("SYSTEM_SAY_HELLO")
        i01.finishedGesture()
      else:
        i01.warn('facerecognizer not starting because no opencv')
        if runtime.isStarted('i01.chatBot'):
          i01_chatBot.getResponse("NOTMEMORIZED")
  else:
        i01.warn('facerecognizer is OFF')
        if runtime.isStarted('i01.chatBot'):
          i01_chatBot.getResponse("NOTFACERECOGNIZED")        

def takeMyPicture(name):
    opencv = i01.startPeer('opencv')
    opencv.capture()
    opencv.addFilter("SetImageROI")
    sleep(10)# Add delay if opencv error recordFrame()
    #protect_counter = 0
    #while opencv.getBase64Image() is None and protect_counter < 60:
      #protect_counter+=1
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.getResponse("GETREADY")
    rect = i01_opencv.getFilter("SetImageROI") 
    # changing parameters
    x=0
    y=0
    width=450
    height=450
    rect.setROI(x, y, width, height)
    photoFileName = opencv.recordFrame()
    if runtime.isStarted('i01.audioPlayer'):
      i01_audioPlayer.playFile('resource/InMoov2/system/sounds/ShutterClik.mp3')
    opencv.removeFilters()
    print(photoFileName)
    sleep(2)
    opencv.stopCapture()
    #i01.releasePeer('opencv')
    picturePath='resource/ProgramAB/'
    shutil.move(photoFileName,picturePath)
    newName = unicode(name,'utf-8')+'.png'
    print(newName)
    sleep(1)
    os.chdir(picturePath)
    matching_names = glob.glob('i01.opencv-*.png')
    try:
      if matching_names:
        os.rename(matching_names[0], newName)
        os.chdir("../../")
    except:
      os.remove(matching_names[0])
      os.chdir("../../")
      pass
    i01.finishedGesture()
