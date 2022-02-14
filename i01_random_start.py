#########################################
# i01_random_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

moveHeadRandomize = Runtime.start('moveHeadRandomize','Random')
if runtime.isStarted('i01.head'):
    if runtime.isStarted('i01.opencv'):
        if not runtime.isStarted('i01.headTracking'):
            moveHeadRandomize.addRandom(3000, 8000, 'i01.head.rothead','setSpeed', moveHeadRandomize.intRange(8, 25))
            moveHeadRandomize.addRandom(3000, 8000, 'i01.head.neck','setSpeed', moveHeadRandomize.intRange(8, 25))
            if not i01_head.rothead.isMoving():moveHeadRandomize.addRandom(1000, 20000, 'i01.head.rothead','moveTo', moveHeadRandomize.intRange(70, 120))
            if not i01_head_neck.isMoving():moveHeadRandomize.addRandom(1000, 20000, 'i01.head.neck','moveTo', moveHeadRandomize.intRange(80, 100))
        if not runtime.isStarted('i01.eyeTracking'):
            moveHeadRandomize.addRandom(3000, 8000, 'i01.head.eyeX','setSpeed', moveHeadRandomize.intRange(8, 25))
            moveHeadRandomize.addRandom(3000, 8000, 'i01.head.eyeY','setSpeed', moveHeadRandomize.intRange(8, 25))
            if not i01_head_eyeX.isMoving():moveHeadRandomize.addRandom(1000, 20000, 'i01.head.eyeX','moveTo', moveHeadRandomize.intRange(80, 100))
            if not i01_head_eyeY.isMoving():moveHeadRandomize.addRandom(1000, 20000, 'i01.head.eyeY','moveTo', moveHeadRandomize.intRange(80, 100))

    else:
        moveHeadRandomize.addRandom(3000, 8000, 'i01.head.rothead','setSpeed', moveHeadRandomize.intRange(8, 25))
        moveHeadRandomize.addRandom(3000, 8000, 'i01.head.neck','setSpeed', moveHeadRandomize.intRange(8, 25))
        moveHeadRandomize.addRandom(3000, 8000, 'i01.head.rollNeck','setSpeed', moveHeadRandomize.intRange(8, 25))
        moveHeadRandomize.addRandom(3000, 8000, 'i01.head.eyeX','setSpeed', moveHeadRandomize.intRange(8, 25))
        moveHeadRandomize.addRandom(3000, 8000, 'i01.head.eyeY','setSpeed', moveHeadRandomize.intRange(8, 25))
        if not i01_head_rothead.isMoving():moveHeadRandomize.addRandom(1000, 20000, 'i01.head.rothead','moveTo', moveHeadRandomize.intRange(70, 120))
        if not i01_head_neck.isMoving():moveHeadRandomize.addRandom(1000, 20000, 'i01.head.neck','moveTo', moveHeadRandomize.intRange(80, 100))
        if not i01_head_rollNeck.isMoving():moveHeadRandomize.addRandom(3000, 8000, 'i01.head.rollNeck','setSpeed', moveHeadRandomize.intRange(8, 25))
        if not i01_head_eyeX.isMoving():moveHeadRandomize.addRandom(1000, 20000, 'i01.head.eyeX','moveTo', moveHeadRandomize.intRange(80, 100))
        if not i01_head_eyeY.isMoving():moveHeadRandomize.addRandom(1000, 20000, 'i01.head.eyeY','moveTo', moveHeadRandomize.intRange(80, 100))
    
moveBodyRandomize = Runtime.start('moveBodyRandomize','Random')
if runtime.isStarted('i01.leftHand'):
    moveBodyRandomize.addRandom(3000, 8000, 'i01','setLeftHandSpeed', moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25))
    if not i01_leftHand_thumb.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.leftHand.thumb', 'moveTo', moveBodyRandomize.intRange(10, 60))
    if not i01_leftHand_index.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.leftHand.index', 'moveTo', moveBodyRandomize.intRange(10, 60))
    if not i01_leftHand_majeure.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.leftHand.majeure', 'moveTo', moveBodyRandomize.intRange(10, 60))
    if not i01_leftHand_ringFinger.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.leftHand.ringFinger', 'moveTo', moveBodyRandomize.intRange(10, 60))
    if not i01_leftHand_pinky.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.leftHand.pinky', 'moveTo', moveBodyRandomize.intRange(10, 60))
    if not i01_leftHand_wrist.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.leftHand.wrist', 'moveTo', moveBodyRandomize.intRange(85, 95))
if runtime.isStarted('i01.rightHand'):
    moveBodyRandomize.addRandom(1000, 20000, 'i01','setRightHandSpeed', moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25))
    if not i01_rightHand_thumb.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.rightHand.thumb', 'moveTo', moveBodyRandomize.intRange(10, 60))
    if not i01_rightHand_index.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.rightHand.index', 'moveTo', moveBodyRandomize.intRange(10, 60))
    if not i01_rightHand_majeure.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.rightHand.majeure', 'moveTo', moveBodyRandomize.intRange(10, 60))
    if not i01_rightHand_ringFinger.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.rightHand.ringFinger', 'moveTo', moveBodyRandomize.intRange(10, 60))
    if not i01_rightHand_pinky.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.rightHand.pinky', 'moveTo', moveBodyRandomize.intRange(10, 60))
    if not i01_rightHand_wrist.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.rightHand.wrist', 'moveTo', moveBodyRandomize.intRange(85, 95))
if runtime.isStarted('i01.leftArm'):
    moveBodyRandomize.addRandom(1000, 20000, 'i01','setLeftArmSpeed', moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5))
    if not i01_leftArm.bicep.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.leftArm.bicep','moveTo', moveBodyRandomize.intRange(0, 5))
    if not i01_leftArm.rotate.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.leftArm.rotate','moveTo', moveBodyRandomize.intRange(85, 95))
    if not i01_leftArm.shoulder.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.leftArm.shoulder','moveTo', moveBodyRandomize.intRange(25, 30))
    if not i01_leftArm.omoplate.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.leftArm.omoplate','moveTo', moveBodyRandomize.intRange(10, 15))
if runtime.isStarted('i01.rightArm'):
    moveBodyRandomize.addRandom(1000, 20000, 'i01','setRightArmSpeed', moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5))
    if not i01_rightArm.bicep.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.rightArm.bicep','moveTo', moveBodyRandomize.intRange(0, 5))
    if not i01_rightArm.rotate.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.rightArm.rotate','moveTo', moveBodyRandomize.intRange(85, 95))
    if not i01_rightArm.shoulder.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.rightArm.shoulder','moveTo', moveBodyRandomize.intRange(25, 30))
    if not i01_rightArm.omoplate.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.rightArm.omoplate','moveTo', moveBodyRandomize.intRange(10, 15))
if runtime.isStarted('i01.torso'):    
    moveBodyRandomize.addRandom(1000, 20000, 'i01','setTorsoSpeed', moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5))
    if not i01_topStom.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.topStom','moveTo', moveBodyRandomize.intRange(85, 95))
    if not i01_midStom.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.midStom','moveTo', moveBodyRandomize.intRange(85, 95))
    if not i01_lowStom.isMoving():moveBodyRandomize.addRandom(1000, 20000, 'i01.lowStom','moveTo', moveBodyRandomize.intRange(85, 95))