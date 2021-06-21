def fullspeed():
  if isNeopixelActivated:
    i01.setNeopixelAnimation("Color Wipe", 200, 0, 0, 1)
    sleep(1)
    i01.setNeopixelAnimation("Ironman", 0, 0, 255, 1)
  if isRightHandActivated:
    i01.setHandSpeed("right", 500.0, 500.0, 500.0, 500.0, 500.0, 500.0)
      
  if isLeftHandActivated:
    i01.setHandSpeed("left", 500.0, 500.0, 500.0, 500.0, 500.0, 500.0)
      
  if isRightArmActivated:
    i01.setArmSpeed("right", 500.0, 500.0, 500.0, 500.0)
    
  if isLeftArmActivated:
    i01.setArmSpeed("left", 500.0, 500.0, 500.0, 500.0)
  
  if isHeadActivated:
    i01.setHeadSpeed(500.0, 500.0, 500.0, 500.0, 500.0, 500.0)
  
  if isTorsoActivated:
    i01.setTorsoSpeed(500.0, 500.0, 500.0)
      
  if isEyeLidsActivated:
    i01.head.eyelidLeft.setSpeed(500.0)
    i01.head.eyelidRight.setSpeed(500.0)

