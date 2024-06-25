def captureGesture2():
  i01_audioPlayer.playFile('resource/InMoov2/system/sounds/ShutterCapture.mp3')
  python.addScript("newGesture", i01.captureGesture())
  i01.finishedGesture()
