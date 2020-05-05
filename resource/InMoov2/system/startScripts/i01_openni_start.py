#########################################
# i01_openni_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)"

# create a openni
i01.openni = Runtime.start("i01.openni","OpenNi")
#if isMouthActivated:
    #i01.speakBlocking(get("STARTINGOPENNI"))
    #i01.speakBlocking("STARTING OPENNI"))
  
i01.isOpenNiActivated = (True)

# we tell to the service what is going on
i01.broadcastState()