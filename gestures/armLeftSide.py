def armLeftSide():
  lookleftside()
  #i01.startedGesture()
  if runtime.isStarted('i01.leftArm'):
    i01.setArmSpeed("left", 36, 36, 36, 36)
    i01.moveArm("left",0,118,29,74)
    sleep(5)
    i01.finishedGesture()
    relax()