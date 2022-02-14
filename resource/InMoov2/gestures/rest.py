# ##############################################################################
#         ROBOT REST POSITIONS ( minimal )
# ##############################################################################

def rest():
  fullspeed()
  if runtime.isStarted('i01.rightHand'):
    i01.rightHand.rest()
  
  if runtime.isStarted('i01.leftHand'):
    i01.leftHand.rest()
  
  if runtime.isStarted('i01.rightArm'):
    i01.rightArm.rest()
  
  if runtime.isStarted('i01.leftArm'):
    i01.leftArm.rest()
    
# ##############################################################################
#         ROBOT REST POSITIONS ( full )
# ##############################################################################    
  
  if runtime.isStarted('i01.head'):
    i01.head.rest()
  
  if runtime.isStarted('i01.torso'):
    i01.torso.rest()
    
  if runtime.isStarted('i01.eyeLids'):
    i01.head.eyelidLeft.rest()
    i01.head.eyelidRight.rest()
