# ##############################################################################
#            *** HEAD ***
# ##############################################################################


  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
isEyeLidsActivated=0  
#read current skeleton part config
ThisSkeletonPart=RuningFolder+'config/skeleton_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

  isEyeLidsActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isEyeLidsActivated')
  EyeLidsLeftActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'EyeLidsLeftActivated') 
  EyeLidsRightActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'EyeLidsRightActivated') 
  
  if (isEyeLidsActivated and (ScriptType=="RightSide" or ScriptType=="LeftSide" or ScriptType=="Full")) or ScriptType=="Virtual":
    EyeLidsConnectedToArduino=eval(ThisSkeletonPartConfig.get('MAIN', 'EyeLidsConnectedToArduino'))
except:
  isEyeLidsActivated=0
  errorSpokenFunc('CONFIGPARSERPROBLEM','eyelids . config')
  pass

  
# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if (isEyeLidsActivated and (ScriptType=="RightSide" or ScriptType=="LeftSide" or ScriptType=="Full")):
  if LeftPortIsConnected or RightPortIsConnected:
    i01_eyelids = Runtime.create("i01.eyelids","InMoov2Eyelids")
    #eyelids.startPeers()        
    i01_eyelids_eyelidLeft.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'eyelidLeft'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'eyelidLeft'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'eyelidLeft'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'eyelidLeft')) 
    i01_eyelids_eyelidRight.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'eyelidRight'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'eyelidRight'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'eyelidRight'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'eyelidRight')) 
    #i01_eyelids_eyelidLeft.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'eyelidLeft'))
    #i01_eyelids_eyelidRight.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'eyelidRight'))
    i01_eyelids_eyelidLeft.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'eyelidLeft'))
    i01_eyelids_eyelidRight.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'eyelidRight'))
    i01_eyelids_eyelidLeft.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'eyelidLeft'))
    i01_eyelids_eyelidRight.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'eyelidRight'))
    i01.startEyelids(EyeLidsConnectedToArduino,ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyelidLeft'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyelidRight'))
    i01_eyelids_eyelidLeft.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'eyelidRight'))
    i01_eyelids_eyelidRight.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'eyelidRight'))
    eyelids.autoBlink(True)
  else:
    #we force parameter if arduino is off
    isEyeLidsActivated=0
