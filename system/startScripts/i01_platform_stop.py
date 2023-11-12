#########################################
# i01_oakD_stop.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware


runtime.release("i01.motorRight")
runtime.release("i01.motorLeft")

if runtime.isStarted('i01.chatBot'):
	i01.invoke("publishEvent", "STOPPED PLATFORM")
