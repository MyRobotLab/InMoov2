###///MOUTH MOVEMENT LIST///###

###BOTH Cheeks###

#CheeksNeutral()                    /       Rest Cheeks
#cheeksC()                          /       Centers Cheeks
#cheeksU()                          /       Raises Cheeks
#cheeksD()                          /       Lowers Cheeks
#cheeksLURD()                       /       Raises left Cheek   / Lowers right Cheek
#cheeksRULD()                       /       Raises right Cheek  / Lowers left Cheek

###LEFT CHEEK ONLY###

#cheekLeftNeutral()              /       Rest left Cheek
#cheekLeftC()                    /       Centers left Cheek
#cheekLeftU()                    /       Raises left Cheek
#cheekLeftD()                    /       Lowers left Cheek

###RIGHT CHEEK ONLY### 

#cheekRightNeutral()             /       Rest right Cheek
#cheekRightC()                   /       Centers right Cheek
#cheekRightU()                   /       Raises right Cheek
#cheekRightD()                   /       Lowers right Cheek

###UPPER LIP###

#upperLipC()                          /       Centers UpperLip
#upperLipU()                          /       Raises UpperLip
#upperLipD()                          /       Lowers UpperLip

###FORHEAD###

#forHeadC()                          /       Centers ForHead
#forHeadU()                          /       Raises ForHead
#forHeadD()                          /       Lowers ForHead


###BOTH CHEEKS###
def cheeksNeutral():
  if runtime.isStarted('i01.cheekLeft') and runtime.isStarted('i01.cheekRight'):
    i01_cheekRight.rest()
    i01_cheekLeft.rest()

def cheeksC():
  if runtime.isStarted('i01.cheekLeft') and runtime.isStarted('i01.cheekRight'):
    i01_cheekRight.moveTo(90)
    i01_cheekLeft.moveTo(90)

def cheeksU():
  if runtime.isStarted('i01.cheekLeft') and runtime.isStarted('i01.cheekRight'):
    i01_cheekRight.moveTo(180)
    i01_cheekLeft.moveTo(180)
    sleep(0.01)  
   
def cheeksD():
  if runtime.isStarted('i01.cheekLeft') and runtime.isStarted('i01.cheekRight'):
    i01_cheekRight.moveTo(0)
    i01_cheekLeft.moveTo(0)
    sleep(0.01)

#############################################


def cheeksLURD():
  if runtime.isStarted('i01.cheekLeft') and runtime.isStarted('i01.cheekRight'):
    i01_cheekRight.moveTo(0)
    i01_cheekLeft.moveTo(180)
    sleep(0.1)  

def cheeksRULD():
  if runtime.isStarted('i01.cheekLeft') and runtime.isStarted('i01.cheekRight'):
    i01_cheekRight.moveTo(180)
    i01_cheekLeft.moveTo(0)
    sleep(0.1)       
  
###LEFT CHEEK ONLY###

def cheekLeftNeutral():
  if runtime.isStarted('i01.cheekLeft'):
    i01_cheekLeft.rest()
    sleep(0.1)

def cheekLeftC():
  if runtime.isStarted('i01.cheekLeft'):
    i01_cheekLeft.moveTo(90)
    sleep(0.1)    
 
def cheekLeftU():
  if runtime.isStarted('i01.cheekLeft'):
    i01_cheekLeft.moveTo(180)
    sleep(0.1)
  
def cheekLeftD():
  if runtime.isStarted('i01.cheekLeft'):
    i01_cheekLeft.moveTo(0)
    sleep(0.1)
  
  ###RIGHT CHEEK ONLY###

def cheekRightNeutral():
  if runtime.isStarted('i01.cheekRight'):
    i01_cheekRight.rest()
    sleep(0.1)

def cheekRightC():
  if runtime.isStarted('i01.cheekRight'):
    i01_cheekRight.moveTo(90)
    sleep(0.1)
 
def cheekRightU():
  if runtime.isStarted('i01.cheekRight'):
    i01_cheekRight.moveTo(180)
    sleep(0.1)
  
def cheekRightD():
  if runtime.isStarted('i01.cheekRight'):
    i01_cheekRight.moveTo(0)
    sleep(0.1)

def upperLipC():
  if runtime.isStarted('i01.upperLip'):
    i01_upperLip.rest()
    sleep(0.1)

def upperLipU():
  if runtime.isStarted('i01.upperLip'):
    i01_upperLip.moveTo(180)
    sleep(0.1)

def upperLipD():
  if runtime.isStarted('i01.upperLip'):
    i01_upperLip.moveTo(0)
    sleep(0.1)

def forHeadC():
  if runtime.isStarted('i01.forHead'):
    i01_forHead.rest()
    sleep(0.1)

def forHeadU():
  if runtime.isStarted('i01.forHead'):
    i01_forHead.moveTo(180)
    sleep(0.1)

def forHeadD():
  if runtime.isStarted('i01.forHead'):
    i01_forHead.moveTo(0)
    sleep(0.1)  
