#########################################
# i01_ultraSonicRight_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)"

# create a UltrasonicSensor
i01_ultraSonicRight = Runtime.start('i01.ultraSonicRight', 'UltrasonicSensor')
i01.speakBlocking(i01.localize("STARTINGULTRASONIC"))
isUltraSonicRightActivated=True
