def evilLaugh1():
  i01_audioPlayer.playFile('resource/InMoov2/system/sounds/EvilLaugh01.mp3')

  #EYELIDS
  eyelidsClose()
  #EYEBROWS
  browsU()



  #UP
  if runtime.isStarted('i01.head') and runtime.isStarted('i01.leftArm') and runtime.isStarted('i01.rightArm') and runtime.isStarted('i01.leftHand') and runtime.isStarted('i01.rightHand') and runtime.isStarted('i01.torso'):
    i01_head_neck.moveTo(140)
    i01_head_rollNeck.moveTo(90)
    i01_head_jaw.moveTo(180)
    sleep(0.1)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    sleep(0.1)

    i01_head_neck.moveTo(140)
    i01_head_rollNeck.moveTo(90)
    sleep(0.1)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    sleep(0.1)

    i01_head_neck.moveTo(140)
    i01_head_rollNeck.moveTo(90)
    sleep(0.1)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    i01_head_jaw.moveTo(80)
    sleep(0.15)

    i01_head_neck.moveTo(150)
    i01_head_rollNeck.moveTo(90)
    sleep(0.15)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    sleep(0.15)

    i01_head_neck.moveTo(150)
    i01_head_rollNeck.moveTo(90)
    sleep(0.15)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    sleep(0.15)

    i01_head_neck.moveTo(150)
    i01_head_rollNeck.moveTo(90)
    sleep(0.15)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    i01_head_jaw.moveTo(180)
    sleep(0.15)

    i01_head_neck.moveTo(160)
    i01_head_rollNeck.moveTo(90)
    i01_leftArm_omoplate.moveTo(15)
    i01_rightArm_omoplate.moveTo(15)
    sleep(0.25)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    i01_leftArm_omoplate.moveTo(0)
    i01_rightArm_omoplate.moveTo(0)
    sleep(0.15)

    i01_head_neck.moveTo(150)
    i01_head_rollNeck.moveTo(90)
    sleep(0.15)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    sleep(0.15)

    i01_head_neck.moveTo(150)
    i01_head_rollNeck.moveTo(90)
    i01_head_jaw.moveTo(80)
    sleep(0.15)

    #STOMACH
    i01_torso_topStom.setSpeed(84)
    i01_torso_midStom.setSpeed(132)
    i01_torso_topStom.moveTo(60)
    i01_torso_midStom.moveTo(120)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    sleep(0.15)

    i01_head_neck.moveTo(180)
    i01_head_rollNeck.moveTo(90)
    i01_leftArm_omoplate.moveTo(15)
    i01_rightArm_omoplate.moveTo(15)
    sleep(0.25)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    i01_leftArm_omoplate.moveTo(0)
    i01_rightArm_omoplate.moveTo(0)
    sleep(0.2)

    i01_head_neck.moveTo(150)
    i01_head_rollNeck.moveTo(90)
    sleep(0.2)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    i01_head_jaw.moveTo(180)
    sleep(0.2)

    i01_head_neck.moveTo(160)
    i01_head_rollNeck.moveTo(90)
    i01_leftArm_omoplate.moveTo(15)
    i01_rightArm_omoplate.moveTo(15)
    sleep(0.2)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    i01_leftArm_omoplate.moveTo(0)
    i01_rightArm_omoplate.moveTo(0)
    sleep(0.2)

    i01_head_neck.moveTo(150)
    i01_head_rollNeck.moveTo(90)
    sleep(0.2)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    sleep(0.2)

    i01_head_neck.moveTo(150)
    i01_head_rollNeck.moveTo(90)
    sleep(0.2)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    i01_head_jaw.moveTo(80)
    sleep(0.2)

    #STOMACH
    i01_torso_topStom.moveTo(140)
    i01_torso_midStom.moveTo(60)

    ##################################

    #SHOULDER
    i01_leftArm_shoulder.moveTo(75)
    i01_rightArm_shoulder.moveTo(75)
    sleep(0.5)

    #BICEP
    i01_leftArm_bicep.moveTo(110)
    i01_rightArm_bicep.moveTo(100)
    #ROTATE
    i01_leftArm_rotate.moveTo(115)
    i01_rightArm_rotate.moveTo(115)
    sleep(0.7)

    #WRIST
    i01_rightHand_wrist.moveTo(30)
    i01_leftHand_wrist.moveTo(150)
    sleep(0.1)

    ######################

    i01_head_neck.moveTo(180)
    i01_head_rollNeck.moveTo(90)
    i01_leftArm_omoplate.moveTo(15)
    i01_rightArm_omoplate.moveTo(15)

    #SEMI CLOSED FINGERS
    i01_leftHand_thumb.moveTo(150)
    i01_leftHand_index.moveTo(120)
    i01_leftHand_majeure.moveTo(100)
    i01_leftHand_ringFinger.moveTo(100)
    i01_leftHand_pinky.moveTo(120)
    i01_rightHand_thumb.moveTo(130)
    i01_rightHand_index.moveTo(100)
    i01_rightHand_majeure.moveTo(120)
    i01_rightHand_ringFinger.moveTo(120)
    i01_rightHand_pinky.moveTo(120)
    sleep(0.12)

    i01_head_neck.moveTo(140)
    i01_head_rollNeck.moveTo(90)
    i01_leftArm_omoplate.moveTo(0)
    i01_rightArm_omoplate.moveTo(0)
    i01_head_jaw.moveTo(180)

    #FINGERS OPEN
    i01_leftHand_thumb.moveTo(0)
    i01_leftHand_index.moveTo(20)
    i01_leftHand_majeure.moveTo(20)
    i01_leftHand_ringFinger.moveTo(20)
    i01_leftHand_pinky.moveTo(20)
    i01_rightHand_thumb.moveTo(20)
    i01_rightHand_index.moveTo(20)
    i01_rightHand_majeure.moveTo(20)
    i01_rightHand_ringFinger.moveTo(20)
    i01_rightHand_pinky.moveTo(20)
    sleep(0.12)

    i01_head_neck.moveTo(160)
    i01_head_rollNeck.moveTo(90)
    i01_leftArm_omoplate.moveTo(15)
    i01_rightArm_omoplate.moveTo(15)

    #SEMI CLOSED FINGERS
    i01_leftHand_thumb.moveTo(150)
    i01_leftHand_index.moveTo(120)
    i01_leftHand_majeure.moveTo(100)
    i01_leftHand_ringFinger.moveTo(100)
    i01_leftHand_pinky.moveTo(120)
    i01_rightHand_thumb.moveTo(130)
    i01_rightHand_index.moveTo(100)
    i01_rightHand_majeure.moveTo(120)
    i01_rightHand_ringFinger.moveTo(120)
    i01_rightHand_pinky.moveTo(120)
    sleep(0.12)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    i01_leftArm_omoplate.moveTo(0)
    i01_rightArm_omoplate.moveTo(0)

    #FINGERS OPEN
    i01_leftHand_thumb.moveTo(0)
    i01_leftHand_index.moveTo(20)
    i01_leftHand_majeure.moveTo(20)
    i01_leftHand_ringFinger.moveTo(20)
    i01_leftHand_pinky.moveTo(20)
    i01_rightHand_thumb.moveTo(20)
    i01_rightHand_index.moveTo(20)
    i01_rightHand_majeure.moveTo(20)
    i01_rightHand_ringFinger.moveTo(20)
    i01_rightHand_pinky.moveTo(20)
    sleep(0.12)

    i01_head_neck.moveTo(150)
    i01_head_rollNeck.moveTo(90)
    i01_head_jaw.moveTo(80)
    #SEMI CLOSED FINGERS
    i01_leftHand_thumb.moveTo(150)
    i01_leftHand_index.moveTo(120)
    i01_leftHand_majeure.moveTo(100)
    i01_leftHand_ringFinger.moveTo(100)
    i01_leftHand_pinky.moveTo(120)
    i01_rightHand_thumb.moveTo(130)
    i01_rightHand_index.moveTo(100)
    i01_rightHand_majeure.moveTo(120)
    i01_rightHand_ringFinger.moveTo(120)
    i01_rightHand_pinky.moveTo(120)
    sleep(0.12)

    i01_head_neck.moveTo(130)
    i01_head_rollNeck.moveTo(90)
    #FINGERS OPEN
    i01_leftHand_thumb.moveTo(0)
    i01_leftHand_index.moveTo(20)
    i01_leftHand_majeure.moveTo(20)
    i01_leftHand_ringFinger.moveTo(20)
    i01_leftHand_pinky.moveTo(20)
    i01_rightHand_thumb.moveTo(20)
    i01_rightHand_index.moveTo(20)
    i01_rightHand_majeure.moveTo(20)
    i01_rightHand_ringFinger.moveTo(20)
    i01_rightHand_pinky.moveTo(20)
    sleep(0.12)

    i01_head_neck.moveTo(150)
    i01_head_rollNeck.moveTo(90)
    i01_leftArm_omoplate.moveTo(0)
    i01_rightArm_omoplate.moveTo(0)
    #SEMI CLOSED FINGERS
    i01_leftHand_thumb.moveTo(150)
    i01_leftHand_index.moveTo(120)
    i01_leftHand_majeure.moveTo(100)
    i01_leftHand_ringFinger.moveTo(100)
    i01_leftHand_pinky.moveTo(120)
    i01_rightHand_thumb.moveTo(130)
    i01_rightHand_index.moveTo(100)
    i01_rightHand_majeure.moveTo(120)
    i01_rightHand_ringFinger.moveTo(120)
    i01_rightHand_pinky.moveTo(120)
    sleep(0.12)

    i01_head_neck.moveTo(180)
    i01_head_rollNeck.moveTo(90)
    i01_head_jaw.moveTo(180)
    i01_leftArm_omoplate.moveTo(15)
    i01_rightArm_omoplate.moveTo(15)
    #FINGERS OPEN
    i01_leftHand_thumb.moveTo(0)
    i01_leftHand_index.moveTo(20)
    i01_leftHand_majeure.moveTo(20)
    i01_leftHand_ringFinger.moveTo(20)
    i01_leftHand_pinky.moveTo(20)
    i01_rightHand_thumb.moveTo(20)
    i01_rightHand_index.moveTo(20)
    i01_rightHand_majeure.moveTo(20)
    i01_rightHand_ringFinger.moveTo(20)
    i01_rightHand_pinky.moveTo(20)
    sleep(0.12)

    i01_head_neck.moveTo(150)
    i01_head_rollNeck.moveTo(90)
    i01_leftArm_omoplate.moveTo(0)
    i01_rightArm_omoplate.moveTo(0)
    #SEMI CLOSED FINGERS
    i01_leftHand_thumb.moveTo(150)
    i01_leftHand_index.moveTo(120)
    i01_leftHand_majeure.moveTo(100)
    i01_leftHand_ringFinger.moveTo(100)
    i01_leftHand_pinky.moveTo(120)
    i01_rightHand_thumb.moveTo(130)
    i01_rightHand_index.moveTo(100)
    i01_rightHand_majeure.moveTo(120)
    i01_rightHand_ringFinger.moveTo(120)
    i01_rightHand_pinky.moveTo(120)
    sleep(0.12)

    #STOMACH
    i01_torso_topStom.moveTo(90)
    i01_torso_midStom.moveTo(90)

    i01_head_neck.moveTo(180)
    i01_head_rollNeck.moveTo(90)
    i01_head_jaw.moveTo(80)
    i01_leftArm_omoplate.moveTo(15)
    i01_rightArm_omoplate.moveTo(15)
    #FINGERS OPEN
    i01_leftHand_thumb.moveTo(0)
    i01_leftHand_index.moveTo(20)
    i01_leftHand_majeure.moveTo(20)
    i01_leftHand_ringFinger.moveTo(20)
    i01_leftHand_pinky.moveTo(20)
    i01_rightHand_thumb.moveTo(20)
    i01_rightHand_index.moveTo(20)
    i01_rightHand_majeure.moveTo(20)
    i01_rightHand_ringFinger.moveTo(20)
    i01_rightHand_pinky.moveTo(20)
    sleep(0.25)

    i01_head_neck.moveTo(150)
    i01_head_rollNeck.moveTo(90)
    i01_leftArm_omoplate.moveTo(0)
    i01_rightArm_omoplate.moveTo(0)
    sleep(0.15)

    i01_head_neck.moveTo(180)
    i01_head_rollNeck.moveTo(90)
    i01_leftArm_omoplate.moveTo(10)
    i01_rightArm_omoplate.moveTo(10)
    sleep(0.25)

    i01_head_neck.moveTo(150)
    i01_head_rollNeck.moveTo(90)
    i01_leftArm_omoplate.moveTo(0)
    i01_rightArm_omoplate.moveTo(0)
    sleep(0.26)

    i01_head_neck.moveTo(180)
    i01_head_rollNeck.moveTo(90)
    i01_head_jaw.moveTo(180)
    i01_leftArm_omoplate.moveTo(10)
    i01_rightArm_omoplate.moveTo(10)
    sleep(0.15)

    i01_torso_topStom.setSpeed(500)
    i01_torso_midStom.setSpeed(500)
    i01.finishedGesture()
    ####ARM AND i01_head_neck RESET/REST####
    rest()
    #EYELID AND BROWS RESET/REST
    neutral()



