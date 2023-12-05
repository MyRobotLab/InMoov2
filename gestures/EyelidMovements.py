###///PINOUT///###

# i01_eyelidRightUpper.PIN(7)
# i01_eyelidLeftUpper.PIN(8)
# i01_eyelidRightLower.PIN(9)
# i01_eyelidLeftLower.PIN(10)

###///EYELID MOVEMENT LIST///###

###BOTH EYELIDS###

#blink()                    /       Blinks Eyelids
#winkBoth()                 /       Both Eyes Wink
#eyelidsClose()             /       Closes Eyelids
#eyelidsOpen()              /       Opens Eyelids
#eyelidsHalfShut()
#eyelidsNeutral()
#eyelidsHalfSpeed()
#eyelidsFullSpeed()
#upperEyelidsOpen()         /       Open Upper Eyelids
#upperEyelidsClose()        /       Close Upper Eyelids
#lowerEyelidsOpen()         /       Open Lower Eyelids
#lowerEyelidsClose()        /       Close Lower Eyelids
#lowerEyelidsU()            /       Half Close Lower Eyelids

###LEFT EYELIDS ONLY### 
#eyelidLeftBlink()          /       Blink left Eyelids
#winkLeft()                 /       Winks left Eye
#eyelidsLeftOpen()          /       Opens left Eyelids
#eyelidsLeftClose()         /       Closes left Eyelids
#eyelidsLeftHalfShut()      /       Closes Half left Eyelids
#upperEyelidLeftOpen()      /       Opens Upper left Eyelid
#upperEyelidLeftClose()     /       Closes Upper left Eyelid
#lowerEyelidLeftOpen()      /       Opens Lower left Eyelid
#lowerEyelidLeftClose()     /       Closes Lower left Eyelid
#lowerEyelidLeftU()         /       Half Close Lower left Eyelid

###RIGHT EYELIDS ONLY### 
#eyelidRightBlink()         /       Blink right Eyelids
#winkRight()                /       Winks right Eye
#eyelidsRightOpen()         /       Opens right Eyelids
#eyelidsRightClose()        /       Closes right Eyelids
#eyelidsRightHalfShut()     /       Closes Half right Eyelids
#upperEyelidRightOpen()     /       Opens Upper right Eyelid
#upperEyelidRightClose()    /       Closes Upper right Eyelid
#lowerEyelidRightOpen()     /       Opens Lower right Eyelid
#lowerEyelidRightClose()    /       Close Lower right Eyelid
#lowerEyelidRightU()        /       Half Close Lower right Eyelid


###BOTH EYELIDS###

def blink():
  if runtime.isStarted('i01.eyelidLeftUpper') and runtime.isStarted('i01.eyelidLeftLower') and runtime.isStarted('i01.eyelidRightUpper') and runtime.isStarted('i01.eyelidRightLower'):
      i01_eyelidLeftUpper.moveTo(180)
      i01_eyelidLeftLower.moveTo(180)
      i01_eyelidRightUpper.moveTo(180)
      i01_eyelidRightLower.moveTo(180)
      sleep(0.1)
      i01_eyelidLeftUpper.moveTo(0)
      i01_eyelidLeftLower.moveTo(0)
      i01_eyelidRightUpper.moveTo(0)
      i01_eyelidRightLower.moveTo(0)
      sleep(0.1)
      i01_eyelidLeftUpper.rest()
      i01_eyelidLeftLower.rest()
      i01_eyelidRightUpper.rest()
      i01_eyelidRightLower.rest()
      sleep(0.1)
  
def winkBoth():
  if runtime.isStarted('i01.eyelidLeftUpper') and runtime.isStarted('i01.eyelidLeftLower') and runtime.isStarted('i01.eyelidRightUpper') and runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidLeftUpper.moveTo(180)
    i01_eyelidLeftLower.moveTo(180)
    i01_eyelidRightUpper.moveTo(180)
    i01_eyelidRightLower.moveTo(180)
    sleep(0.1)
    i01_eyelidLeftUpper.moveTo(0)
    i01_eyelidLeftLower.moveTo(0)
    i01_eyelidRightUpper.moveTo(0)
    i01_eyelidRightLower.moveTo(0)
    sleep(1)
    i01_eyelidLeftUpper.rest()
    i01_eyelidLeftLower.rest()
    i01_eyelidRightUpper.rest()
    i01_eyelidRightLower.rest()
    sleep(0.1)

def eyelidsNeutral():
  if runtime.isStarted('i01.eyelidLeftUpper') and runtime.isStarted('i01.eyelidLeftLower') and runtime.isStarted('i01.eyelidRightUpper') and runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidLeftUpper.rest()
    i01_eyelidLeftLower.rest()
    i01_eyelidRightUpper.rest()
    i01_eyelidRightLower.rest()
    sleep(0.1)
  
def eyelidsClose():
  if runtime.isStarted('i01.eyelidLeftUpper') and runtime.isStarted('i01.eyelidLeftLower') and runtime.isStarted('i01.eyelidRightUpper') and runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidRightUpper.moveTo(0)
    i01_eyelidLeftUpper.moveTo(0)
    i01_eyelidRightLower.moveTo(0)
    i01_eyelidLeftLower.moveTo(0)
    sleep(0.1)
  
def eyelidsOpen():
  if runtime.isStarted('i01.eyelidLeftUpper') and runtime.isStarted('i01.eyelidLeftLower') and runtime.isStarted('i01.eyelidRightUpper') and runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidRightUpper.moveTo(180)
    i01_eyelidLeftUpper.moveTo(180)
    i01_eyelidRightLower.moveTo(180)
    i01_eyelidLeftLower.moveTo(180)
    sleep(0.1)

def eyelidsHalfShut():
  if runtime.isStarted('i01.eyelidLeftUpper') and runtime.isStarted('i01.eyelidLeftLower') and runtime.isStarted('i01.eyelidRightUpper') and runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidLeftUpper.moveTo(80)
    i01_eyelidLeftLower.moveTo(80)
    i01_eyelidRightUpper.moveTo(80)
    i01_eyelidRightLower.moveTo(80)
    sleep(0.1)

def eyelidsHalfSpeed():
  if runtime.isStarted('i01.eyelidLeftUpper') and runtime.isStarted('i01.eyelidLeftLower') and runtime.isStarted('i01.eyelidRightUpper') and runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidLeftUpper.setSpeed(100)
    i01_eyelidLeftLower.setSpeed(100)
    i01_eyelidRightUpper.setSpeed(100)
    i01_eyelidRightLower.setSpeed(100)

def eyelidsFullSpeed():
  if runtime.isStarted('i01.eyelidLeftUpper') and runtime.isStarted('i01.eyelidLeftLower') and runtime.isStarted('i01.eyelidRightUpper') and runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidLeftUpper.setSpeed(180)
    i01_eyelidLeftLower.setSpeed(180)
    i01_eyelidRightUpper.setSpeed(180)
    i01_eyelidRightLower.setSpeed(180)

def upperEyelidsOpen():
  if runtime.isStarted('i01.eyelidLeftUpper') and runtime.isStarted('i01.eyelidRightUpper'):
    i01_eyelidLeftUpper.moveTo(180)
    i01_eyelidRightUpper.moveTo(180)
    sleep(0.1)
  
def upperEyelidsClose():
  if runtime.isStarted('i01.eyelidLeftUpper') and runtime.isStarted('i01.eyelidRightUpper'):
    i01_eyelidLeftUpper.moveTo(0)
    i01_eyelidRightUpper.moveTo(0)
    sleep(0.1)
  
def lowerEyelidsOpen():
  if runtime.isStarted('i01.eyelidLeftLower') and runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidLeftLower.moveTo(180)
    i01_eyelidRightLower.moveTo(180)
    sleep(0.1)
  
def lowerEyelidsClose():
  if runtime.isStarted('i01.eyelidLeftLower') and runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidLeftLower.moveTo(0)
    i01_eyelidRightLower.moveTo(0)
    sleep(0.1)

def lowerEyelidsU():
  if runtime.isStarted('i01.eyelidLeftLower') and runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidLeftLower.moveTo(110)
    i01_eyelidRightLower.moveTo(110)
    sleep(0.1)
  
  
###LEFT EYELIDS ONLY###   
def eyelidLeftBlink():
  if runtime.isStarted('i01.eyelidLeftUpper') and runtime.isStarted('i01.eyelidLeftLower'):
    i01_eyelidLeftUpper.moveTo(180)
    i01_eyelidLeftLower.moveTo(180)
    sleep(0.1)
    i01_eyelidLeftUpper.moveTo(0)
    i01_eyelidLeftLower.moveTo(0)
    sleep(0.1)
    i01_eyelidLeftUpper.rest()
    i01_eyelidLeftLower.rest()
    sleep(0.1)
  
def winkLeft():
  if runtime.isStarted('i01.eyelidLeftUpper') and runtime.isStarted('i01.eyelidLeftLower'):
    i01_eyelidLeftUpper.moveTo(180)
    i01_eyelidLeftLower.moveTo(180)
    sleep(0.1)
    i01_eyelidLeftUpper.moveTo(0)
    i01_eyelidLeftLower.moveTo(0)
    sleep(1)
    i01_eyelidLeftUpper.rest()
    i01_eyelidLeftLower.rest()
    sleep(0.1)

def eyelidsLeftOpen():
  if runtime.isStarted('i01.eyelidLeftUpper') and runtime.isStarted('i01.eyelidLeftLower'):
    i01_eyelidLeftUpper.moveTo(180)
    i01_eyelidLeftLower.moveTo(180)
    sleep(0.1)

def eyelidsLeftClose():
  if runtime.isStarted('i01.eyelidLeftUpper') and runtime.isStarted('i01.eyelidLeftLower'):
    i01_eyelidLeftUpper.moveTo(0)
    i01_eyelidLeftLower.moveTo(0)
    sleep(0.1)

def eyelidsLeftHalfShut():
  if runtime.isStarted('i01.eyelidLeftUpper') and runtime.isStarted('i01.eyelidLeftLower'):
    i01_eyelidLeftUpper.moveTo(80)
    i01_eyelidLeftLower.moveTo(80)
    sleep(0.1)
  
def upperEyelidLeftOpen():
  if runtime.isStarted('i01.eyelidLeftUpper'):
    i01_eyelidLeftUpper.moveTo(180)
    sleep(0.1)
  
def upperEyelidLeftClose():
  if runtime.isStarted('i01.eyelidLeftUpper'):
    i01_eyelidLeftUpper.moveTo(0)
    sleep(0.1)
  
def lowerEyelidLeftOpen():
  if runtime.isStarted('i01.eyelidLeftLower'):
    i01_eyelidLeftLower.moveTo(180)
    sleep(0.1)
  
def lowerEyelidLeftClose():
  if runtime.isStarted('i01.eyelidLeftLower'):
    i01_eyelidLeftLower.moveTo(0)
    sleep(0.1)

def lowerEyelidLeftU():
  if runtime.isStarted('i01.eyelidLeftLower'):
    i01_eyelidLeftLower.moveTo(130)
    sleep(0.1)

###RIGHT EYELIDS ONLY###
def eyelidRightBlink():
  if runtime.isStarted('i01.eyelidRightUpper') and runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidRightUpper.moveTo(180)
    i01_eyelidRightLower.moveTo(180)
    sleep(0.1)
    i01_eyelidRightUpper.moveTo(0)
    i01_eyelidRightLower.moveTo(0)
    sleep(0.1)
    i01_eyelidRightUpper.rest()
    i01_eyelidRightLower.rest()
    sleep(0.1)
  
def winkRight():
  if runtime.isStarted('i01.eyelidRightUpper') and runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidRightUpper.moveTo(180)
    i01_eyelidRightLower.moveTo(180)
    sleep(0.1)
    i01_eyelidRightUpper.moveTo(0)
    i01_eyelidRightLower.moveTo(0)
    sleep(1)
    i01_eyelidRightUpper.rest()
    i01_eyelidRightLower.rest()
    sleep(0.1)

def eyelidsRightOpen():
  if runtime.isStarted('i01.eyelidRightUpper') and runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidRightUpper.moveTo(180)
    i01_eyelidRightLower.moveTo(180)
    sleep(0.1)

def eyelidsRightClose():
  if runtime.isStarted('i01.eyelidRightUpper') and runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidRightUpper.moveTo(0)
    i01_eyelidRightLower.moveTo(0)
    sleep(0.1)

def eyelidsRightHalfShut():
  if runtime.isStarted('i01.eyelidRightUpper') and runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidRightUpper.moveTo(80)
    i01_eyelidRightLower.moveTo(80)
    sleep(0.1)  
  
def upperEyelidRightOpen():
  if runtime.isStarted('i01.eyelidRightUpper'):
    i01_eyelidRightUpper.moveTo(180)
    sleep(0.1)
  
def upperEyelidRightClose():
  if runtime.isStarted('i01.eyelidRightUpper'):
    i01_eyelidRightUpper.moveTo(0)
    sleep(0.1)
  
def lowerEyelidRightOpen():
  if runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidRightLower.moveTo(180)
    sleep(0.1)
  
def lowerEyelidRightClose():
  if runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidRightLower.moveTo(0)
    sleep(0.1)

def lowerEyelidRightU():
  if runtime.isStarted('i01.eyelidRightLower'):
    i01_eyelidRightLower.moveTo(130)
    sleep(0.1)  