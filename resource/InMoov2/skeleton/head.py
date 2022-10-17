# ##############################################################################
#            *** HEAD ***
# ##############################################################################


  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
isHeadActivated=0

#read current skeleton part config
ThisSkeletonPart=RuningFolder+'config/skeleton_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

  isHeadActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isHeadActivated') 
  MouthControlActivated=ThisSkeletonPartConfig.getboolean('MOUTHCONTROL', 'MouthControlActivated')
  AudioSignalProcessing=ThisSkeletonPartConfig.getboolean('AUDIOSIGNALPROCESSING', 'AudioSignalProcessing')
  AnalogPinFromSoundCard=ThisSkeletonPartConfig.getint('AUDIOSIGNALPROCESSING', 'AnalogPin')
  if ScriptType=="Virtual":AnalogPinFromSoundCard=3
  HowManyPollsBySecond=ThisSkeletonPartConfig.getint('AUDIOSIGNALPROCESSING', 'HowManyPollsBySecond')
  MouthControlJawMin=ThisSkeletonPartConfig.getint('MOUTHCONTROL', 'MouthControlJawMin')
  MouthControlJawMax=ThisSkeletonPartConfig.getint('MOUTHCONTROL', 'MouthControlJawMax')
  MouthControlJawTweak=ThisSkeletonPartConfig.getboolean('MOUTHCONTROL', 'MouthControlJawTweak')
  MouthControlJawdelaytime=ThisSkeletonPartConfig.getint('MOUTHCONTROL', 'MouthControlJawdelaytime')
  MouthControlJawdelaytimestop=ThisSkeletonPartConfig.getint('MOUTHCONTROL', 'MouthControlJawdelaytimestop')
  MouthControlJawdelaytimeletter=ThisSkeletonPartConfig.getint('MOUTHCONTROL', 'MouthControlJawdelaytimeletter')
  jawMIN=ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'jaw')
  jawMAX=ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'jaw')
  neckRest=ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'neck')
  rotheadRest=ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rothead')
  neckPin=ThisSkeletonPartConfig.getint('SERVO_PIN', 'neck')
except:
  isHeadActivated=0
  errorSpokenFunc('CONFIGPARSERPROBLEM','head.config')
  pass

isRollNeckActivated=ThisSkeletonPartConfig.getboolean('ROLLNECKSERVO', 'isRollNeckActivated') 
RollNeckArduino=ThisSkeletonPartConfig.get('ROLLNECKSERVO', 'RollNeckArduino')

# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isHeadActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full") or ScriptType=="Virtual":
  isHeadActivated=1
  if LeftPortIsConnected:
    i01_head = Runtime.create("i01.head","InMoov2Head")
    #head.startPeers()
    #map    
    i01_head_jaw.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'jaw'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'jaw')) 
    i01_head_eyeX.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'eyeX'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'eyeX'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'eyeX'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'eyeX')) 
    i01_head_eyeY.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'eyeY'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'eyeY'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'eyeY'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'eyeY')) 
    i01_head_neck.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'neck'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'neck'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'neck'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'neck')) 
    i01_head_rothead.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'rothead'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'rothead'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'rothead'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'rothead'))
    i01_head_rollNeck.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'rollneck'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'rollneck'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'rollneck'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'rollneck'))
  
    #maxspeed
    #i01_head_neck.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'neck'))
    #i01_head_rothead.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'rothead'))
    #i01_head_rollNeck.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'rollneck'))
     
    i01_head_jaw.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'jaw'))
    i01_head_eyeX.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'eyeX'))
    i01_head_eyeY.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'eyeY'))
    i01_head_neck.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'neck'))
    i01_head_rothead.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rothead'))
    i01_head_rollNeck.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rollneck'))

    i01_head_jaw.setPin(ThisSkeletonPartConfig.getint('SERVO_PIN', 'jaw'))
    i01_head_eyeX.setPin(ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyeX'))
    i01_head_eyeY.setPin(ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyeY'))
    i01_head_neck.setPin(ThisSkeletonPartConfig.getint('SERVO_PIN', 'neck'))
    i01_head_rothead.setPin(ThisSkeletonPartConfig.getint('SERVO_PIN', 'rothead'))
    i01_head_rollNeck.setPin(ThisSkeletonPartConfig.getint('SERVO_PIN', 'rollneck'))
  
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'jaw'):i01_head_jaw.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'eyeX'):i01_head_eyeX.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'eyeY'):i01_head_eyeY.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'neck'):i01_head_neck.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'rothead'):i01_head_rothead.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'rollneck'):i01_head_rollNeck.setInverted(True)

    #i01.startHead(MyLeftPort,BoardTypeMyLeftPort,ThisSkeletonPartConfig.getint('SERVO_PIN', 'neck'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'rothead'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyeX'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyeY'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'rollneck'))
    #i01.startHead(MyLeftPort)
    i01_head.startService()
    rollneck=i01_head_rollNeck
    
    #overide rollneck arduino
    try:
      RollNeckArduino=eval(RollNeckArduino)
    except:
      errorSpokenFunc('BADRDUINOCHOOSEN',', Roll Neck')
      isRollNeckActivated=0
      pass  
    
    if isRollNeckActivated:
      i01_head_rollNeck.detach(left)
      i01_head_rollNeck.attach(RollNeckArduino,ThisSkeletonPartConfig.getint('SERVO_PIN', 'rollNeck'),ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rollNeck'))
     
    rotheadEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'rothead')
    neckEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'neck')
    rollneckEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'rollneck')
    eyeXEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'eyeX')
    eyeYEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'eyeY')
    
    #i01_head.jaw.setMaxSpeed(500)

    i01_head.rest()
    
    i01_head_rothead.setAutoDisable(rotheadEnableAutoDisable)
    i01_head_neck.setAutoDisable(neckEnableAutoDisable)
    i01_head_rollNeck.setAutoDisable(rollneckEnableAutoDisable)
    i01_head_jaw.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'jaw'))
    i01_head_eyeX.setAutoDisable(eyeXEnableAutoDisable)
    i01_head_eyeY.setAutoDisable(eyeYEnableAutoDisable)
    
# ##############################################################################
#                 Software mouth control
# ##############################################################################    
    
    if MouthControlActivated==True and AudioSignalProcessing==False:
      i01_mouthControl = runtime.start("i01.mouthControl","MouthControl")
      #i01.startMouthControl(i01_head.jaw,i01_mouth)
      i01_mouthControl.setmouth(MouthControlJawMin,MouthControlJawMax)
      print "software mouthcontrol activation"
      if MouthControlJawTweak:i01_mouthControl.setDelays(MouthControlJawdelaytime, MouthControlJawdelaytimestop, MouthControlJawdelaytimeletter)
# ##############################################################################
#                 mouth control based on audio signal processing
# ##############################################################################  
    
    #please set aref
    if AudioSignalProcessing:
      i01.setMute(False)
      left.addListener("publishPinArray","python","publishMouthcontrolPinLeft")
      AudioSignalProcessing=False
      MouthControlActivated=False
      AudioSignalProcessingCalibration=1
      left.enablePin(AnalogPinFromSoundCard,HowManyPollsBySecond)
      i01.speakBlocking(i01.localize("MOUTHSYNCRONISATION"))
      
      
      AudioSignalProcessingCalibration=0
      maxAudioValue=maxAverage(AudioInputValues,10)
      AudioInputValues=[]
      AudioSignalProcessingCalibration=1
      sleep(3)
      AudioSignalProcessingCalibration=0
      minAudioValue = (sum(AudioInputValues) / len(AudioInputValues)) + 20
      left.disablePin(AnalogPinFromSoundCard)
      result=0
      #arduino dit not detect analog value
      if minAudioValue>50:
        i01.speakBlocking(i01.localize("MOUTHSYNCRONISATION")+str(AnalogPinFromSoundCard))
        result=1
      #arduino detect a poor value
      if result==0 and (maxAudioValue-minAudioValue<=255):
        i01_head_jaw.map(minAudioValue,maxAudioValue,jawMIN,jawMAX)
        AudioSignalProcessing=True
        i01.speakBlocking(i01.localize("MOUTHSYNCRONISATIONNOTPERFECT"))
      #arduino detect a good value  
      if result==0 and (maxAudioValue-minAudioValue>255):
        i01_head_jaw.map(minAudioValue,maxAudioValue,jawMIN,jawMAX)
        AudioSignalProcessing=True
        i01.speakBlocking(i01.localize("MOUTHSYNCRONISATIONOK"))
        
      print maxAudioValue,minAudioValue
      
   
  else:
    #we force parameter if arduino is off
    isHeadActivated=0
    MouthControlActivated=0
    
else:
  MouthControlActivated=0
