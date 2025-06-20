## sync the i2Head eyes with the default i01.eyes
if runtime.isStarted('i01.head') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightLR') and runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeRightUD'):
  i01_head_eyeX.sync(i01_head_eyeLeftLR)
  i01_head_eyeX.sync(i01_head_eyeRightLR)
  i01_head_eyeY.sync(i01_head_eyeLeftUD)
  i01_head_eyeY.sync(i01_head_eyeRightUD)
## sync the i2Head eyelids with the default i01.eyelids  
if runtime.isStarted('i01.head') and runtime.isStarted('i01.head.eyelidLeft') and runtime.isStarted('i01.head.eyelidRight') and runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidRightUpper'):
  i01_head_eyelidLeft.sync(i01_head_eyelidLeftUpper)
  i01_head_eyelidRight.sync(i01_head_eyelidRightUpper)
