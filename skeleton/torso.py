# ##############################################################################
#            *** TORSO ***
# ##############################################################################

 
  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
ThisSkeletonPart=RuningFolder+'config/skeleton_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

isTorsoActivated=0
try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

  isTorsoActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isTorsoActivated') 
  
  if isTorsoActivated or ScriptType=="Virtual":
    TorsoConnectedToArduinoPort=eval(ThisSkeletonPartConfig.get('MAIN', 'TorsoConnectedToArduino').replace("left","MyLeftPort").replace("right","MyRightPort"))
    TorsoConnectedToArduino=eval(ThisSkeletonPartConfig.get('MAIN', 'TorsoConnectedToArduino'))
    TorsoConnectedToArduinoPortBoardType=eval(ThisSkeletonPartConfig.get('MAIN', 'TorsoConnectedToArduino').replace("left","BoardTypeMyLeftPort").replace("right","BoardTypeMyRightPort"))
except:
  errorSpokenFunc('CONFIGPARSERPROBLEM','i01_torso_config')
  isTorsoActivated=0
  TorsoConnectedToArduino=""
  pass

# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isTorsoActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full" ) or ScriptType=="Virtual":
  isTorsoActivated=1
  if LeftPortIsConnected or RightPortIsConnected:
    i01_torso = Runtime.create("i01.torso","InMoov2Torso")
    #i01_torso.startPeers()
        
    i01_torso_topStom.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'topStom'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'topStom'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'topStom'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'topStom')) 
    i01_torso_midStom.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'midStom'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'midStom'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'midStom'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'midStom')) 
    i01_torso_lowStom.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'lowStom'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'lowStom'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'lowStom'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'lowStom')) 
    
    #i01_torso_topStom.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'topStom'))
    #i01_torso_midStom.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'midStom'))
    #i01_torso_lowStom.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'lowStom'))
    
    i01_torso_topStom.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'topStom'))
    i01_torso_midStom.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'midStom'))
    i01_torso_lowStom.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'lowStom'))

    i01_torso.startService()

    i01_torso_topStom.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'topStom'))
    i01_torso_midStom.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'midStom'))
    i01_torso_lowStom.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'lowStom'))

    
    #i01.startTorso(TorsoConnectedToArduinoPort)

    i01_torso.rest()
    
    i01_torso_topStom.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'topStom'))
    i01_torso_midStom.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'midStom'))
    i01_torso_lowStom.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'lowStom'))

       
  else:
    #we force parameter if arduino is off
    istorsoActivated=0
