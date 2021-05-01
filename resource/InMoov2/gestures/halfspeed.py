def halfspeed():
  if isNeopixelActivated:
    i01.setNeopixelAnimation("Color Wipe", 0, 200, 0, 1)
    sleep(1)
    i01.setNeopixelAnimation("Ironman", 0, 255, 0, 1)
  if isRightHandActivated:
    i01.setHandSpeed("right", 50.0, 50.0, 50.0, 50.0, 50.0, 50.0)
      
  if isLeftHandActivated:
    i01.setHandSpeed("left", 50.0, 50.0, 50.0, 50.0, 50.0, 50.0)
      
  if isRightArmActivated:
    i01.setArmSpeed("right", 50.0, 50.0, 50.0, 50.0)
    
  if isLeftArmActivated:
    i01.setArmSpeed("left", 50.0, 50.0, 50.0, 50.0)
  
  if isHeadActivated:
    i01.setHeadSpeed(50.0, 50.0, 50.0, 50.0, 100.0, 50.0)
  
  if isTorsoActivated:
    i01.setTorsoSpeed(50.0, 50.0, 50.0)
      
  if isEyeLidsActivated:
    i01.setEyelidsSpeed(50.0,50.0)