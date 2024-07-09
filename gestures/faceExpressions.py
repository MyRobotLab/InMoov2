###///FACE EXPRESSIONS LIST///###

def faceMove(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13):
  if runtime.isStarted('i01.head'):
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


def bodyMove(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13):
  if runtime.isStarted('i01.head'):
    i01_head_neck.moveTo(pos1)
    i01_head_rothead.moveTo(pos2)
    i01_head_rollNeck.moveTo(pos3)
  if runtime.isStarted('i01.leftArm'):  
    i01_leftArm_omoplate.moveTo(pos4)
    i01_leftArm_shoulder.moveTo(pos5)
    i01_leftArm_rotate.moveTo(pos6)
    i01_leftArm_bicep.moveTo(pos7)
  if runtime.isStarted('i01.rightArm'):  
    i01_rightArm_omoplate.moveTo(pos8)
    i01_rightArm_shoulder.moveTo(pos9)
    i01_rightArm_rotate.moveTo(pos10)
    i01_rightArm_bicep.moveTo(pos11)
  if runtime.isStarted('i01.torso'):
    i01_torso_topStom.moveTo(pos12)
    i01_torso_midStom.moveTo(pos13)
  sleep(2.5)
  rest()  

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

def neutralHalfSpeed():
  cheeksNeutral()
  cheeksHalfSpeed()
  upperLipNeutral()
  upperLipHalfSpeed()
  eyelidsNeutral()
  eyelidsHalfSpeed()
  eyesC()
  eyesHalfSpeed()
  browsC()
  browsHalfSpeed()
  forheadsNeutral()
  forheadsHalfSpeed()  

def neutralLowSpeed():
  cheeksNeutral()
  cheeksLowSpeed()
  upperLipNeutral()
  upperLipLowSpeed()
  eyelidsNeutral()
  eyelidsLowSpeed()
  eyesC()
  eyesLowSpeed()
  browsC()
  browsLowSpeed()
  forheadsNeutral()
  forheadsLowSpeed()  

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
  neutralHalfSpeed()

def fear():
  eyelidsOpen()
  cheeksD()
  browsU()
  forheadsU()
  sleep(1)
  neutral()

def happy():
  browsHalfSpeed()
  browsU()
  cheeksLowSpeed()
  cheeksU()
  upperLipC()
  eyelidsLowSpeed()
  lowerEyelidsClose()
  if runtime.isStarted("i01.head"):
    i01_head_jaw.rest()
  sleep(1)
  browsC()
  eyelidsNeutral()
  cheeksNeutral()
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
    sleep(0.1)
    i01_audioPlayer.playFile('resource/InMoov2/system/sounds/Sigh_nose.wav')
    sleep(0.1)
  sleep(3)
  if runtime.isStarted('i01.head'):
    i01_head_neck.moveTo(90)
  neutral()

def sorry():
  browsHalfSpeed()
  browsU()
  cheeksLowSpeed()
  cheeksD()
  sleep(0.8)
  browsC()
  cheeksC()
  sleep(0.5)
  neutral()

def smile():
  cheeksHalfSpeed()
  cheeksU()
  lowerEyelidsClose()
  if runtime.isStarted('i01.head'):
    i01_head_jaw.moveTo(100)
  sleep(1)
  cheeksLowSpeed()
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
  neutralHalfSpeed()

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
  eyelidsHalfSpeed()
  lowerEyelidsClose()
  if runtime.isStarted('i01.head.eyeY'):
    i01_head_eyeY.moveTo(130)
  if runtime.isStarted('i01.head.eyeX'):
    i01_head_eyeX.moveTo(130)
  sleep(1.5)
  if runtime.isStarted('i01.head.eyeY'):
    i01_head_eyeY.rest()
  if runtime.isStarted('i01.head.eyeX'):
    i01_head_eyeX.rest()
  neutral()

def unamused():
  browRightD()
  forheadsLURD()
  eyelidsLowSpeed()
  eyelidsHalfShut()
  eyesLowSpeed()
  eyesR()
  cheeksLowSpeed()
  cheeksD()
  sleep(1.5)
  neutralHalfSpeed()

def wake():
  blink()

def lowSpeedFaceMove():
  browsLowSpeed()
  browRightD()
  forheadsLowSpeed()
  forheadsLURD()
  sleep(1)
  browsU()
  forheadsU()
  cheeksLowSpeed()
  cheeksC()
  sleep(1)
  neutralLowSpeed()
  i01.finishedGesture()

def halfSpeedFaceMove():
  browsHalfSpeed()
  browRightD()
  forheadsHalfSpeed()
  forheadsLURD()
  sleep(0.5)
  cheeksHalfSpeed()
  cheeksC()
  sleep(1)
  neutralHalfSpeed()
  i01.finishedGesture()

def fullSpeedFaceMove():
  browsU()
  forheadsU()
  cheeksFullSpeed()
  cheeksC()
  sleep(1)
  browsFullSpeed()
  browRightD()
  forheadsFullSpeed()
  forheadsLURD()
  sleep(1)
  neutral()
  i01.finishedGesture()


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
