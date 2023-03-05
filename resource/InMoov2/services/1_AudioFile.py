#########################################
# i01_audioPlayer.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

i01_audioPlayer = runtime.start("i01.audioPlayer", "AudioFile")
audioPlayer=i01_audioPlayer
musicpath = audioPlayer.getConfig().currentPlaylist
#i01.startAudioPlayer()
mouthControlAudiofile=True

# def onAudioStart(data):
#   try:
#     if i01_ear.listening:
#       i01_ear.setAutoListen(False)
#       i01_ear.stopListening()
#   except:
#     pass
  
#   if AudioSignalProcessing and runtime.isStarted('i01.head'):
#     print "onaudiostart"
#     try:
#       i01_head.jaw.moveTo(180)
#       i01_left.enablePin(AnalogPinFromSoundCard,HowManyPollsBySecond)
#     except:
#       print "onAudioStart error"
#       pass
      
#   try:
#     if runtime.isStarted('i01.mouthControl') and mouthControlAudiofile:i01_mouthControl.onStartSpeaking("This is a fake text, a long fake text, very long.")
#   except:
#     pass
    

# def onAudioEnd(data):
#   try:
#     if not i01_ear.listening:
#       i01_ear.setAutoListen(True)
#       i01_ear.startListening()
#   except:
#     print "onAudioEnd error"
#     pass
#   if AudioSignalProcessing and runtime.isStarted('i01.head'):
#     try:
#       i01_left.disablePin(AnalogPinFromSoundCard)
#       i01_head_jaw.disable()
#     except:
#       print "onAudioEnd error"
#       pass
      
#   try:
#     if runtime.isStarted('i01.mouthControl') and mouthControlAudiofile:i01_mouthControl.onEndSpeaking("This is a fake text, a long fake text, very long.")
#   except:
#     pass
  
def AudioPlay(file):
  i01_audioPlayer.playFile(file,False)
      


#python.subscribe(i01_audioPlayer.getName(),"publishAudioStart")
#python.subscribe(i01_audioPlayer.getName(),"publishAudioEnd")
sleep(2)

global musiconoff
global cpt
global element
musiconoff = 0
cpt = 0

 
# Function to create a list of mp3 files
def fileList(musicpath):
    global matches
    global element
    matches = []
    for root, dirs, element in os.walk(musicpath):
        for mp3 in element:
            #if mp3.endswith(('.mp3', '.m4a', '.wav')):
            if mp3.endswith(('.mp3', '.wav')):  
                #print root+'/'+str(file)
                #print mp3
                matches.append(os.path.join(root+'/'+str(mp3)))
   
    return matches

def playRandomMusic():
      global musiconoff
      fileList(musicpath)
      musiconoff = 1
      global matches
      global element
      global cpt
      print("Loaded: " + str(len(matches)) + " files. " + str(len(element)) + " files for random")
      cpt = len(matches)
      print (cpt)
 
      random.shuffle(matches)
      
      for i in range(0,len(element)+1):
        print(matches[i])
        sleep(1)
        i01_audioPlayer.playFile((matches[i]) , False)
        ear.startListening()
        sleep(1)
        ear.setAutoListen(True)
       

def playMusic():
    global musiconoff
    musiconoff = 1
    #musicpath = (RuningFolder+"/system/sounds/")
    files = os.listdir(musicpath)
    song=random.choice(files)
    sleep(3)
    #i01.speakBlocking("playing song" + str(song))
    i01_audioPlayer.playFile(musicpath + str(song) , False)
    i01.info("playing song:" + str(song))
    # Select one of the mp3 files from the list at random
    mp3 = random.choice(fileList(musicpath))
    print mp3
    # Play the file
    sleep(1)
    i01_audioPlayer.playFile((mp3) , False)
    ear.startListening()
    sleep(1)
    ear.setAutoListen(True)


# pause method 
def pauseMusic():
    global musiconoff
    if musiconoff == 1:
      i01_audioPlayer.pause()
      print "Pause music"

# resume method 
def resumeMusic():
    global musiconoff
    if musiconoff == 1:
      i01_audioPlayer.resume()
      print "Resume song"

# stop the music
def stopMusic():
    global musiconoff
    global cpt
    #print (cpt)
    if musiconoff == 1:
        i01_audioPlayer.stop()
        print "Stop music"
        if cpt > 1:
            i = -2
            while i < cpt :   
                #print (i)
                i01_audioPlayer.stop()
                i = i+1
                sleep(0.2)
                ear.startListening()
                sleep(1)
                ear.setAutoListen(True)
            cpt = 0
            musiconoff = 0
        
def nextMusic():
    global musiconoff
    if musiconoff == 1:
        i01_audioPlayer.stop()
        play()
        sleep(1)
        ear.startListening()
        sleep(1)
        ear.setAutoListen(True)

def searchPlay(song):
    global musiconoff
    f = open(musicpath, 'r')
    liste = f.readlines()
    #Remove the first 11 elements of the list
    del liste[0:11]
    i=0
    flag =0
    # iteration on the list with set up of the chaine
    while i <= len(liste)-2 :  
        var = "".join(liste[i][4:]).rstrip('\n')
        #if " "+song+" " in (" " + var + " "):
        #if song.lower() in var :
        if song in var :    
            i01_audioPlayer.play(var)
            flag = 1
            print(var)
        i=i+1
    if flag == 0 :
        i01.warn(u"I don't have this song in my list, or the file contains upper case.")
    f.close()
