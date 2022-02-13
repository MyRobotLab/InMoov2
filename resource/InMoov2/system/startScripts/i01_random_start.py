#########################################
# i01_random_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

moveHeadRandomize = Runtime.start('moveHeadRandomize','Random')
if i01.isHeadActivated:
  #if i01.isOpenCvActivated:
    #if not i01_opencv.isTracking():
    moveHeadRandomize.addRandom(3000, 8000, 'i01.head.rothead','setSpeed', moveHeadRandomize.intRange(8, 25))
    moveHeadRandomize.addRandom(1000, 20000, 'i01.head.rothead','moveTo', moveHeadRandomize.intRange(70, 120))
    moveHeadRandomize.addRandom(3000, 8000, 'i01.head.neck','setSpeed', moveHeadRandomize.intRange(8, 25))
    moveHeadRandomize.addRandom(1000, 20000, 'i01.head.neck','moveTo', moveHeadRandomize.intRange(80, 100))
    moveHeadRandomize.addRandom(3000, 8000, 'i01.head.rollNeck','setSpeed', moveHeadRandomize.intRange(8, 25))
    moveHeadRandomize.addRandom(1000, 20000, 'i01.head.rollNeck','moveTo', moveHeadRandomize.intRange(80, 100))
    moveHeadRandomize.addRandom(3000, 8000, 'i01.head.eyeX','setSpeed', moveHeadRandomize.intRange(8, 25))
    moveHeadRandomize.addRandom(1000, 20000, 'i01.head.eyeX','moveTo', moveHeadRandomize.intRange(80, 100))
    moveHeadRandomize.addRandom(3000, 8000, 'i01.head.eyeY','setSpeed', moveHeadRandomize.intRange(8, 25))
    moveHeadRandomize.addRandom(1000, 20000, 'i01.head.eyeY','moveTo', moveHeadRandomize.intRange(80, 100))
    #else:
        #moveHeadRandomize.addRandom(1000, 20000, 'i01','head','setSpeed', moveHeadRandomize.intRange(8, 25), moveHeadRandomize.intRange(8, 25)) 
        #moveHeadRandomize.addRandom(1000, 20000, 'i01','moveHead', moveHeadRandomize.intRange(80, 100), moveHeadRandomize.intRange(80, 100))
    
moveBodyRandomize = Runtime.start('moveBodyRandomize','Random')
if i01.isLeftHandActivated:
    moveBodyRandomize.addRandom(3000, 8000, 'i01','setLeftHandSpeed', moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.leftHand.thumb', 'moveTo', moveBodyRandomize.intRange(10, 60))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.leftHand.index', 'moveTo', moveBodyRandomize.intRange(10, 60))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.leftHand.majeure', 'moveTo', moveBodyRandomize.intRange(10, 60))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.leftHand.ringFinger', 'moveTo', moveBodyRandomize.intRange(10, 60))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.leftHand.pinky', 'moveTo', moveBodyRandomize.intRange(10, 60))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.leftHand.wrist', 'moveTo', moveBodyRandomize.intRange(85, 95))
if i01.isRightHandActivated:
    moveBodyRandomize.addRandom(1000, 20000, 'i01','setRightHandSpeed', moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.rightHand.thumb', 'moveTo', moveBodyRandomize.intRange(10, 60))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.rightHand.index', 'moveTo', moveBodyRandomize.intRange(10, 60))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.rightHand.majeure', 'moveTo', moveBodyRandomize.intRange(10, 60))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.rightHand.ringFinger', 'moveTo', moveBodyRandomize.intRange(10, 60))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.rightHand.pinky', 'moveTo', moveBodyRandomize.intRange(10, 60))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.rightHand.wrist', 'moveTo', moveBodyRandomize.intRange(85, 5))
if i01.isLeftArmActivated:
    moveBodyRandomize.addRandom(1000, 20000, 'i01','setLeftArmSpeed', moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.leftArm.bicep','moveTo', moveBodyRandomize.intRange(0, 5))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.leftArm.rotate','moveTo', moveBodyRandomize.intRange(85, 95))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.leftArm.shoulder','moveTo', moveBodyRandomize.intRange(25, 30))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.leftArm.omoplate','moveTo', moveBodyRandomize.intRange(10, 15))

if i01.isRightArmActivated:
    moveBodyRandomize.addRandom(1000, 20000, 'i01','setRightArmSpeed', moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.rightArm.bicep','moveTo', moveBodyRandomize.intRange(0, 5))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.rightArm.rotate','moveTo', moveBodyRandomize.intRange(85, 95))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.rightArm.shoulder','moveTo', moveBodyRandomize.intRange(25, 30))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.rightArm.omoplate','moveTo', moveBodyRandomize.intRange(10, 15))
if i01.isTorsoActivated:    
    moveBodyRandomize.addRandom(1000, 20000, 'i01','setTorsoSpeed', moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.topStom','moveTo', moveBodyRandomize.intRange(85, 95))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.midStom','moveTo', moveBodyRandomize.intRange(85, 95))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.lowStom','moveTo', moveBodyRandomize.intRange(85, 95))