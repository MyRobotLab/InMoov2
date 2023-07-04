def batterylevel():
  #i01.startedGesture()
  print("battery level is " + str(batterieLevel)+" percent")
  if runtime.isStarted('i01.mouth'):
    i01_mouth.speak(str(batterieLevel)+" percent")
  i01.finishedGesture()
  