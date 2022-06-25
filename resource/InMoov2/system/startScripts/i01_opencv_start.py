#########################################
# i01_opencv_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

# create a opencv
i01_opencv = runtime.start("i01.opencv","OpenCV")
i01_opencv.setGrabberType("OpenCV")
i01_opencv.nativeViewer=False
i01_opencv.webViewer=True
i01.speakBlocking(i01.localize("STARTINGOPENCV"))
