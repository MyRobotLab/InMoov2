#########################################
# i01_opencv_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

# create a opencv
i01_opencv = Runtime.start("i01.opencv","OpenCV")
#i01_opencv.setGrabberType("org.bytedeco.javacv.OpenCVFrameGrabber")
i01_opencv.setGrabberType("OpenCV")
i01.speakBlocking(i01.localize("STARTINGOPENCV"))
isOpenCVActivated=True