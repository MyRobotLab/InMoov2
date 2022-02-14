#########################################
# i01_eyesTracking_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

# create a pid
i01_eyesPid = Runtime.start("i01.eyesPid","Pid")
#set Kp, kd, ki kp = gain, how strong it react kd = how fast it react ki= take care of the sum of errors (differences between target and actual value) in the time
i01_eyesPid.setPid("i01.head.eyeX", 0.035, 0.01, 0.0)
i01_eyesPid.setMode("i01.head.eyeX", 1)
#set ControllerDirection means inverted = 1
i01_eyesPid.setControllerDirection("i01.head.eyeX", 0)
#set the range of the "correction"
i01_eyesPid.setOutputRange("i01.head.eyeX", -5, 5)

i01_eyesPid.setPid("i01.head.eyeY", 0.035, 0.01, 0.0)
i01_eyesPid.setMode("i01.head.eyeY", 1)
i01_eyesPid.setControllerDirection("i01.head.eyeY", 0)
#set the range of the "correction"
i01_eyesPid.setOutputRange("i01.head.eyeY", -5, 5)


# create a tracking
i01_eyesTracking = Runtime.start("i01.eyesTracking","Tracking")
i01_eyesTracking.attachCv("i01.opencv")
i01_eyesTracking.attachPan("i01.head.eyeX")
i01_eyesTracking.attachTilt("i01.head.eyeY")
i01_eyesTracking.attachPid("i01.eyesPid")
i01_eyesTracking.enable()



