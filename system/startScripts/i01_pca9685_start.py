#########################################
# i01_pca9685_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

i01_pca9685 = runtime.start("i01.pca9685","Adafruit16CServoDriver")
if runtime.isStarted('i01.left'):
    #i01_pca9685.setController('i01.left')
    i01_pca9685.setBus('0')
    i01_pca9685.save()
    i01_pca9685.attach('i01.left')
else:
    runtime.warn('i01.left not started')
if runtime.isStarted('i01.chatBot'):
    i01.invoke("publishEvent", "STARTED PCA9685")
