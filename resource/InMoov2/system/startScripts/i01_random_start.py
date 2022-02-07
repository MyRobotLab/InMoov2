#########################################
# i01_random_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware

moveHeadRandomize = Runtime.start('moveHeadRandomize','Random')
if i01.isHeadActivated:
    if not i01_opencv.isCapturing():
      moveHeadRandomize.addRandom(1000, 20000, 'i01.head.rothead', 'moveTo', moveHeadRandomize.intRange(50, 130))
      moveHeadRandomize.addRandom(1000, 20000, 'i01.head.neck', 'moveTo', moveHeadRandomize.intRange(35, 165))
      moveHeadRandomize.addRandom(1000, 20000, 'i01.head.rollNeck', 'moveTo', moveHeadRandomize.intRange(35, 165))
