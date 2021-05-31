# ##############################################################################
#            *** OPEN CV ***
# ##############################################################################


# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  

#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
global isOpenCvActivated

#FIXME
#i01.vision.setOpenCVenabled(ThisServicePartConfig.getboolean('MAIN', 'isOpenCvActivated'))
#isOpenCvActivated=i01.vision.openCVenabled

isOpenCvActivated=(ThisServicePartConfig.getboolean('MAIN', 'isOpenCvActivated'))

CameraIndex=ThisServicePartConfig.getint('MAIN', 'CameraIndex') 
DisplayRender=ThisServicePartConfig.get('MAIN', 'DisplayRender')

flipPicture=False
faceRecognizerActivated=True
try:
  flipPicture=ThisServicePartConfig.getboolean('MAIN', 'flipPicture')
  faceRecognizerActivated=ThisServicePartConfig.getboolean('MAIN', 'faceRecognizerActivated')
except:pass

streamerEnabled=ThisServicePartConfig.getboolean('MAIN', 'streamerEnabled')

#for noworky
log.info("D_OpenCv.config")
log.info("isOpenCvActivated : "+str(isOpenCvActivated))
log.info("DisplayRender : "+str(DisplayRender))
log.info("streamerEnabled : "+str(streamerEnabled))

#i01_vision.setOpenCVenabled(True)
#i01_vision.addPreFilter("Flip")
#i01_opencv.setCameraIndex(1)
#i01_opencv.setGrabberType("Sarxos")


# ##############################################################################
#                 SERVICE START
# ##############################################################################

if isOpenCvActivated:
  i01_opencv = Runtime.create("i01.opencv", "OpenCV")
  i01_opencv.setCameraIndex(CameraIndex)
  i01_opencv.setGrabberType(DisplayRender)
  i01_opencv = Runtime.start("i01.opencv", "OpenCV")
  i01.startOpenCV()
  if flipPicture:i01_opencv.addPreFilter("Flip")
  if not isOpenCvActivated:
    errorSpokenFunc('OPENCVNOWORKY','camera '+str(i01_opencv.getCameraIndex()))
  else:
    python.subscribe("i01.opencv", "publishRecognizedFace")
  

def onRecognizedFace(name):
  print name
  # robot reaction if recognized face ( todo beter reaction... )
  if isChatbotActivated:
    i01_chatBot.startSession(unicode(name,'utf-8'))
    i01_opencv.disableFilter("FaceRecognizer")
    i01_chatBot.getResponse("SYSTEM_SAY_HELLO")
