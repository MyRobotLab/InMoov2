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
  upperLipU()
  forheadsD()
  lowerEyelidsClose()
  cheekRightU()
  browsD()

def fear():
  eyelidsOpen()
  cheeksD()
  browsU()
  forheadsU()

def sad():
  upperEyelidsClose()
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
  if runtime.isStarted('i01.head'):
    i01_head_jaw.moveTo(90)

def sleeping():
  upperEyelidsClose()
  lowerEyelidsClose()

def surprise():
  browsU()
  upperEyelidsOpen()
  forheadsU()
  if runtime.isStarted('i01.head'):
    i01_head_jaw.moveTo(160)

def suspicious():
  upperLipD()
  forheadsRULD()
  cheekLeftU()
  browsRULD()
  eyelidsLeftOpen()
  eyelidsRightHalfShut()

def thinking():
  forheadsU()
  eyelidsOpen()
  lowerEyelidsClose()
  if runtime.isStarted('i01.head.eyeY'):
    i01_head_eyeY.moveTo(120)

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
