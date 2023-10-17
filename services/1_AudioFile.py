#########################################
# 1_AudioFile.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# -- coding: utf-8 --

if i01.getConfig().startupSound==1:
    i01_audioPlayer = runtime.start('i01.audioPlayer','AudioFile')
    i01_audioPlayer.playFile('resource/InMoov2/system/sounds/startupsound.mp3', False)

def initAudioPlayer():
    global musicPath
    global musicList
    audioPlayer = i01_audioPlayer
    musicPath = audioPlayer.getConfig().currentPlaylist
    musicList = 'data/config/default/i01.audioPlayer.yml'
    python.subscribe(audioPlayer.getName(),"publishAudioStart")
    python.subscribe(audioPlayer.getName(),"publishAudioEnd")

def onAudioStart(data):
  try:
    if i01_ear.listening:
      i01_ear.stopListening()
  except:
      print "onAudioStart error"
      pass
    
def onAudioEnd(data):
  try:
    if not i01_ear.listening:
      i01_ear.startListening()
  except:
    print "onAudioEnd error"
    pass    

def playMusic():
    if runtime.isStarted('i01.chatBot'):
        if runtime.isStarted('i01.audioPlayer'):
            initAudioPlayer()
            i01_audioPlayer.startPlaylist(musicPath,0,0)
        else :
            i01_AudioPlayer = runtime.start('i01.audioPlayer','AudioFile')
    else:
        i01.warn("i01.chatBot needs to be started")    


def playRandomMusic():
    if runtime.isStarted('i01.chatBot'):
        if runtime.isStarted('i01.audioPlayer'):
            initAudioPlayer()
            #TOSHUFFLE("playlistName", # of times played shuffle, boolean repeat, String track)
            i01_audioPlayer.startPlaylist(musicPath,1,0)
        else :
            i01_AudioPlayer = runtime.start('i01.audioPlayer','AudioFile')
    else:
        i01.warn("i01.chatBot needs to be started") 

def searchPlay(song):
    if runtime.isStarted('i01.chatBot'):
        if runtime.isStarted('i01.audioPlayer'):
            initAudioPlayer()
            global musicList
            if os.path.exists(musicList):
                    global liste
                    global pointeur
                    f = open(musicList, 'r')
                    liste = f.readlines()
                    #Remove the first 11 elements of the list
                    del liste[0:11]
                    i=0
                    flag =0
                    # iteration on the list with set up of the chaine
                    while i <= len(liste)-2 :  
                        var = unicode("".join(liste[i][4:]).rstrip('\n'),'utf-8')
                        if (song.lower() in var) or (song.capitalize() in var):
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
            var = unicode("".join(liste[pointeur][4:]).rstrip('\n'),'utf-8')
            if 'mp3' or 'wav' in var :
                i01_audioPlayer.play(var)
                print(var+" Song : "+str(pointeur))
            else:
                i01_chatBot.getResponse("END_PLAYLIST")
                pointeur = -1
                i01_audioPlayer.stop()
                i01_chatBot.getResponse("SYSTEM_NEXT_SONG")
        else :
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
            var = unicode("".join(liste[pointeur][4:]).rstrip('\n'),'utf-8')
            if 'mp3' or 'wav' in var :
                i01_audioPlayer.play(var)
                print(var+" Song : "+str(pointeur))
            else:
                i01_chatBot.getResponse("END_PLAYLIST")
                pointeur = -1
                i01_audioPlayer.stop()
                i01_chatBot.getResponse("SYSTEM_NEXT_SONG")
        else :
            i01_AudioPlayer = runtime.start('i01.audioPlayer','AudioFile')
    else:
        i01.warn("i01.chatBot needs to be started")

