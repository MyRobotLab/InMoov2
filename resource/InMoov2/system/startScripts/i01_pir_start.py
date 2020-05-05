#########################################
# i01_pir_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)"

# create a pir
i01.pir = Runtime.start("i01.pir","Pir")
#if isMouthActivated:
    #i01.speakBlocking("STARTING PIR")
#i01.isPirActivated = (True)

# we tell to the service what is going on
i01.broadcastState()