def takePicture():
    if runtime.isStarted('i01.opencv'):
        photoFileName = i01_opencv.recordFrame()
        print photoFileName
        if runtime.isStarted('imageDisplay'):
            imageDisplay = runtime.start("imageDisplay", "ImageDisplay")
            #sleep(3)
            i01_audioPlayer.playFile('resource/InMoov2/system/sounds/ShutterClik.mp3')
            #imageDisplay.display(photoFileName)
            imageDisplay.displayFullScreen(photoFileName)
            sleep(15)
            imageDisplay.closeAll()
        else:
            imageDisplay = runtime.start("imageDisplay", "ImageDisplay")
            sleep(3)
            i01_audioPlayer.playFile('resource/InMoov2/system/sounds/ShutterClik.mp3')
            sleep(1)
            #imageDisplay.display(photoFileName)
            imageDisplay.displayFullScreen(photoFileName)
            sleep(15)
            imageDisplay.closeAll()
    else:
        i01.cameraOn()
        if runtime.isStarted('imageDisplay'):
            photoFileName = i01_opencv.recordFrame()
            print photoFileName
            i01_audioPlayer.playFile('resource/InMoov2/system/sounds/ShutterClik.mp3')
            sleep(1)
            #imageDisplay.display(photoFileName)
            imageDisplay.displayFullScreen(photoFileName)
            sleep(15)
            imageDisplay.closeAll()
        else:
            imageDisplay = runtime.start("imageDisplay", "ImageDisplay")
            sleep(5)
            i01_audioPlayer.playFile('resource/InMoov2/system/sounds/ShutterClik.mp3')
            sleep(2)
            photoFileName = i01_opencv.recordFrame()
            print photoFileName
            sleep(1)
            #imageDisplay.display(photoFileName)
            imageDisplay.displayFullScreen(photoFileName)
            sleep(15)
