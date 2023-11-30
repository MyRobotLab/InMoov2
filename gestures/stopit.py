def stopit():
  if runtime.isStarted("i01.audioPlayer"):
      i01_audioPlayer.stopPlaylist()
      i01_audioPlayer.stop()
  i01.stop()    
  lookinmiddle()
  sleep(0.2)
  relax()
  i01.finishedGesture()

