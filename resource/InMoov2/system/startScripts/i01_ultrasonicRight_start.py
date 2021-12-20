#########################################
# i01_ultrasonicRight_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)"

# create a UltrasonicSensor
i01_ultrasonicRight = Runtime.start('i01.ultrasonicRight', 'UltrasonicSensor')
i01.speakBlocking(i01.localize("STARTINGULTRASONICRIGHT"))
isUltrasonicRightActivated=True
enableUltrasonicRight=True
