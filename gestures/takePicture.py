def takePicture():
    opencv = runtime.start('i01.opencv', 'OpenCV')
    opencv.capture()
    audioPlayer = runtime.start('i01.audioPlayer', 'AudioFile')
    imageDisplay = runtime.start('i01.imageDisplay', 'ImageDisplay')
    photoFileName = i01_opencv.recordFrame()
    print(photoFileName)
    audioPlayer.playFile('resource/InMoov2/system/sounds/ShutterClik.mp3')
    sleep(1)
    imageDisplay.displayFullScreen(photoFileName)
    opencv.stopCapture()
    sleep(15)
    imageDisplay.closeAll()
    i01.finishedGesture()