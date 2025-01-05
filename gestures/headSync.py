def headSync():
  ## If you want to sync the second servo of rollNeck
  i01_head_rollNeck2 = runtime.start('i01.head.rollNeck2', 'Servo')
  if runtime.isStarted('i01.head'):
    ## if you have started a second rollNeck2 servo and wish to sync it with rollNeck (1)
    i01_head_rollNeck.sync(i01_head_rollNeck2)
    ## if you have built the i2Eyes and need to sync them with the original eyes.
    i01_head_eyeX.sync(i01_head_eyeLeftLR)
    i01_head_eyeX.sync(i01_head_eyeRightLR)
    i01_head_eyeY.sync(i01_head_eyeLeftUD)
    i01_head_eyeY.sync(i01_head_eyeRightUD)