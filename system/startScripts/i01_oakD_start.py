#########################################
# i01_oakD_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

i01_oakD = runtime.start("i01.oakD","OakD")

if runtime.isStarted('i01.chatBot'):
    i01.invoke("publishEvent", "STARTED OAKD")
