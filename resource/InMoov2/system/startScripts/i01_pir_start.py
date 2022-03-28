#########################################
# i01_pir_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

# create a pir
i01_pir = Runtime.start("i01.pir","Pir")
if runtime.isStarted("i01.left") or runtime.isStarted("i01.right"):
    i01_pir.setPin("23")
    try:
        i01_pir.attach("i01.left")
        enablePir=True
    except:
        pass
    try:
        i01_pir.attach("i01.right")
        enablePir=True
    except:
        pass   
else:
    i01.info("Pir needs a controller to attach to")
