# ##############################################################################
#         ROBOT REST POSITIONS ( minimal )
# ##############################################################################

def rest():
  fullspeed()
  if i01.isRightHandActivated():
    i01.rightHand.rest()
  
  if i01.isLeftHandActivated():
    i01.leftHand.rest()
  
  if i01.isRightArmActivated():
    i01.rightArm.rest()
  
  if i01.isLeftArmActivated():
    i01.leftArm.rest()
    
# ##############################################################################
#         ROBOT REST POSITIONS ( full )
# ##############################################################################    
  
  if i01.isHeadActivated():
    i01.head.rest()
  
  if i01.isTorsoActivated():
    i01.torso.rest()
    
  if i01.isEyeLidsActivated():
    i01.eyelids.rest()