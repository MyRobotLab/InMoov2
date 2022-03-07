# -- coding: utf-8 --
# ##############################################################################
#                 ultrasonic Sensor FILE
# ##############################################################################


#parse config
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
trigLeftPin=ThisServicePartConfig.getint('MAIN', 'trigLeftPin')
echoLeftPin=ThisServicePartConfig.getint('MAIN', 'echoLeftPin')
ultrasonicLeftArduino=ThisServicePartConfig.get('MAIN', 'ultrasonicLeftArduino')
ultrasonicLeftActivated=ThisServicePartConfig.getboolean('MAIN', 'ultrasonicLeftActivated')

trigRightPin=ThisServicePartConfig.getint('MAIN', 'trigRightPin')
echoRightPin=ThisServicePartConfig.getint('MAIN', 'echoRightPin')
ultrasonicRightArduino=ThisServicePartConfig.get('MAIN', 'ultrasonicRightArduino')
ultrasonicRightActivated=ThisServicePartConfig.getboolean('MAIN', 'ultrasonicRightActivated')

if ultrasonicRightActivated:
  ultrasonicRight = Runtime.start("ultrasonicRight", "UltrasonicSensor")
  
  try:
    ultrasonicRightArduino=eval(ThisServicePartConfig.get('MAIN', 'ultrasonicRightArduino'))
    ultrasonicRight.attach(ultrasonicRightArduino, trigRightPin, echoRightPin)
    i01.ultrasonicSensor=ultrasonicRight
    i01.speakBlocking(i01.localize("STARTINGULTRASONIC"))
    # range can also be retreieved in a blocking call
    print "ultrasonicRight test is: ", i01.getultrasonicRightDistance()
  except:
    errorSpokenFunc('BADRDUINOCHOOSEN','ultra sonic Sensor Right')
    ultrasonicRightActivated=False
    pass

if ultrasonicLeftActivated:
  ultrasonicLeft = Runtime.start("ultrasonicLeft", "UltrasonicSensor")
  
  try:
    ultrasonicLeftArduino=eval(ThisServicePartConfig.get('MAIN', 'ultrasonicLeftArduino'))
    ultrasonicLeft.attach(ultrasonicLeftArduino, trigLeftPin, echoLeftPin)
    i01.ultrasonicSensor=ultrasonicLeft
    i01.speakBlocking(i01.localize("STARTINGULTRASONIC"))
    # range can also be retreieved in a blocking call
    print "ultrasonicLeft test is: ", i01.getultrasonicLeftDistance()
  except:
    errorSpokenFunc('BADRDUINOCHOOSEN','ultra sonic Sensor Left')
    ultrasonicLeftActivated=False
    pass
