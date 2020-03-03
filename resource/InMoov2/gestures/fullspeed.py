def fullspeed():
  if i01.isNeopixelActivated():
    i01.setNeopixelAnimation("Color Wipe", 200, 0, 0, 1)
    sleep(1)
    i01.setNeopixelAnimation("Ironman", 0, 0, 255, 1)
  if i01.isRightHandActivated():
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
      
  if i01.isLeftHandActivated():
    i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
      
  if i01.isRightArmActivated():
    i01.setArmVelocity("right", -1, -1, -1, -1)
    
  if i01.isLeftArmActivated():
    i01.setArmVelocity("left", -1, -1, -1, -1)
  
  if i01.isHeadActivated():
    i01.setHeadVelocity(-1, -1, -1)
  
  if i01.isTorsoActivated():
    i01.setTorsoVelocity(-1, -1, -1)
      
  if i01.isEyeLidsActivated():
    i01.setEyelidsVelocity(-1,-1)

