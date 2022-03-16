def cry():
  #i01.startedGesture()
  x = (random.randint(1, 2))
  if x == 1:
    Yes()
    i01_audioPlayer.playFile('resource/InMoov2/system/sounds/cryBaby.mp3')  
    sleep(2)
    ear.setAutoListen(setAutoListen)
  if x == 2:
    No()
    i01_audioPlayer.playFile('resource/InMoov2/system/sounds/Sad-Robot.mp3')  
    sleep(2)
    ear.setAutoListen(setAutoListen)
  i01.finishedGesture()  
