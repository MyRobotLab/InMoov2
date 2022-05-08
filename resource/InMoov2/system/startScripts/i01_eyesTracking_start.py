#########################################
# i01_eyesTracking_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

if not runtime.isStarted('i01.pid'):
    # create a pid
    i01_pid = Runtime.start("i01.pid","Pid")
    #set Kp, kd, ki kp = gain, how strong it react kd = how fast it react ki= take care of the sum of errors (differences between target and actual value) in the time
    i01_pid.setPid("i01.head.eyeX", 35.0, 1.0, 0.0)
    i01_pid.setMode("i01.head.eyeX", 1)
    #set ControllerDirection means inverted = 1
    i01_pid.setControllerDirection("i01.head.eyeX", 0)
    #set the range of the "correction"
    i01_pid.setOutputRange("i01.head.eyeX", -5, 5)

    i01_pid.setPid("i01.head.eyeY", 35.0, 1.0, 0.0)
    i01_pid.setMode("i01.head.eyeY", 1)
    i01_pid.setControllerDirection("i01.head.eyeY", 0)
    #set the range of the "correction"
    i01_pid.setOutputRange("i01.head.eyeY", -5, 5)

else:
    # create a tracking
    i01_eyesTracking = Runtime.start("i01.eyesTracking","Tracking")
    i01_eyesTracking.attachCv("i01.opencv")
    i01_eyesTracking.attachPan("i01.head.eyeX")
    i01_eyesTracking.attachTilt("i01.head.eyeY")
    i01_eyesTracking.attachPid("i01.pid")
    i01_eyesTracking.enable()
