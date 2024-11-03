def handopen():
  if runtime.isStarted('i01_rightHand'):
    i01.moveHand("right",0,0,0,0,0)
  elif runtime.isStarted('i01_leftHand'):  
    i01.moveHand("left",0,0,0,0,0)
  i01.finishedGesture()
