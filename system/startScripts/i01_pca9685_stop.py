#########################################
# i01_pca9685_stop.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True) 

# release service pca9685
runtime.release('i01.pca9685')
if runtime.isStarted('i01.chatBot'):
   i01_chatBot.getResponse("SYSTEM_EVENT STOPPED pca9685")