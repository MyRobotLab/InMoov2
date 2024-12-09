def healthCheckSequence():
  if i01.getConfig().healthCheckActivated==1:
    print("health check sequence initiated")
    if runtime.isStarted('i01'):
      i01.fullSpeed()
    if runtime.isStarted('i01.head'):
      i01_head.rest()
    if runtime.isStarted('i01.rightHand'):
      i01_rightHand.rest()
    if runtime.isStarted('i01.leftHand'):
      i01_leftHand.rest()
    if runtime.isStarted('i01.rightArm'):
      i01_rightArm.rest()
    if runtime.isStarted('i01.leftArm'):
      i01_leftArm.rest()
    if runtime.isStarted('i01.torso'):
      i01_torso.rest()
    if runtime.isStarted('i01.head.eyelidLeft'):
      i01_head_eyelidLeft.rest()
    if runtime.isStarted('i01.head.eyelidRight'):  
      i01_head_eyelidRight.rest()
    i01.finishedGesture()
