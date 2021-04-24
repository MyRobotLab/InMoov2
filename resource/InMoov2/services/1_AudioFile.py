# ##############################################################################
#                 AUDIOFILE SERVICE
# ##############################################################################
# http://myrobotlab.org/service/audiofile

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')

MyMusicPath=ThisServicePartConfig.get('AUDIO', 'MyMusicPath')

#for noworky
log.info("MyMusicPath : "+str(MyMusicPath))
musicpath = MyMusicPath 
import os

#startup sound
AudioPlayer = Runtime.createAndStart("AudioPlayer", "AudioFile")
mouthControlAudiofile=True

def onAudioStart(data):
  try:
    if ear.listening:
      ear.setAutoListen(False)
      ear.stopListening()
  except:
    pass
  
  if AudioSignalProcessing and isHeadActivated:
    print "onaudiostart"
    try:
      head.jaw.moveTo(180)
      left.enablePin(AnalogPinFromSoundCard,HowManyPollsBySecond)
    except:
      print "onAudioStart error"
      pass
      
  try:
    if MouthControlActivated and mouthControlAudiofile:i01_mouthControl.onStartSpeaking("This is a fake text, a long fake text, very long.")
  except:
    pass
    

def onAudioEnd(data):
  try:
    if not ear.listening:
      ear.setAutoListen(setAutoListen)
      ear.startListening()
  except:
    print "onAudioEnd error"
    pass
  if AudioSignalProcessing and isHeadActivated:
    try:
      left.disablePin(AnalogPinFromSoundCard)
      #head.jaw.detach()
    except:
      print "onAudioEnd error"
      pass
      
  try:
    if MouthControlActivated and mouthControlAudiofile:i01_mouthControl.onEndSpeaking("This is a fake text, a long fake text, very long.")
  except:
    pass
  
def AudioPlay(file):
  AudioPlayer.playFile(file,False)
      


python.subscribe(AudioPlayer.getName(),"publishAudioStart")
python.subscribe(AudioPlayer.getName(),"publishAudioEnd")
if StartupSound:AudioPlayer.playFile(RuningFolder+'/system/sounds/startupsound.mp3', False)
sleep(2)

global musiconoff
global cpt
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
        AudioPlayer.playFile((matches[i]) , False)
        ear.startListening()
        sleep(1)
        ear.setAutoListen(setAutoListen)
       

def playMusic():
    global musiconoff
    musiconoff = 1
    #musicpath = (RuningFolder+"/system/sounds/")
    files = os.listdir(musicpath)
    song=random.choice(files)
    sleep(3)
    #i01.speakBlocking("playing song" + str(song))
    AudioPlayer.playFile(musicpath + str(song) , False)
    print("playing song:" + str(song))
    # Select one of the mp3 files from the list at random
    mp3 = random.choice(fileList(musicpath))
    print mp3
    # Play the file
    sleep(1)
    AudioPlayer.playFile((mp3) , False)
    ear.startListening()
    sleep(1)
    ear.setAutoListen(setAutoListen)


# pause method 
def pauseMusic():
    global musiconoff
    if musiconoff == 1:
      AudioPlayer.pause()
      print "Pause music"

# resume method 
def resumeMusic():
    global musiconoff
    if musiconoff == 1:
      AudioPlayer.resume()
      print "Resume song"

# stop the music
def stopMusic():
    global musiconoff
    global cpt
    #print (cpt)
    if musiconoff == 1:
        AudioPlayer.stop()
        print "Stop music"
        if cpt > 1:
            i = -2
            while i < cpt :   
                #print (i)
                AudioPlayer.stop()
                i = i+1
                sleep(0.2)
                ear.startListening()
                sleep(1)
                ear.setAutoListen(setAutoListen)
            cpt = 0
            musiconoff = 0
        
def nextMusic():
    global musiconoff
    if musiconoff == 1:
        AudioPlayer.stop()
        play()
        sleep(1)
        ear.startListening()
        sleep(1)
        ear.setAutoListen(setAutoListen)
