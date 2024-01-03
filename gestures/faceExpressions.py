###///FACE EXPRESSIONS LIST///###

def neutral():
  cheeksNeutral()
  upperLipNeutral()
  eyelidsNeutral()
  eyesC()
  browsC()
  forheadsNeutral()

def anger():
  eyelidsHalfShut()
  upperLipU()
  cheeksD()
  browsD()

def blinkLeft():
  browLeftD()
  eyelidLeftBlink()
  cheekLeftU()

def blinkRight():
  browRightD()
  eyelidRightBlink()
  cheekRightU()

def disgust():
  upperLipD()
  forheadsD()
  cheekRightU()
  browRightD()
  lowerEyelidRightClose()

def fear():
  eyelidsOpen()
  cheeksD()
  browsU()
  forheadsU()

def sad():
  upperEyelidsClose()
  lowerEyelidsOpen()
  cheeksD()

def smileClosed():
  cheeksU()
  upperLipD()
  lowerEyelidsU()
  if runtime.isStarted('i01.head'):
    i01_head_jaw.rest()

def smileOpen():
  cheeksU()
  lowerEyelidsU()
  upperLipU()
  if runtime.isStarted('i01.head'):
    i01_head_jaw.moveTo(90)

def sleeping():
  upperEyelidsClose()  

def surprise():
  browsU()
  upperLipU()
  forheadsU()
  if runtime.isStarted('i01.head'):
    i01_head_jaw.moveTo(70)

def suspicious():
  upperLipD()
  forheadsRULD()
  cheekLeftU()
  browsRULD()
  eyelidsLeftOpen()
  eyelidsRightHalfShut()

def unamused():
  browRightD()
  eyelidsHalfShut()
  eyesR()
  cheeksD()

def wake():
  blink() 

#def contempt():
#def anxiety():
#def disapointment():
#def helplessness():
