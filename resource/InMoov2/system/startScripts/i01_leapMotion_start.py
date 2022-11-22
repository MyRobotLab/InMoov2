#########################################
# i01_leapMotion_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

i01_leap = runtime.start("i01.leap","LeapMotion")

if runtime.isStarted('i01.rightHand'):
    i01_leap.addLeapDataListener(i01_rightHand)
    i01_leap.startTracking()
    i01.info("starting tracking i01.rightHand")
elif runtime.isStarted('i01.leftHand'):
    i01_leap.addLeapDataListener(i01_leftHand)
    i01_leap.startTracking()
    i01.info("starting tracking i01.leftHand")
else:
    i01.warn("i01.rightHand or i01.leftHand needs to be started to start leap tracking!")
