###///EYEBROW MOVEMENT LIST///###

###BOTH EYEBROWS###


#browsC()                          /       Centers Eyebrows
#browsU()                          /       Raises Eyebrows
#browsD()                          /       Lowers Eyebrows
#browinnerUouterD()                /       Raises Inner Eyebrows / Lowers Outer Eyebrows
#browsouterUinnerD()               /       Raises Outer Eyebrows / Lowers Inner Eyebrows
#browsLURD()                       /       Raises left Eyebrow   / Lowers right Eyebrow
#browsRULD()                       /       Raises right Eyebrow  / Lowers left Eyebrow

###LEFT EYEBROW ONLY###

#browLeftC()                       /       Centers left Eyebrow
#browLeftU()                       /       Raises left Eyebrow
#BrowLeftD()                    /       Lowers left Eyebrow


###RIGHT EYEBROW ONLY### 

#BrowRightC()                   /       Centers right Eyebrow
#BrowRightU()                   /       Raises right Eyebrow
#BrowRightD()                   /       Lowers right Eyebrow

###BOTH EYEBROWS###
def browsC():
  if runtime.isStarted('i01.eyeBrowLeft') and runtime.isStarted('i01.eyeBrowRight'):
    i01_eyeBrowRight.rest()
    i01_eyeBrowLeft.rest()
    sleep(0.1)

def browsU():
  if runtime.isStarted('i01.eyeBrowLeft') and runtime.isStarted('i01.eyeBrowRight'):
    i01_eyeBrowRight.moveTo(180)
    i01_eyeBrowLeft.moveTo(180)
    sleep(0.1)  

def browsD():
  if runtime.isStarted('i01.eyeBrowLeft') and runtime.isStarted('i01.eyeBrowRight'):
    i01_eyeBrowRight.moveTo(0)
    i01_eyeBrowLeft.moveTo(0)
    sleep(0.1)  

def browsLURD():
  if runtime.isStarted('i01.eyeBrowLeft') and runtime.isStarted('i01.eyeBrowRight'):
    i01_eyeBrowRight.moveTo(180)
    i01_eyeBrowLeft.moveTo(0)
    sleep(0.1)  

def browsRULD():
  if runtime.isStarted('i01.eyeBrowLeft') and runtime.isStarted('i01.eyeBrowRight'):
    i01_eyeBrowRight.moveTo(0)
    i01_eyeBrowLeft.moveTo(180)
    sleep(0.1)       
  
###LEFT EYEBROW ONLY### 
def browLeftC():
  if runtime.isStarted('i01.eyeBrowLeft'):
    i01_eyeBrowLeft.moveTo(90)
    sleep(0.1)    
 
def browLeftU():
  if runtime.isStarted('i01.eyeBrowLeft'):
    i01_eyeBrowLeft.moveTo(180)
    sleep(0.1)
  
def browLeftD():
  if runtime.isStarted('i01.eyeBrowLeft'):
    i01_eyeBrowLeft.moveTo(0)
    sleep(0.1)

  ###RIGHT EYEBROW ONLY### 
def browRightC():
  if runtime.isStarted('i01.eyeBrowRight'):
    i01_eyeBrowRight.moveTo(90)
    sleep(0.1)    
 
def browRightU():
  if runtime.isStarted('i01.eyeBrowRight'):
    i01_eyeBrowRight.moveTo(180)
    sleep(0.1)
  
def browRightD():
  if runtime.isStarted('i01.eyeBrowRight'):
    i01_eyeBrowRight.moveTo(0)
    sleep(0.1)      
