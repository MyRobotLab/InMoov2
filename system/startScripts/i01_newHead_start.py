#########################################
# i01_newHead_start.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

## start the eyes
i01_head_eyeLeftUD = runtime.start('i01.head.eyeLeftUD','Servo')
i01_head_eyeLeftLR = runtime.start('i01.head.eyeLeftLR','Servo')
i01_head_eyeLeftUD = runtime.start('i01.head.eyeLeftUD','Servo')
i01_head_eyeRightUD = runtime.start('i01.head.eyeRightUD','Servo')
i01_head_eyeRightLR = runtime.start('i01.head.eyeRightLR','Servo')

## sync the eyes with the default i01.eyes
if runtime.isStarted('i01.head'):
  i01_head_eyeX.sync(i01_head_eyeLeftLR)
  i01_head_eyeX.sync(i01_head_eyeRightLR)
  i01_head_eyeY.sync(i01_head_eyeLeftUD)
  i01_head_eyeY.sync(i01_head_eyeRightUD)

## start the eyelids
i01_head_eyelidLeftUpper = runtime.start('i01.head.eyelidLeftUpper','Servo')
i01_head_eyelidLeftLower = runtime.start('i01.head.eyelidLeftLower','Servo')
i01_head_eyelidRightUpper = runtime.start('i01.head.eyelidRightUpper','Servo')
i01_head_eyelidRightLower = runtime.start('i01.head.eyelidRightLower','Servo')

## start the default i01.eyelids
i01_head_eyelidLeft = runtime.start('i01.head.eyelidLeft','Servo')
i01_head_eyelidRight = runtime.start('i01.head.eyelidRight','Servo')

## sync the upper eyelids with the default i01.head.eyelids
if runtime.isStarted('i01.head.eyelidLeft') and runtime.isStarted('i01.head.eyelidRight'):
  i01_head_eyelidLeft.sync(i01_head_eyelidLeftUpper)
  i01_head_eyelidRight.sync(i01_head_eyelidRightUpper)

## start the eyebrows
i01_head_eyeBrowRight = runtime.start('i01.head.eyeBrowRight','Servo')
i01_head_eyeBrowLeft = runtime.start('i01.head.eyeBrowLeft','Servo')

## start the cheeks
i01_head_cheekRight = runtime.start('i01.head.cheekRight','Servo')
i01_head_cheekLeft = runtime.start('i01.head.cheekLeft','Servo')

## start the upper lip
i01_head_upperLip = runtime.start('i01.head.upperLip','Servo')

## start the for head
i01_head_forheadRight = runtime.start('i01.head.forheadRight','Servo')
i01_head_forheadLeft = runtime.start('i01.head.forheadLeft','Servo')
