def armRightSide():
  lookrightside()
  #i01.startedGesture()
  if runtime.isStarted('i01.rightArm'):
    i01.setArmSpeed("right", 36, 36, 36, 36)
    i01.moveArm("right",0,118,29,74)
    sleep(5)
    i01.finishedGesture()
    relax()