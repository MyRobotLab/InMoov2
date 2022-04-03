#########################################
# i01_headTracking_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

# create a pid
i01_pid = Runtime.start("i01.pid","Pid")
#set Kp, kd, ki kp = gain, how strong it react kd = how fast it react ki= take care of the sum of errors (differences between target and actual value) in the time
i01_pid.setPid("i01.head.rothead", 0.035, 0.01, 0.0)
i01_pid.setMode("i01.head.rothead", 1)
#set ControllerDirection means inverted = 1
i01_pid.setControllerDirection("i01.head.rothead", 0)
#set the range of the "correction"
i01_pid.setOutputRange("i01.head.rothead", -5, 5)

i01_pid.setPid("i01.head.neck", 0.035, 0.01, 0.0)
i01_pid.setMode("i01.head.neck", 1)
i01_pid.setControllerDirection("i01.head.neck", 0)
#set the range of the "correction"
i01_pid.setOutputRange("i01.head.neck", -5, 5)

#enablePid = True

# create a tracking
i01_headTracking = Runtime.start("i01.headTracking","Tracking")
i01_headTracking.attachCv("i01.opencv")
i01_headTracking.attachPan("i01.head.rothead")
i01_headTracking.attachTilt("i01.head.neck")
i01_headTracking.attachPid("i01.pid")
i01_headTracking.enable()

#enableTracking = True

#i01.startPeer('headTracking')