#########################################
# i01_pir_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

# create a pir
i01_pir = Runtime.start("i01.pir","Pir")
i01_pir.setPin("23")
i01.startPir()
enablePir=True
