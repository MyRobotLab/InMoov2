#########################################
# i01_openni_stop.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)"

# release a openni
Runtime.releaseService("i01.openni")
i01.speakBlocking(i01.localize("STOPOPENNI"))
isOpenNiActivated=False

# we tell to the service what is going on 
# i01.broadcastState()