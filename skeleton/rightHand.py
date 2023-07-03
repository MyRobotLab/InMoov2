# ##############################################################################
#            *** RIGHT HAND ***
# ##############################################################################

 
  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
isRightHandActivated=0
ThisSkeletonPart=RuningFolder+'config/skeleton_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

  isRightHandActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isRightHandActivated') 
  
except:
  errorSpokenFunc('CONFIGPARSERPROBLEM','right hand . config')
  pass    
 
# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isRightHandActivated==1 and (ScriptType=="RightSide" or ScriptType=="Full") or ScriptType=="Virtual":
  isRightHandActivated=1
  if RightPortIsConnected:
    i01_rightHand = Runtime.create("i01.rightHand", "InMoov2Hand")
    #i01_rightHand_startPeers()    
    i01_rightHand_thumb.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'thumb'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'thumb')) 
    i01_rightHand_index.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'index'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'index'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'index'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'index')) 
    i01_rightHand_majeure.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'majeure'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'majeure')) 
    i01_rightHand_ringFinger.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'ringFinger')) 
    i01_rightHand_pinky.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'pinky'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'pinky'))
    i01_rightHand_wrist.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'wrist'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'wrist'))
    
  
    #i01_rightHand_thumb.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'thumb'))
    #i01_rightHand_index.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'index'))
    #i01_rightHand_majeure.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'majeure'))
    #i01_rightHand_ringFinger.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'ringFinger'))
    #i01_rightHand_pinky.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'pinky'))
    #i01_rightHand_wrist.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'wrist'))
        

    i01_rightHand_thumb.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'thumb'))
    i01_rightHand_index.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'index'))
    i01_rightHand_majeure.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'majeure'))
    i01_rightHand_ringFinger.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'ringFinger'))
    i01_rightHand_pinky.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'pinky'))
    i01_rightHand_wrist.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'wrist'))

    i01_rightHand.startService()
    
    i01_rightHand_thumb.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'thumb'))
    i01_rightHand_index.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'index'))
    i01_rightHand_majeure.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'majeure'))
    i01_rightHand_ringFinger.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'ringFinger'))
    i01_rightHand_pinky.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'pinky'))
    i01_rightHand_wrist.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'wrist'))
    
    #i01.startRightHand(MyRightPort)

    i01_rightHand.rest()
    
    i01_rightHand_thumb.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'thumb'))
    i01_rightHand_index.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'index'))
    i01_rightHand_majeure.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'majeure'))
    i01_rightHand_ringFinger.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'ringFinger'))
    i01_rightHand_pinky.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'pinky'))
    i01_rightHand_wrist.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'wrist'))
    
  else:
    #we force parameter if arduino is off
    isRightHandActivated=0