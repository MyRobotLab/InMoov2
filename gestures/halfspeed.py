def halfspeed():
  #i01.startedGesture()
  if runtime.isStarted('i01.neoPixel'):
    i01_neoPixel.setAnimation("Color Wipe", 0, 200, 0, 50)
    sleep(1)
    i01_neoPixel.setAnimation("Ironman", 0, 255, 0, 50)
  if runtime.isStarted('i01.rightHand'):
    i01.setHandSpeed("right", 50.0, 50.0, 50.0, 50.0, 50.0, 50.0)
      
  if runtime.isStarted('i01.leftHand'):
    i01.setHandSpeed("left", 50.0, 50.0, 50.0, 50.0, 50.0, 50.0)
      
  if runtime.isStarted('i01.rightArm'):
    i01.setArmSpeed("right", 50.0, 50.0, 50.0, 50.0)
    
  if runtime.isStarted('i01.leftArm'):
    i01.setArmSpeed("left", 50.0, 50.0, 50.0, 50.0)
  
  if runtime.isStarted('i01.head'):
    i01.setHeadSpeed(50.0, 50.0, 50.0, 50.0, 100.0, 50.0)
  
  if runtime.isStarted('i01.torso'):
    i01.setTorsoSpeed(50.0, 50.0, 50.0)
      
  if runtime.isStarted('i01.eyeLids'):
    i01_head_eyelidLeft.setSpeed(50.0)
    i01_head_eyelidRight.setSpeed(50.0)
  i01.finishedGesture()  
