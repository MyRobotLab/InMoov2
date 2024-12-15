#########################################
# 1_AudioFile.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
# modif lecagnois le 13/12/2024 pour jukeboxe et radio
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
      print("onAudio Start")
      pass
    
def onAudioEnd(data):
  try:
    if not i01_ear.listening:
        i01_ear.startListening()
  except:
    print("onAudio End")
    pass       

# Procedure pour le jukebox
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
    song = song.decode('utf-8')
    if runtime.isStarted('i01.chatBot'):
        if runtime.isStarted('i01.audioPlayer'):
            initAudioPlayer()
            global musicList
            global pointeur
            global lignes_audio
            if os.path.exists(musicList):
              #create a list of songs from the i01.audioPlayer.yml file
                    lignes_audio = []
                    lignes_audio.append("bigin")
                    with open(musicList, 'r') as f:
                        for ligne in f:
                            if( ".mp3" in ligne) or ( ".wav" in ligne):
                                Mchaine = (ligne.strip().decode('utf-8')).lower()
                                lignes_audio.append(Mchaine)      
                        lignes_audio.append("eof")
                    #for result in lignes_audio :
                    #    print(result)
                    i=0
                    flag =0
                    # iteration on the list with set up of the chaine
                    while i <= len(lignes_audio)-1 :  
                        var = ("".join(lignes_audio[i][4:]).rstrip('\n'))
                        if (song.lower() in var) or (song.capitalize() in var):
                            i01_audioPlayer.play(var)
                            pointeur = i
                            flag = 1
                            print("I've found "+var+" Song : "+str(i+1))
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
    #i01_audioPlayer.stop()
    if runtime.isStarted('i01.chatBot'):
        if runtime.isStarted('i01.audioPlayer'):
            initAudioPlayer()
            global pointeur 
            global lignes_audio
            pointeur = pointeur + 1
            i01_audioPlayer.stop()
            var = unicode("".join(lignes_audio[pointeur][4:]).rstrip('\n'),'utf-8')
            print(var+" Song : "+str(pointeur))
            if ("mp3" or "wav") in var :
                i01_audioPlayer.play(var)
                print(var+" Song : "+str(pointeur))
            else :
                i01_chatBot.getResponse("END_PLAYLIST")
                pointeur = pointeur-pointeur +1
                i01_audioPlayer.stop()
                #i01_chatBot.getResponse("SYSTEM_NEXT_SONG")
                i01_audioPlayer.play(unicode("".join(lignes_audio[pointeur][4:]).rstrip('\n'),'utf-8'))
                print(" start of playlist : "+("".join(lignes_audio[1][4:]).rstrip('\n'))+" Song : "+str(pointeur))
        else :
            i01_AudioPlayer = runtime.start('i01.audioPlayer','AudioFile')
    else:
        i01.warn("i01.chatBot needs to be started")

def previousPlay():
    if runtime.isStarted('i01.chatBot'):
        if runtime.isStarted('i01.audioPlayer'):
            initAudioPlayer()
            global pointeur
            global lignes_audio
            pointeur = pointeur -1
            i01_audioPlayer.stop()
            var = unicode("".join(lignes_audio[pointeur][4:]).rstrip('\n'),'utf-8')
            #print(var+" Song : "+str(pointeur))
            if ("mp3" or "wav'") in var :
                i01_audioPlayer.play(var)
                print(var+" Song : "+str(pointeur))
            else:
                # sinon arriver au debut de la liste on recommence
                i01_chatBot.getResponse("BEGIN_PLAYLIST")
                pointeur = pointeur + 1
                i01_audioPlayer.stop()
                i01_audioPlayer.play(unicode("".join(lignes_audio[pointeur][4:]).rstrip('\n'),'utf-8'))
                print(" start of playlist : "+("".join(lignes_audio[1][4:]).rstrip('\n'))+" Song : "+str(pointeur))
                
        else :
            i01_AudioPlayer = runtime.start('i01.audioPlayer','AudioFile')
    else:
        i01.warn("i01.chatBot needs to be started")
 
def authorPlaylist() : 
    if runtime.isStarted('i01.chatBot'): 
        if runtime.isStarted('i01.audioPlayer'):
            global musicList
            initAudioPlayer()
            #create a list of author from the i01.audioPlayer.yml file
            lignes_auteur = []
            with open(musicList, 'r') as f:
                for ligne in f:
                    if(".mp3" not in ligne) and ("publishPeakResetDelayMs" not in ligne) and ("playlists" not in ligne) and ("null" not in ligne)\
                    and ("false" not in ligne) and ("true" not in ligne) and ("AudioFile" not in ligne) and ("method" not in ligne)  and ("myrobotlab" not in ligne)\
                    and ("callback" not in ligne)  and ("audio" not in ligne) and ("current" not in ligne) and ("peak" not in ligne) and ("listener" not in ligne)and \
                    ("volume" not in ligne) and (".wav" not in ligne):
                        lignes_auteur.append(ligne.strip().decode('utf-8'))  
            for result in lignes_auteur :
                print(result)         
            for i in range(len(lignes_auteur)):
                i01.speakBlocking(u","+lignes_auteur[i])
            f.close()   
        else :
            i01_AudioPlayer = runtime.start('i01.audioPlayer','AudioFile')
    else:
        i01.warn("i01.chatBot needs to be started")


# radio process
def startRadio(station):
    if runtime.isStarted('i01.chatBot'):
        if station[:4].lower() == 'http':
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
        else:
            i01_chatBot.getResponse("DO_NOT_HAVE_RADIO")
    else:
        i01.warn("i01.chatBot needs to be started")

def stopRadio():
    if runtime.isStarted('i01.chatBot'):
        if runtime.isStarted('i01.audioPlayer'):
            audioPlayer = runtime.getService('i01.audioPlayer')
            audioPlayer.stop()
            print("Radio stopped")
            audiocfg = audioPlayer.getConfig()
            if audiocfg.stream == 1:
                audiocfg.stream = 1
                audioPlayer.save()
                audioPlayer.apply(audiocfg)
                audioPlayer.broadcastState()
    else:
        i01.warn("i01.chatBot needs to be started")
