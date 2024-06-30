def captureGesture1():
  print"i01_head_eyeLeftUD.moveTo("+str(i01_head_eyeLeftUD.getPos())+")"
  print"i01_head_eyeLeftLR.moveTo("+str(i01_head_eyeLeftLR.getPos())+")"
  print"i01_head_eyeRightUD.moveTo("+str(i01_head_eyeRightUD.getPos())+")"
  print"i01_head_eyeRightLR.moveTo("+str(i01_head_eyeRightLR.getPos())+")"
  ## the eyelids
  print"i01_head_eyelidLeftUpper.moveTo("+str(i01_head_eyelidLeftUpper.getPos())+")"
  print"i01_head_eyelidLeftLower.moveTo("+str(i01_head_eyelidLeftLower.getPos())+")"
  print"i01_head_eyelidRightUpper.moveTo("+str(i01_head_eyelidRightUpper.getPos())+")"
  print"i01_head_eyelidRightLower.moveTo("+str(i01_head_eyelidRightLower.getPos())+")"
  ## the eyebrows
  print"i01_head_eyebrowRight.moveTo("+str(i01_head_eyebrowRight.getPos())+")"
  print"i01_head_eyebrowLeft.moveTo("+str(i01_head_eyebrowLeft.getPos())+")"
  ## the cheeks
  print"i01_head_cheekRight.moveTo("+str(i01_head_cheekRight.getPos())+")"
  print"i01_head_cheekLeft.moveTo("+str(i01_head_cheekLeft.getPos())+")"
  ## the upper lip
  print"i01_head_upperLip.moveTo("+str(i01_head_upperLip.getPos())+")"
  ## the for head
  print"i01_head_forheadRight.moveTo("+str(i01_head_forheadRight.getPos())+")"
  print"i01_head_forheadLeft.moveTo("+str(i01_head_forheadLeft.getPos())+")"
  print"## i2Head"
  #head
  print"i01_head.moveTo("+str(i01_head_neck.getPos())+","+str(i01_head_rothead.getPos())+","+str(i01_head_eyeX.getPos())+","+str(i01_head_eyeY.getPos())+","+str(i01_head_jaw.getPos())+","+str(i01_head_rollNeck.getPos())+")"
  #armLeft
  print "i01_leftArm.moveTo("+str(i01_leftArm_bicep.getPos())+","+str(i01_leftArm_rotate.getPos())+","+str(i01_leftArm_shoulder.getPos())+","+str(i01_leftArm_omoplate.getPos())+")"
  #handLeft
  print "i01_leftHand.moveTo("+str(i01_leftHand_thumb.getPos())+","+str(i01_leftHand_index.getPos())+","+str(i01_leftHand_majeure.getPos())+","+str(i01_leftHand_ringFinger.getPos())+","+str(i01_rightHand_wrist.getPos())+")"
  #armRight
  print "i01_rightArm.moveTo("+str(i01_rightArm_bicep.getPos())+","+str(i01_rightArm_rotate.getPos())+","+str(i01_rightArm_shoulder.getPos())+","+str(i01_rightArm_omoplate.getPos())+")"
  #handRight
  print "i01_rightHand.moveTo("+str(i01_rightHand_thumb.getPos())+","+str(i01_rightHand_index.getPos())+","+str(i01_rightHand_majeure.getPos())+","+str(i01_rightHand_ringFinger.getPos())+","+str(i01_rightHand_wrist.getPos())+")"
  #torso
  print "i01_torso.moveTo("+str(i01_torso_topStom.getPos())+","+str(i01_torso_midStom.getPos())+","+str(i01_torso_lowStom.getPos())+")"
