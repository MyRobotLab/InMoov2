###///EYEBROW MOVEMENT LIST///###

###///PINOUT///###

# i01_head_eyebrowRight.PIN(11)
# i01_head_eyebrowLeft.PIN(14)

###BOTH EYEBROWS###


#browsC()                          /       Centers Eyebrows
#browsU()                          /       Raises Eyebrows
#browsD()                          /       Lowers Eyebrows
#browsLURD()                       /       Raises left Eyebrow   / Lowers right Eyebrow
#browsRULD()                       /       Raises right Eyebrow  / Lowers left Eyebrow

###LEFT EYEBROW ONLY###

#browLeftC()                       /       Centers left Eyebrow
#browLeftU()                       /       Raises left Eyebrow
#BrowLeftD()                       /       Lowers left Eyebrow


###RIGHT EYEBROW ONLY### 

#browRightC()                   /       Centers right Eyebrow
#browRightU()                   /       Raises right Eyebrow
#browRightD()                   /       Lowers right Eyebrow

###BOTH EYEBROWS###
def browsC():
  if runtime.isStarted('i01.head.eyebrowLeft') and runtime.isStarted('i01.head.eyebrowRight'):
    i01_head_eyebrowRight.rest()
    i01_head_eyebrowLeft.rest()
    sleep(0.1)

def browsU():
  if runtime.isStarted('i01.head.eyebrowLeft') and runtime.isStarted('i01.head.eyebrowRight'):
    i01_head_eyebrowRight.moveTo(180)
    i01_head_eyebrowLeft.moveTo(180)
    sleep(0.1)  

def browsD():
  if runtime.isStarted('i01.head.eyebrowLeft') and runtime.isStarted('i01.head.eyebrowRight'):
    i01_head_eyebrowRight.moveTo(0)
    i01_head_eyebrowLeft.moveTo(0)
    sleep(0.1)  

def browsLURD():
  if runtime.isStarted('i01.head.eyebrowLeft') and runtime.isStarted('i01.head.eyebrowRight'):
    i01_head_eyebrowRight.moveTo(180)
    i01_head_eyebrowLeft.moveTo(0)
    sleep(0.1)  

def browsRULD():
  if runtime.isStarted('i01.head.eyebrowLeft') and runtime.isStarted('i01.head.eyebrowRight'):
    i01_head_eyebrowRight.moveTo(0)
    i01_head_eyebrowLeft.moveTo(180)
    sleep(0.1)       
  
###LEFT EYEBROW ONLY### 
def browLeftC():
  if runtime.isStarted('i01.head.eyebrowLeft'):
    i01_head_eyebrowLeft.moveTo(90)
    sleep(0.1)    
 
def browLeftU():
  if runtime.isStarted('i01.head.eyebrowLeft'):
    i01_head_eyebrowLeft.moveTo(180)
    sleep(0.1)
  
def browLeftD():
  if runtime.isStarted('i01.head.eyebrowLeft'):
    i01_head_eyebrowLeft.moveTo(0)
    sleep(0.1)

  ###RIGHT EYEBROW ONLY### 
def browRightC():
  if runtime.isStarted('i01.head.eyebrowRight'):
    i01_head_eyebrowRight.moveTo(90)
    sleep(0.1)    
 
def browRightU():
  if runtime.isStarted('i01.head.eyebrowRight'):
    i01_head_eyebrowRight.moveTo(180)
    sleep(0.1)
  
def browRightD():
  if runtime.isStarted('i01.head.eyebrowRight'):
    i01_head_eyebrowRight.moveTo(0)
    sleep(0.1)      
