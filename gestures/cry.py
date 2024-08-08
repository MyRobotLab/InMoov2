def cry():
  #i01.startedGesture()
  x = (random.randint(1, 2))
  if x == 1:
    Yes()
    upperEyelidsClose()
    cheeksD()
    if runtime.isStarted('i01.mouth.audioFile'):
      i01_mouth_audioFile.playBlocking('resource/InMoov2/system/sounds/cryBaby.mp3')  
    neutral()
  if x == 2:
    upperEyelidsClose()
    cheeksD()
    if runtime.isStarted('i01.mouth.audioFile'):
      i01_mouth_audioFile.playBlocking('resource/InMoov2/system/sounds/Sad-Robot.mp3')  
    neutral()
  i01.finishedGesture()  
