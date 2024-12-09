def startRadio(station):
    if runtime.isStarted("i01.audioPlayer"):
        audioPlayer = runtime.getService("i01.audioPlayer")
        audiocfg = audioPlayer.getConfig()
        print("Radio started")
        if audiocfg.stream == 0:
            audiocfg.stream = 1
            audioPlayer.save()
            audioPlayer.apply(audiocfg)
            audioPlayer.broadcastState()
        print(station)
        audioPlayer.playFile(station)

def stopRadio():
    if runtime.isStarted('i01.audioPlayer'):
        audioPlayer = runtime.getService('i01.audioPlayer')
        audioPlayer.stop()
        print("Radio stopped")
        audiocfg = audioPlayer.getConfig()
        if audiocfg.stream == 1:
            audiocfg.stream = 0
            audioPlayer.save()
            audioPlayer.apply(audiocfg)
            audioPlayer.broadcastState()