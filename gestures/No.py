def No():
  if runtime.isStarted('i01.head'):
    i01_head_rothead.setSpeed(90)
    i01_head_rothead.moveToBlocking(130)
    i01_head_rothead.moveToBlocking(50)
    i01_head_rothead.moveToBlocking(130)
    i01_head_rothead.rest()
    i01.finishedGesture()
