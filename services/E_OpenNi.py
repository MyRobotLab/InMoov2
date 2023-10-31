# ##############################################################################
#            *** KINECT *** >> TODO MIGRATE TO INMOOV SERVICE
# ##############################################################################


# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  

# ##############################################################################
#                 SERVICE START
# ##############################################################################

openNiShouldersOffset=30.0
openNiLeftShoulderInverted=False
openNiRightShoulderInverted=False

def openNiInit():
  if runtime.isStarted('i01.openni'):
    if runtime.isStarted('i01.leftArm'):
      i01_leftArm_shoulder.setRest(openNiShouldersOffset)
      if openNiLeftShoulderInverted==1:
        i01_leftArm_shoulder.setInverted(True)
    if runtime.isStarted('i01.rightArm'):
      i01_rightArm_shoulder.setRest(openNiShouldersOffset)
      if openNiRightShoulderInverted==1:
        i01_rightArm_shoulder.setInverted(True)
    i01_openni.capture()
    #worky open ni kinect detection
    #while not i01.RobotIsOpenNiCapturing:
    if runtime.isStarted('i01.fsm'):
      timeout=0
      while not i01_fsm.getCurrent()=="isTracking":
        sleep(1)
        timeout+=1
        if timeout>7:break
  

def openNiStop():
  if runtime.isStarted('i01.openni'):
    if runtime.isStarted('i01.leftArm'):
      i01_leftArm_shoulder.setRest(i01_leftArm_shoulder.getConfig().rest)
      if openNiLeftShoulderInverted==0:
        i01_leftArm_shoulder.setInverted(False)
    if runtime.isStarted('i01.rightArm'):
      i01_rightArm_shoulder.setRest(i01_rightArm_shoulder.getConfig().rest)
      if openNiRightShoulderInverted==0:
        i01_rightArm_shoulder.setInverted(False)
    if runtime.isStarted('i01.fsm'):
      i01_fsm.fire("awake")

# if runtime.isStarted('i01.openni'):
#   if i01_openni.getConfig().autoStart==1:
#     openNIInit()
      
#   else:
#     openni.stopCapture()
