###///FACE EXPRESSIONS LIST///###

def neutral():
  cheeksNeutral()
  upperLipNeutral()
  eyelidsNeutral()
  eyesC()
  browsC()
  forheadsNeutral()

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

def sorry():
  browsU()
  cheeksD()
  sleep(0.5)
  neutral()

def smile():
  cheeksU()
  lowerEyelidsU()
  if runtime.isStarted('i01.head'):
    i01_head_jaw.moveTo(90)
  sleep(0.2)
  if runtime.isStarted('i01.head'):
    i01_head_jaw.rest()
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
def helplessness():
  sorry()
def chuckle():
  smile()
def grin():
  smile()
def grins():
  smile()  
def excited_face():
  surprised()
def nods():
  yes()
def excited():
  surprised()
def excitedly():
  happy()
def smiles():
  smile()
def smiling():
  smile()  
def smiling_face():
  smile()
def wink():
  winkLeft()
def winks():
  winkRight()    