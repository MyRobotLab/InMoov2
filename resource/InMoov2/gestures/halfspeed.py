def halfspeed():
  if runtime.isStarted('i01.neopixel'):
    i01.setNeopixelAnimation("Color Wipe", 0, 200, 0, 1)
    sleep(1)
    i01.setNeopixelAnimation("Ironman", 0, 255, 0, 1)
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
    i01.head.eyelidLeft.setSpeed(50.0)
    i01.head.eyelidRight.setSpeed(50.0)
