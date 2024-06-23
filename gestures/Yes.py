def Yes():
  if runtime.isStarted('i01.head'):
    i01_head_neck.setSpeed(90)
    i01_head_neck.moveToBlocking(90)
    i01_head_neck.moveToBlocking(50)
    i01_head_neck.moveToBlocking(120)
    i01_head_neck.moveToBlocking(70)
    i01_head_neck.rest()
    i01.finishedGesture()
