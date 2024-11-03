def handclose():
  if runtime.isStarted('i01_rightHand'):
    i01.moveHand("right",180,180,180,180,180)
  elif runtime.isStarted('i01_leftHand'):  
    i01.moveHand("left",180,180,180,180,180)
  i01.finishedGesture()
