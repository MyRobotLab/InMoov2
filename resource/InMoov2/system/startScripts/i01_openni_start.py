#########################################
# i01_openni_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)"

# create a openni
i01_openni = Runtime.start("i01.openni","OpenNi")
i01.speakBlocking(i01.localize("STARTINGOPENNI"))
enableOpenNi=True
