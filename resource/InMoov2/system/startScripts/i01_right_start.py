#########################################
# i01_right_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

# Every settings like limits / port number / controller are saved after initial use
# so you can share them between differents script 

# port = "/dev/ttyUSB0"
# port = "COM15"

# create a controller
i01_right = Runtime.start("i01.right","Arduino")
i01_right.setBoardMega()
isRightPortActivated=True
enableRightPort=True


# initialize controller
# linux or macos -> i01.right.connect("/dev/ttyUSB0")
# print("connecting i01.right to serial port")
# i01_right.connect(port)