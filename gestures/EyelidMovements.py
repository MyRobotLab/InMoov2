###///PINOUT///###

# i01_head_eyelidRightUpper.PIN(7)
# i01_head_eyelidRightLower.PIN(8)
# i01_head_eyelidLeftUpper.PIN(9)
# i01_head_eyelidLeftLower.PIN(10)

###///EYELID MOVEMENT LIST///###

###BOTH EYELIDS SPEED###

#eyelidsFullSpeed()
#eyelidsHalfSpeed()
#eyelidsLowSpeed()

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
#upperEyelidsHalfShut()     /       Half Close Upper Eyelids
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


###BOTH EYELIDS SPEED###
def eyelidsFullSpeed():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower') and runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidLeftUpper.setSpeed(500)
    i01_head_eyelidRightUpper.setSpeed(500)
    i01_head_eyelidLeftLower.setSpeed(500)
    i01_head_eyelidRightLower.setSpeed(500)

def eyelidsHalfSpeed():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower') and runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidLeftUpper.setSpeed(200)
    i01_head_eyelidRightUpper.setSpeed(200)
    i01_head_eyelidLeftLower.setSpeed(200)
    i01_head_eyelidRightLower.setSpeed(200)

def eyelidsLowSpeed():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower') and runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidLeftUpper.setSpeed(20)
    i01_head_eyelidRightUpper.setSpeed(20)
    i01_head_eyelidLeftLower.setSpeed(20)
    i01_head_eyelidRightLower.setSpeed(20)

#############################################
###BOTH EYEBROWS###  
def blink():
  eyelidsFullSpeed()
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower') and runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
      i01_head_eyelidLeftUpper.moveTo(0)
      i01_head_eyelidRightUpper.moveTo(0)
      i01_head_eyelidLeftLower.moveTo(0)
      i01_head_eyelidRightLower.moveTo(0)
      sleep(0.2)
      i01_head_eyelidLeftUpper.rest()
      i01_head_eyelidRightUpper.rest()
      i01_head_eyelidLeftLower.rest()
      i01_head_eyelidRightLower.rest()
      sleep(0.1)
  
def winkBoth():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower') and runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidLeftUpper.moveTo(0)
    i01_head_eyelidLeftLower.moveTo(0)
    i01_head_eyelidRightUpper.moveTo(0)
    i01_head_eyelidRightLower.moveTo(0)
    sleep(1)
    i01_head_eyelidLeftUpper.rest()
    i01_head_eyelidLeftLower.rest()
    i01_head_eyelidRightUpper.rest()
    i01_head_eyelidRightLower.rest()
    sleep(0.1)

def eyelidsNeutral():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower') and runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidLeftUpper.rest()
    i01_head_eyelidLeftLower.rest()
    i01_head_eyelidRightUpper.rest()
    i01_head_eyelidRightLower.rest()
    
  
def eyelidsClose():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower') and runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidRightUpper.moveTo(0)
    i01_head_eyelidLeftUpper.moveTo(0)
    i01_head_eyelidRightLower.moveTo(0)
    i01_head_eyelidLeftLower.moveTo(0)
    
  
def eyelidsOpen():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower') and runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidRightUpper.moveTo(180)
    i01_head_eyelidLeftUpper.moveTo(180)
    i01_head_eyelidRightLower.moveTo(180)
    i01_head_eyelidLeftLower.moveTo(180)
    

def eyelidsHalfShut():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower') and runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidLeftUpper.moveTo(70)
    i01_head_eyelidLeftLower.moveTo(70)
    i01_head_eyelidRightUpper.moveTo(70)
    i01_head_eyelidRightLower.moveTo(70)
    

def eyelidsHalfSpeed():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower') and runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidLeftUpper.setSpeed(100)
    i01_head_eyelidLeftLower.setSpeed(100)
    i01_head_eyelidRightUpper.setSpeed(100)
    i01_head_eyelidRightLower.setSpeed(100)

def eyelidsFullSpeed():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower') and runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidLeftUpper.setSpeed(180)
    i01_head_eyelidLeftLower.setSpeed(180)
    i01_head_eyelidRightUpper.setSpeed(180)
    i01_head_eyelidRightLower.setSpeed(180)

def upperEyelidsHalfShut():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidRightUpper'):
    i01_head_eyelidLeftUpper.moveTo(70)
    i01_head_eyelidRightUpper.moveTo(70)   

def upperEyelidsOpen():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidRightUpper'):
    i01_head_eyelidLeftUpper.moveTo(180)
    i01_head_eyelidRightUpper.moveTo(180)
    
  
def upperEyelidsClose():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidRightUpper'):
    i01_head_eyelidLeftUpper.moveTo(0)
    i01_head_eyelidRightUpper.moveTo(0)
    
  
def lowerEyelidsOpen():
  if runtime.isStarted('i01.head.eyelidLeftLower') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidLeftLower.moveTo(180)
    i01_head_eyelidRightLower.moveTo(180)
    
  
def lowerEyelidsClose():
  if runtime.isStarted('i01.head.eyelidLeftLower') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidLeftLower.moveTo(0)
    i01_head_eyelidRightLower.moveTo(0)
    

def lowerEyelidsU():
  if runtime.isStarted('i01.head.eyelidLeftLower') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidLeftLower.moveTo(50)
    i01_head_eyelidRightLower.moveTo(50)
    
  
  
###LEFT EYELIDS ONLY###   
def eyelidLeftBlink():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower'):
    i01_head_eyelidLeftUpper.moveTo(0)
    i01_head_eyelidLeftLower.moveTo(0)
    sleep(0.1)
    i01_head_eyelidLeftUpper.rest()
    i01_head_eyelidLeftLower.rest()
    sleep(0.1)
  
def winkLeft():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower'):
    i01_head_eyelidLeftUpper.moveTo(0)
    i01_head_eyelidLeftLower.moveTo(0)
    sleep(1)
    i01_head_eyelidLeftUpper.rest()
    i01_head_eyelidLeftLower.rest()
    sleep(0.1)

def eyelidsLeftOpen():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower'):
    i01_head_eyelidLeftUpper.moveTo(180)
    i01_head_eyelidLeftLower.moveTo(180)
    

def eyelidsLeftClose():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower'):
    i01_head_eyelidLeftUpper.moveTo(0)
    i01_head_eyelidLeftLower.moveTo(0)
    

def eyelidsLeftHalfShut():
  if runtime.isStarted('i01.head.eyelidLeftUpper') and runtime.isStarted('i01.head.eyelidLeftLower'):
    i01_head_eyelidLeftUpper.moveTo(70)
    i01_head_eyelidLeftLower.moveTo(70)
    
  
def upperEyelidLeftOpen():
  if runtime.isStarted('i01.head.eyelidLeftUpper'):
    i01_head_eyelidLeftUpper.moveTo(180)
    
  
def upperEyelidLeftClose():
  if runtime.isStarted('i01.head.eyelidLeftUpper'):
    i01_head_eyelidLeftUpper.moveTo(0)
    
  
def lowerEyelidLeftOpen():
  if runtime.isStarted('i01.head.eyelidLeftLower'):
    i01_head_eyelidLeftLower.moveTo(180)
    
  
def lowerEyelidLeftClose():
  if runtime.isStarted('i01.head.eyelidLeftLower'):
    i01_head_eyelidLeftLower.moveTo(0)
    

def lowerEyelidLeftU():
  if runtime.isStarted('i01.head.eyelidLeftLower'):
    i01_head_eyelidLeftLower.moveTo(130)
    

###RIGHT EYELIDS ONLY###
def eyelidRightBlink():
  if runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidRightUpper.moveTo(0)
    i01_head_eyelidRightLower.moveTo(0)
    sleep(0.1)
    i01_head_eyelidRightUpper.rest()
    i01_head_eyelidRightLower.rest()
    sleep(0.1)
  
def winkRight():
  if runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidRightUpper.moveTo(0)
    i01_head_eyelidRightLower.moveTo(0)
    sleep(1)
    i01_head_eyelidRightUpper.rest()
    i01_head_eyelidRightLower.rest()
    sleep(0.1)

def eyelidsRightOpen():
  if runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidRightUpper.moveTo(180)
    i01_head_eyelidRightLower.moveTo(180)
    

def eyelidsRightClose():
  if runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidRightUpper.moveTo(0)
    i01_head_eyelidRightLower.moveTo(0)
    

def eyelidsRightHalfShut():
  if runtime.isStarted('i01.head.eyelidRightUpper') and runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidRightUpper.moveTo(70)
    i01_head_eyelidRightLower.moveTo(70)
      
  
def upperEyelidRightOpen():
  if runtime.isStarted('i01.head.eyelidRightUpper'):
    i01_head_eyelidRightUpper.moveTo(180)
    
  
def upperEyelidRightClose():
  if runtime.isStarted('i01.head.eyelidRightUpper'):
    i01_head_eyelidRightUpper.moveTo(0)
    
  
def lowerEyelidRightOpen():
  if runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidRightLower.moveTo(180)
    
  
def lowerEyelidRightClose():
  if runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidRightLower.moveTo(0)
    

def lowerEyelidRightU():
  if runtime.isStarted('i01.head.eyelidRightLower'):
    i01_head_eyelidRightLower.moveTo(130)
      