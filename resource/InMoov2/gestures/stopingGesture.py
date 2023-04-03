#TODO: currently not working
def stopingGesture():
  i01.finishedGesture()
  if runtime.isStarted('i01.audioPlayer'):
    i01_audioPlayer.stop()
  if runtime.isStarted('i01.mouth'):
    i01_mouth.stop()  
  relax()
