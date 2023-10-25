def fullspeed():
  #i01.startedGesture()
  if runtime.isStarted('i01.neoPixel'):
    i01_neoPixel.setAnimation("Color Wipe", 200, 0, 0, 50)
    sleep(1)
    i01_neoPixel.setAnimation("Ironman", 0, 255, 255, 50)

  if runtime.isStarted('i01.rightHand'):  
    i01.setHandSpeed("right", 500.0, 500.0, 500.0, 500.0, 500.0, 500.0)
      
  if runtime.isStarted('i01.leftHand'):
    i01.setHandSpeed("left", 500.0, 500.0, 500.0, 500.0, 500.0, 500.0)
      
  if runtime.isStarted('i01.rightArm'):
    i01.setArmSpeed("right", 500.0, 500.0, 500.0, 500.0)
    
  if runtime.isStarted('i01.leftArm'):
    i01.setArmSpeed("left", 500.0, 500.0, 500.0, 500.0)
  
  if runtime.isStarted('i01.head'):
    i01.setHeadSpeed(500.0, 500.0, 500.0, 500.0, 500.0, 500.0)
  
  if runtime.isStarted('i01.torso'):
    i01.setTorsoSpeed(500.0, 500.0, 500.0)
      
  if runtime.isStarted('i01.eyeLids'):
    i01_head_eyelidLeft.setSpeed(500.0)
    i01_head_eyelidRight.setSpeed(500.0)
  i01.finishedGesture()  

