#########################################
# i01_oakD_stop.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware


runtime.release("i01.oakD")

if runtime.isStarted('i01.chatBot'):
	i01.invoke("publishEvent", "STOPPED OAKD")
