def captureGesture1():
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
