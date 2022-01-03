#########################################
# i01_ultrasonicRight_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)"

# create a UltrasonicSensor
i01_ultrasonicLeft = Runtime.start('i01.ultrasonicLeft', 'UltrasonicSensor')
i01_ultrasonicLeft.setTriggerPin(64)
i01_ultrasonicLeft.setEchoPin(63)
#i01_ultrasonicLeft.attach("i01.left")
i01.startUltrasonicLeft()


enableUltrasonicLeft=True
isUltrasonicLeftActivated=True
