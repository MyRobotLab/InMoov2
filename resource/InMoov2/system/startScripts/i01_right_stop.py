#########################################
# i01_right_stop.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

# Every settings like limits / port number / controller are saved after initial use
# so you can share them between differents script 

# port = "/dev/ttyUSB0"
# port = "COM15"

# release a servo controller and a servo
Runtime.releaseService("i01.right")

# we tell to the service what is going on 
# i01.broadcastState()