###///FACE EXPRESSIONS LIST///###

def faceMove(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13):
  i01_head_eyeX.moveTo(pos1)
  i01_head_eyeY.moveTo(pos2)
  i01_head_eyelidLeftUpper.moveTo(pos3)
  i01_head_eyelidLeftLower.moveTo(pos4)
  i01_head_eyelidRightUpper.moveTo(pos5)
  i01_head_eyelidRightLower.moveTo(pos6)
  i01_head_eyebrowRight.moveTo(pos7)
  i01_head_eyebrowLeft.moveTo(pos8)
  i01_head_cheekRight.moveTo(pos9)
  i01_head_cheekLeft.moveTo(pos10)
  i01_head_upperLip.moveTo(pos11)
  i01_head_forheadRight.moveTo(pos12)
  i01_head_forheadLeft.moveTo(pos13)
  sleep(2.5)
  neutral()

def neutral():
  cheeksNeutral()
  cheeksFullSpeed()
  upperLipNeutral()
  upperLipFullSpeed()
  eyelidsNeutral()
  eyelidsFullSpeed()
  eyesC()
  eyesFullSpeed()
  browsC()
  browsFullSpeed()
  forheadsNeutral()
  forheadsFullSpeed()

def anger():
  forheadsU()    
  eyelidsHalfShut()
  upperLipU()
  cheeksD()
  browsD()
  sleep(1)
  neutral() 

def blinkLeft():
  cheekLeftU()
  browLeftD()
  eyelidLeftBlink()
  neutral()

def blinkRight():
  cheekRightU()
  browRightD()
  eyelidRightBlink()
  neutral()

def disgust():
  upperLipU()
  forheadsD()
  lowerEyelidsClose()
  cheekRightU()
  browsD()
  sleep(1)
  neutral()

def fear():
  eyelidsOpen()
  cheeksD()
  browsU()
  forheadsU()
  sleep(1)
  neutral()

def happy():
  cheeksLowSpeed()
  cheeksU()
  upperLipD()
  lowerEyelidsU()
  if runtime.isStarted('i01.head'):
    i01_head_jaw.rest()
  sleep(1)
  neutral()

def sad():
  upperEyelidsClose()
  cheeksD()
  sleep(1)
  neutral()

def sigh():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeLeftUD.setSpeed(20)
    i01_head_eyeLeftLR.setSpeed(20)
    i01_head_eyeRightUD.setSpeed(20)
    i01_head_eyeRightLR.setSpeed(20)
    ##
    i01_head_eyeLeftUD.moveTo(130)
    i01_head_eyeLeftLR.moveTo(130)
    i01_head_eyeRightUD.moveTo(130)
    i01_head_eyeRightLR.moveTo(130)
    sleep(0.1)
    i01_head_eyeLeftUD.setMaxSpeed()
    i01_head_eyeLeftLR.setMaxSpeed()
    i01_head_eyeRightUD.setMaxSpeed()
    i01_head_eyeRightLR.setMaxSpeed()
  if runtime.isStarted('i01.head'):
    i01_head_neck.moveTo(0)
  if runtime.isStarted('i01.audioPlayer'):
    i01_audioPlayer.setVolume(0.8)
    sleep(0.1)
    i01_audioPlayer.playFile('resource/InMoov2/system/sounds/Sigh_nose.wav')
    sleep(0.1)
    i01_audioPlayer.setVolume(1)    
  sleep(3)
  if runtime.isStarted('i01.head'):
    i01_head_neck.moveTo(90)
  neutral()

def sorry():
  browsU()
  cheeksD()
  sleep(0.5)
  neutral()

def smile():
  cheeksHalfSpeed()
  cheeksU()
  lowerEyelidsClose()
  if runtime.isStarted('i01.head'):
    i01_head_jaw.moveTo(110)
  sleep(1)
  eyelidsLowSpeed()
  lowerEyelidsU()
  cheeksC()
  if runtime.isStarted('i01.head'):
    i01_head_jaw.rest()
  sleep(0.5)
  neutral()  

def sleeping():
  upperEyelidsClose()
  lowerEyelidsClose()

def surprise():
  browsU()
  upperEyelidsOpen()
  forheadsD()
  if runtime.isStarted('i01.head'):
    i01_head_jaw.moveTo(160)
  sleep(0.5)
  if runtime.isStarted('i01.head'):
    i01_head_jaw.rest()
  neutral()

def suspicious():
  upperLipD()
  forheadsRULD()
  cheekLeftU()
  browsRULD()
  eyelidsLeftOpen()
  eyelidsRightHalfShut()
  sleep(1.5)
  neutral()

def thinking():
  browsD()
  forheadsU()
  upperEyelidsHalfShut()
  if runtime.isStarted('i01.head.eyeY'):
    i01_head_eyeY.moveTo(140)
  sleep(1.5)
  if runtime.isStarted('i01.head.eyeY'):
    i01_head_eyeY.rest()
  neutral()

def unamused():
  browRightD()
  forheadsLURD()
  eyelidsHalfShut()
  eyesR()
  cheeksD()
  sleep(1.5)
  neutral()

def wake():
  blink() 

def contempt():
  happy()
def anxiety():
  anger()
def disapointment():
  sad()
def frown():
  sad()  
def gasp():
  surprise()  
def helplessness():
  sorry()
def chuckle():
  smile()
def grin():
  smile()
def grins():
  smile()
def excited_face():
  surprise()
def nods():
  Yes()
def excited():
  surprise()
def excitedly():
  happy()
def smiles():
  smile()
def smiling():
  smile()  
def smiling_face():
  smile()
def surprised():
  surprise()  
def wink():
  winkLeft()
def winks():
  winkRight()
def wow():
  surprise()
