# ##############################################################################
#         ROBOT REST POSITIONS ( minimal )
# ##############################################################################

def rest():
  fullspeed()
  if runtime.isStarted('i01.rightHand'):
    i01_rightHand.rest()
  
  if runtime.isStarted('i01.leftHand'):
    i01_leftHand.rest()
  
  if runtime.isStarted('i01.rightArm'):
    i01_rightArm.rest()
  
  if runtime.isStarted('i01.leftArm'):
    i01_leftArm.rest()
    
# ##############################################################################
#         ROBOT REST POSITIONS ( full )
# ##############################################################################    
  
  if runtime.isStarted('i01.head'):
    i01_head.rest()
  
  if runtime.isStarted('i01.torso'):
    i01_torso.rest()
    
  if runtime.isStarted('i01.eyeLids'):
    i01_head_eyelidLeft.rest()
    i01_head_eyelidRight.rest()
  i01.finishedGesture()  
