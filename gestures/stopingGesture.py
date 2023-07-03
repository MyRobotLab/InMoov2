#TODO: currently not working
def stopingGesture():
  i01.finishedGesture()
  if runtime.isStarted('i01.audioPlayer'):
    i01_audioPlayer.stop()
    i01_audioPlayer.stopPlaylist()
  if runtime.isStarted('i01.mouth'):
    i01_mouth.stop()  
  relax()
