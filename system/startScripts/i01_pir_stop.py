#########################################
# i01_pir_stop.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)"

# stop a pir
Runtime.releaseService('i01.pir')
i01.speakBlocking(i01.localize("STOPPIR"))
isPirActivated=False