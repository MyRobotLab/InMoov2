###///PINOUT///###

# i01_head_eyeRightLR.PIN(3)
# i01_head_eyeRightUD.PIN(4)
# i01_head_eyeLeftLR.PIN(5)
# i01_head_eyeLeftUD.PIN(6)

###///EYE MOVEMENT LIST///###

###BOTH EYES SPEED###

#eyesFullSpeed()
#eyesHalfSpeed()
#eyesLowSpeed()

###BOTH EYES###
#eyesC()               /     Centers both eyes
#eyesU()               /     Looks up
#eyesD()               /     Looks down
#eyesL()               /     Looks to the left
#eyesR()               /     Looks to the right
#eyesUL()              /     Eyes look Up/left
#eyesUR()              /     Eyes look Up/right
#eyesDL()              /     Eyes look Down/left
#eyesDR()              /     Eyes look Down/right
#eyesCross()           /     Cross-eye
#eyesRevCross()        /     Reverse cross-eye
#eyesInnerSpin()       /     Spin Eyes Inwards
#eyesOuterSpin()       /     Spin Eyes Outwards
#eyesLeftSpin()        /     Sping Eyes left
#eyesRightSpin()       /     Sping Eyes right


###LEFT EYE ONLY### 
#eyeLeftC()            /     Centers left eye
#eyeLeftU()            /     left eye - Looks up
#eyeLeftD()            /     left eye - Looks down
#eyeLeftL()            /     left eye - Looks left
#eyeLeftR()            /     left eye - Looks right
#eyeLeftUL()           /     left eye - Looks Up/left
#eyeLeftUR()           /     left eye - Looks Up/right
#eyeLeftDL()           /     left eye - Looks Down/left
#eyeLeftDR()           /     left eye - Looks Down/right
#eyeLeftInnerSpin()    /     left Eye - Spin Inwards
#eyeLeftOuterSpin()    /     left Eye - Spin Outwards

###RIGHT EYE ONLY###
#eyeRightC()           /     Centers left eye
#eyeRightU()           /     right eye - Looks up
#eyeRightD()           /     right eye - Looks down
#eyeRightL()           /     right eye - Looks left
#eyeRightR()           /     right eye - Looks right
#eyeRightUL()          /     right eye - Looks Up/left
#eyeRightUR()          /     right eye - Looks Up/right
#eyeRightDL()          /     right eye - Looks Down/left
#eyeRightDR()          /     right eye - Looks Down/right
#eyeRightInnerSpin()   /     right eye - Spin Inwards
#eyeRightOuterSpin()   /     right eye - Spin Outwards


###BOTH EYES SPEED###
def eyesFullSpeed():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeLeftUD.setSpeed(500)
    i01_head_eyeLeftLR.setSpeed(500)
    i01_head_eyeRightUD.setSpeed(500)
    i01_head_eyeRightLR.setSpeed(500)

def eyesHalfSpeed():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeLeftUD.setSpeed(200)
    i01_head_eyeLeftLR.setSpeed(200)
    i01_head_eyeRightUD.setSpeed(200)
    i01_head_eyeRightLR.setSpeed(200)

def eyesLowSpeed():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeLeftUD.setSpeed(20)
    i01_head_eyeLeftLR.setSpeed(20)
    i01_head_eyeRightUD.setSpeed(20)
    i01_head_eyeRightLR.setSpeed(20)


#############################################
###BOTH EYES###
def eyesC():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeLeftUD.rest()
    i01_head_eyeLeftLR.rest()
    i01_head_eyeRightUD.rest()
    i01_head_eyeRightLR.rest()
    sleep(0.01)

def eyesU():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.01)
   
def eyesD():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.01)

def eyesL():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.01)
  
def eyesR():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.01)
  
def eyesUL():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.01)
  
def eyesUR():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.01)
  
def eyesDL():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.01)

def eyesDR():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.01)
    
def eyesCross():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'): 
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.01)
    
def eyesRevCross():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.01)
  
def eyesInnerSpin():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'): 
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
  
def eyesOuterSpin():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'): 
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(0)  
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
  
def eyesLeftSpin():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'): 
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
  
def eyesRightSpin():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR') and runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(0)  
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(0)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(180)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
  
###LEFT EYE ONLY###
def eyeLeftC():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR'): 
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(90)
    sleep(0.01)
  
def eyeLeftU():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR'):
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(90)
    sleep(0.01)
   
def eyeLeftD():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR'):
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(90)
    sleep(0.01)

def eyeLeftL():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR'):
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(180)
    sleep(0.01)
   
def eyeLeftR():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR'):
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(0)
    sleep(0.01)
  
def eyeLeftUL():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR'):
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(180)
    sleep(0.01)
  
def eyeLeftUR():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR'):
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(0)
    sleep(0.01)
  
def eyeLeftDL():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR'):
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(180)
    sleep(0.01)
  
def eyeLeftDR():
  if runtime.isStarted('i01.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR'):
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(0)
    sleep(0.01)
    
def eyeLeftInnerSpin():
  if runtime.isStarted('i01.head.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR'):
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(90)
    sleep(0.025)
    
def eyeLeftOuterSpin():
  if runtime.isStarted('i01.head.head.eyeLeftUD') and runtime.isStarted('i01.head.eyeLeftLR'):
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(0)
    i01_head_eyeLeftLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeLeftUD.moveTo(180)
    i01_head_eyeLeftLR.moveTo(90)
    sleep(0.025)
  
###RIGHT EYE ONLY###
def eyeRightC():
  if runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.01)

def eyeRightU():
  if runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.01)
  
def eyeRightD():
  if runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.01)

def eyeRightL():
  if runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.01)
  
def eyeRightR():
  if runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.01)

def eyeRightUL():
  if runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.01)

def eyeRightUR():
  if runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.01)

def eyeRightDL():
  if runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.01)

def eyeRightDR():
  if runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.01)

def eyeRightInnerSpin():
  if runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)

def eyeRightOuterSpin():
  if runtime.isStarted('i01.head.eyeRightUD') and runtime.isStarted('i01.head.eyeRightLR'):
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(0)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(0)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(180)
    sleep(0.025)
    i01_head_eyeRightUD.moveTo(180)
    i01_head_eyeRightLR.moveTo(90)
    sleep(0.025)