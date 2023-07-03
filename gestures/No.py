def No():
  if runtime.isStarted('i01.head'):
    i01.setHeadSpeed(45,45,45)
    i01.moveHeadBlocking(80,130)
    sleep(0.5)
    i01.moveHeadBlocking(80,50)
    sleep(0.5)
    i01.moveHeadBlocking(80,130)
    sleep(0.5)
    i01.moveHeadBlocking(80,90)
    i01.finishedGesture()