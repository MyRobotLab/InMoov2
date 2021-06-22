#########################################
# i01_controller3_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

# Every settings like limits / port number / controller are saved after initial use
# so you can share them between differents script 

# port = "/dev/ttyUSB0"
# port = "COM10"

# create a controller
i01_controller3 = Runtime.start("i01.controller3","Arduino")
isController3Activated=True

# initialize controller
# linux or macos -> i01.controller3.connect("/dev/ttyUSB0")
# print("connecting i01.controller3 to serial port")
# i01.controller3.connect(port)