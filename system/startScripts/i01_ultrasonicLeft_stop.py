#########################################
# i01_ultrasonicLeft_stop.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)"

# stop a UltrasonicSensor
Runtime.releaseService('i01.ultrasonicLeft')
i01.speakBlocking(i01.localize("STOPULTRASONIC"))
enableUltrasonicLeft=False
