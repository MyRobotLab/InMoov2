#########################################
# 1_AudioFile.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# -- coding: utf-8 --

if startupSound==True:
    i01_audioPlayer = runtime.start('i01.audioPlayer','AudioFile')
    i01_audioPlayer.playFile('resource/InMoov2/system/sounds/startupsound.mp3', False)

def initAudioPlayer():
  musicPath = audioPlayer.getConfig()

def searchPlay(song):
    if runtime.isStarted('i01.chatBot'):
        if runtime.isStarted('i01.audioPlayer'):
            initAudioPlayer()
            if os.path.exists(musicPath):
                    global liste
                    global pointeur
                    f = open(musicPath, 'r')
                    liste = f.readlines()
                    #Remove the first 11 elements of the list
                    del liste[0:11]
                    i=0
                    flag =0
                    # iteration on the list with set up of the chaine
                    while i <= len(liste)-2 :  
                        var = "".join(liste[i][4:]).rstrip('\n')
                        if song.lower() in var :
                            i01_audioPlayer.play(var)
                            pointeur = i
                            flag = 1
                            print(var+" Song : "+str(pointeur))
                        i=i+1
                    if flag == 0 :
                        i01_chatBot.getResponse("DO_NOT_HAVE_SONG")
                    else:
                        i01_chatBot.getResponse("NEXT_SONG")
                    f.close()
            else:
                i01_chatBot.getResponse("DO_NOT_HAVE_PLAYLIST")
        else :
            i01.speakBlocking(i01.localize("STARTINGAUDIOPLAYER"))
            i01_AudioPlayer = runtime.start('i01.audioPlayer','AudioFile')
    else:
        i01.warn("i01.chatBot needs to be started")

def nextPlay():
    if runtime.isStarted('i01.chatBot'):
        if runtime.isStarted('i01.audioPlayer'):
            initAudioPlayer()
            global pointeur 
            pointeur = pointeur + 1
            i01_audioPlayer.stop()
            var = "".join(liste[pointeur][4:]).rstrip('\n')
            if 'mp3' in var :
                i01_audioPlayer.play(var)
                print(var+" Song : "+str(pointeur))
            else:
                i01_chatBot.getResponse("END_PLAYLIST")
                pointeur = -1
                i01_audioPlayer.stop()
                i01_chatBot.getResponse("SYSTEM_NEXT_SONG")
        else :
            i01.speakBlocking(i01.localize("STARTINGAUDIOPLAYER"))
            i01_AudioPlayer = runtime.start('i01.audioPlayer','AudioFile')
    else:
        i01.warn("i01.chatBot needs to be started")

def previousPlay():
    if runtime.isStarted('i01.chatBot'):
        if runtime.isStarted('i01.audioPlayer'):
            initAudioPlayer()
            global pointeur 
            pointeur = pointeur -1
            i01_audioPlayer.stop()
            var = "".join(liste[pointeur][4:]).rstrip('\n')
            if 'mp3' in var :
                i01_audioPlayer.play(var)
                print(var+" Song : "+str(pointeur))
            else:
                i01_chatBot.getResponse("END_PLAYLIST")
                pointeur = -1
                i01_audioPlayer.stop()
                i01_chatBot.getResponse("SYSTEM_NEXT_SONG")
        else :
            i01.speakBlocking(i01.localize("STARTINGAUDIOPLAYER"))
            i01_AudioPlayer = runtime.start('i01.audioPlayer','AudioFile')
    else:
        i01.warn("i01.chatBot needs to be started")
