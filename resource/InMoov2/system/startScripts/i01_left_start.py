#########################################
# i01_left_start.py
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
i01_left = runtime.start("i01.left","Arduino")
#i01_left.setBoardMega()
enableLeftPort=True


# initialize controller
# linux or macos -> i01.left.connect("/dev/ttyUSB0")
# print("connecting i01.left to serial port")
# i01.left.connect(port)