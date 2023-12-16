#########################################
# i01_platform_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

i01_motorRight = runtime.start("i01.motorRight","MotorDualPwm")
i01_motorLeft = runtime.start("i01.motorLeft","MotorDualPwm")


if runtime.isStarted('i01.controller3'):
  i01_motorRight.setPwmPins(10,11)
  #i01_motorRight.setMap(-100,100,0,255)
  i01_motorRight.attach('i01.controller3')
  i01_motorLeft.setPwmPins(12,13)
  #i01_motorLeft.setMap(-100,100,0,255)
  i01_motorLeft.attach('i01.controller3')

if runtime.isStarted('i01.chatBot'):
    i01.invoke("publishEvent", "STARTED PLATFORM")
