#########################################
# i01_random_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

moveHeadRandomize = Runtime.start('moveHeadRandomize','Random')
if i01.isHeadActivated:
  #if i01.isOpenCvActivated:
    #if not i01_opencv.isTracking():
    moveHeadRandomize.addRandom(3000, 8000, 'i01.head','setSpeed', moveHeadRandomize.intRange(8, 25), moveHeadRandomize.intRange(8, 25), moveHeadRandomize.intRange(8, 25), moveHeadRandomize.intRange(8, 25), moveHeadRandomize.intRange(8, 25))
    moveHeadRandomize.addRandom(1000, 20000, 'i01.head','moveTo', moveHeadRandomize.intRange(80, 100), moveHeadRandomize.intRange(80, 100), moveHeadRandomize.intRange(80, 100), moveHeadRandomize.intRange(80, 100), moveHeadRandomize.intRange(80, 100))
    #else:
        #moveHeadRandomize.addRandom(1000, 20000, 'i01.head','setSpeed', moveHeadRandomize.intRange(8, 25), moveHeadRandomize.intRange(8, 25)) 
        #moveHeadRandomize.addRandom(1000, 20000, 'i01.head','moveTo', moveHeadRandomize.intRange(80, 100), moveHeadRandomize.intRange(80, 100))
    
moveBodyRandomize = Runtime.start('moveBodyRandomize','Random')
if i01.isLeftHandActivated:
    moveBodyRandomize.addRandom(3000, 8000, 'i01.leftHand','setSpeed', moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.leftHand','moveTo', moveBodyRandomize.intRange(10, 160), moveBodyRandomize.intRange(10, 160), moveBodyRandomize.intRange(10, 160), moveBodyRandomize.intRange(10, 160), moveBodyRandomize.intRange(10, 160), moveBodyRandomize.intRange(130, 175))
if i01.isRightHandActivated:
    moveBodyRandomize.addRandom(1000, 20000, 'i01.rightHand','setSpeed', moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25), moveBodyRandomize.intRange(8, 25))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.rightHand','moveTo', moveBodyRandomize.intRange(10, 160), moveBodyRandomize.intRange(10, 160), moveBodyRandomize.intRange(10, 160), moveBodyRandomize.intRange(10, 160), moveBodyRandomize.intRange(130, 175))
if i01.isLeftArmActivated:
    moveBodyRandomize.addRandom(1000, 20000, 'i01.leftArm','setSpeed', moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.leftArm','moveTo', moveBodyRandomize.intRange(0, 5), moveBodyRandomize.intRange(85, 95), moveBodyRandomize.intRange(25, 30), moveBodyRandomize.intRange(10, 15))
if i01.isRightArmActivated:
    moveBodyRandomize.addRandom(1000, 20000, 'i01.rightArm','setSpeed', moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.rightArm','moveTo', moveBodyRandomize.intRange(0, 5), moveBodyRandomize.intRange(85, 95), moveBodyRandomize.intRange(25, 30), moveBodyRandomize.intRange(10, 15))
if i01.isTorsoActivated:    
    moveBodyRandomize.addRandom(1000, 20000, 'i01.torso','setSpeed', moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5), moveBodyRandomize.intRange(2, 5))
    moveBodyRandomize.addRandom(1000, 20000, 'i01.torso','moveTo', moveBodyRandomize.intRange(85, 95), moveBodyRandomize.intRange(85, 95), moveBodyRandomize.intRange(85, 95))
