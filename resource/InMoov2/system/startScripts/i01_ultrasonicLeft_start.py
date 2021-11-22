#########################################
# i01_ultrasonicRight_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)"

# create a UltrasonicSensor
i01_ultrasonicLeft = Runtime.start('i01.ultrasonicLeft', 'UltrasonicSensor')
i01.speakBlocking(i01.localize("STARTINGULTRASONIC"))
enableUltrasonicLeft=True
