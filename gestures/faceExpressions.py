###///FACE EXPRESSIONS LIST///###

def neutral():
  cheeksNeutral()
  upperLipC()
  eyelidsNeutral()
  eyesC()
  browsC()
  forHeadC()

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
  forHeadD()
  cheekRightU()
  browRightD()
  lowerEyelidRightClose()

def fear():
  eyelidsOpen()
  cheeksD()
  browsU()
  forHeadU()

def sad():
  upperEyelidsClose()
  lowerEyelidsOpen()
  cheeksD()

def smileClosed():
  cheeksU()
  upperLipD()
  lowerEyelidsU()
  i01_head_jaw.rest()

def smileOpen():
  cheeksU()
  lowerEyelidsU()
  upperLipU()
  i01_head_jaw.moveTo(90)

def sleeping():
  upperEyelidsClose()  

def surprise():
  browsU()
  upperLipU()
  forHeadU()
  i01_head_jaw.moveTo(70)

def suspicious():
  upperLipD()
  forHeadD()
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
#def aah():

#def bigAah():  

