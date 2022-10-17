# ##############################################################################
#            *** LEFT HAND ***
# ##############################################################################



# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
isLeftHandActivated=0
ThisSkeletonPart=RuningFolder+'config/skeleton_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

  isLeftHandActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isLeftHandActivated') 
  
  
except:
  errorSpokenFunc('CONFIGPARSERPROBLEM','i01_leftHand_config')
  pass  
  
  
# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isLeftHandActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full") or ScriptType=="Virtual":
  isLeftHandActivated=1
  if LeftPortIsConnected:
    i01_leftHand = Runtime.create("i01.leftHand", "InMoov2Hand")
    #i01_leftHand.startPeers()
    i01_leftHand_thumb.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'thumb'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'thumb')) 
    i01_leftHand_index.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'index'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'index'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'index'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'index')) 
    i01_leftHand_majeure.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'majeure'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'majeure')) 
    i01_leftHand_ringFinger.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'ringFinger')) 
    i01_leftHand_pinky.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'pinky'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'pinky'))
    i01_leftHand_wrist.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'wrist'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'wrist'))
    
    #i01_leftHand_thumb.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'thumb'))
    #i01_leftHand_index.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'index'))
    #i01_leftHand_majeure.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'majeure'))
    #i01_leftHand_ringFinger.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'ringFinger'))
    #i01_leftHand_pinky.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'pinky'))
    #i01_leftHand_wrist.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'wrist'))
     
    i01_leftHand_thumb.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'thumb'))
    i01_leftHand_index.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'index'))
    i01_leftHand_majeure.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'majeure'))
    i01_leftHand_ringFinger.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'ringFinger'))
    i01_leftHand_pinky.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'pinky'))
    i01_leftHand_wrist.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'wrist'))

    i01_leftHand.startService()
    
    i01_leftHand_thumb.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'thumb'))
    i01_leftHand_index.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'index'))
    i01_leftHand_majeure.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'majeure'))
    i01_leftHand_ringFinger.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'ringFinger'))
    i01_leftHand_pinky.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'pinky'))
    i01_leftHand_wrist.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'wrist'))
 
    #i01.startLeftHand(MyLeftPort)
    
    #i01_leftHand_enableAutoEnable(1)
    i01_leftHand_thumb.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'thumb'))
    i01_leftHand_index.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'index'))
    i01_leftHand_majeure.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'majeure'))
    i01_leftHand_ringFinger.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'ringFinger'))
    i01_leftHand_pinky.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'pinky'))
    i01_leftHand_wrist.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'wrist'))

    i01_leftHand.rest()
    
  else:
    #we force parameter if arduino is off
    isleftHandActivated=0
