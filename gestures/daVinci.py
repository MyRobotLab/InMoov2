def daVinci():
  #i01.startedGesture()
  if runtime.isStarted('i01.leftArm') and runtime.isStarted('i01.rightArm'):
    # get the current value of auto disable
    leftPreviousAutoDisableValue = i01_leftArm_omoplate.isAutoDisable()
    rightPreviousAutoDisableValue = i01_rightArm_omoplate.isAutoDisable()
    # turn off auto disable for this gesture
    i01_leftArm_omoplate.setAutoDisable(False)
    i01_rightArm_omoplate.setAutoDisable(False)
    i01_leftArm_omoplate.enable()
    i01_rightArm_omoplate.enable()
    i01.setHandSpeed("left", 100.0, 100.0, 100.0, 100.0, 100.0, 22.0)
    i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 22.0)
    i01.setArmSpeed("left", 36, 36, 36, 36)
    i01.setArmSpeed("right", 36, 36, 36, 36)
    i01.setHeadSpeed(31.0, 31.0)
    i01.moveHead(80,90)
    i01.moveArm("left",0,118,29,74)
    i01.moveArm("right",0,118,29,74)
    i01.moveHand("left",50,40,30,20,10,47)
    i01.moveHand("right",50,40,30,20,10,137)
    sleep(5)
    # restore the auto disable value after the gesture is done.
    i01_leftArm_omoplate.setAutoDisable(leftPreviousAutoDisableValue)
    i01_rightArm_omoplate.setAutoDisable(rightPreviousAutoDisableValue)
    i01.finishedGesture()

