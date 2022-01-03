#########################################
# i01_ultrasonicRight_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)"

# create a UltrasonicSensor
i01_ultrasonicRight = Runtime.start('i01.ultrasonicRight', 'UltrasonicSensor')
i01_ultrasonicRight.setTriggerPin(64)
i01_ultrasonicRight.setEchoPin(63)
#i01_ultrasonicRight.attach("i01.right")
i01.startUltrasonicRight()

isUltrasonicRightActivated=True
enableUltrasonicRight=True
