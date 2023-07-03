def tiltHeadRightSide():
  #i01.startedGesture()
  i01.setHeadSpeed(70, 70, 70)
  i01.moveHead(90,90,20)
  sleep(1.0)
  i01.moveHead(90,90,90)
  sleep(1)
  i01.finishedGesture()