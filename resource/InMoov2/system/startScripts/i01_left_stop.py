#########################################
# i01_left_stop.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

# Every settings like limits / port number / controller are saved after initial use
# so you can share them between differents script 

# port = "/dev/ttyUSB0"
# port = "COM10"

# release a servo controller and a servo
Runtime.releaseService("i01.left")
enableLeftPort=False
