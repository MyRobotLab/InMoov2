###///MOUTH MOVEMENT LIST///###

###BOTH CHEEKS###

#cheeksNeutral()                    /       Rest Cheeks
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

#upperLipNeutral()               /       Rest UpperLip
#upperLipC()                     /       Centers UpperLip
#upperLipU()                     /       Raises UpperLip
#upperLipD()                     /       Lowers UpperLip

###BOTH FORHEADS###

#forheadsNeutral()                    /       Rest Forheads
#forheadsC()                          /       Centers Forheads
#forheadsU()                          /       Raises Forheads
#forheadsD()                          /       Lowers Forheads
#forheadsLURD()                       /       Raises left Forhead   / Lowers right Forhead
#forheadsRULD()                       /       Raises right Forhead  / Lowers left Forhead 

###RIGHT FORHEAD ONLY###

#forheadRightNeutral()           /       Rest right forhead
#forheadRightC()                 /       Centers right forhead
#forheadRightU()                 /       Raises right forhead
#forheadRightD()                 /       Lowers right forhead

###LEFT FORHEAD ONLY###

#forheadLeftNeutral()           /       Rest left forhead
#forheadLeftC()                 /       Centers left forhead
#forheadLeftU()                 /       Raises left forhead
#forheadLeftD()                 /       Lowers left forhead


###BOTH CHEEKS###
def cheeksNeutral():
  if runtime.isStarted('i01.head.cheekLeft') and runtime.isStarted('i01.head.cheekRight'):
    i01_head_cheekRight.rest()
    i01_head_cheekLeft.rest()

def cheeksC():
  if runtime.isStarted('i01.head.cheekLeft') and runtime.isStarted('i01.head.cheekRight'):
    i01_head_cheekRight.moveTo(90)
    i01_head_cheekLeft.moveTo(90)

def cheeksU():
  if runtime.isStarted('i01.head.cheekLeft') and runtime.isStarted('i01.head.cheekRight'):
    i01_head_cheekRight.moveTo(180)
    i01_head_cheekLeft.moveTo(180)
    sleep(0.01)  
   
def cheeksD():
  if runtime.isStarted('i01.head.cheekLeft') and runtime.isStarted('i01.head.cheekRight'):
    i01_head_cheekRight.moveTo(0)
    i01_head_cheekLeft.moveTo(0)
    sleep(0.01)

#############################################


def cheeksLURD():
  if runtime.isStarted('i01.head.cheekLeft') and runtime.isStarted('i01.head.cheekRight'):
    i01_head_cheekRight.moveTo(0)
    i01_head_cheekLeft.moveTo(180)
    sleep(0.1)  

def cheeksRULD():
  if runtime.isStarted('i01.head.cheekLeft') and runtime.isStarted('i01.head.cheekRight'):
    i01_head_cheekRight.moveTo(180)
    i01_head_cheekLeft.moveTo(0)
    sleep(0.1)       
  
###LEFT CHEEK ONLY###

def cheekLeftNeutral():
  if runtime.isStarted('i01.head.cheekLeft'):
    i01_head_cheekLeft.rest()
    sleep(0.1)

def cheekLeftC():
  if runtime.isStarted('i01.head.cheekLeft'):
    i01_head_cheekLeft.moveTo(90)
    sleep(0.1)    
 
def cheekLeftU():
  if runtime.isStarted('i01.head.cheekLeft'):
    i01_head_cheekLeft.moveTo(180)
    sleep(0.1)
  
def cheekLeftD():
  if runtime.isStarted('i01.head.cheekLeft'):
    i01_head_cheekLeft.moveTo(0)
    sleep(0.1)
  
  ###RIGHT CHEEK ONLY###

def cheekRightNeutral():
  if runtime.isStarted('i01.head.cheekRight'):
    i01_head_cheekRight.rest()
    sleep(0.1)

def cheekRightC():
  if runtime.isStarted('i01.head.cheekRight'):
    i01_head_cheekRight.moveTo(90)
    sleep(0.1)
 
def cheekRightU():
  if runtime.isStarted('i01.head.cheekRight'):
    i01_head_cheekRight.moveTo(180)
    sleep(0.1)
  
def cheekRightD():
  if runtime.isStarted('i01.head.cheekRight'):
    i01_head_cheekRight.moveTo(0)
    sleep(0.1)

def upperLipNeutral():
  if runtime.isStarted('i01.head.upperLip'):
    i01_head_upperLip.rest()
    sleep(0.1)

def upperLipC():
  if runtime.isStarted('i01.head.upperLip'):
    i01_head_upperLip.moveTo(90)
    sleep(0.1)

def upperLipU():
  if runtime.isStarted('i01.head.upperLip'):
    i01_head_upperLip.moveTo(180)
    sleep(0.1)

def upperLipD():
  if runtime.isStarted('i01.head.upperLip'):
    i01_head_upperLip.moveTo(0)
    sleep(0.1)

###BOTH FORHEADS###

def forheadsNeutral():
  if runtime.isStarted('i01.head.forheadLeft') and runtime.isStarted('i01.head.forheadRight'):
    i01_head_forheadRight.rest()
    i01_head_forheadLeft.rest()

def forheadsC():
  if runtime.isStarted('i01.head.forheadLeft') and runtime.isStarted('i01.head.forheadRight'):
    i01_head_forheadRight.moveTo(90)
    i01_head_forheadLeft.moveTo(90)

def forheadsU():
  if runtime.isStarted('i01.head.forheadLeft') and runtime.isStarted('i01.head.forheadRight'):
    i01_head_forheadRight.moveTo(180)
    i01_head_forheadLeft.moveTo(180)
    sleep(0.01)  
   
def forheadsD():
  if runtime.isStarted('i01.head.forheadLeft') and runtime.isStarted('i01.head.forheadRight'):
    i01_head_forheadRight.moveTo(0)
    i01_head_forheadLeft.moveTo(0)
    sleep(0.01)

#############################################


def forheadsLURD():
  if runtime.isStarted('i01.head.forheadLeft') and runtime.isStarted('i01.head.forheadRight'):
    i01_head_forheadRight.moveTo(0)
    i01_head_forheadLeft.moveTo(180)
    sleep(0.1)  

def forheadsRULD():
  if runtime.isStarted('i01.head.forheadLeft') and runtime.isStarted('i01.head.forheadRight'):
    i01_head_forheadRight.moveTo(180)
    i01_head_forheadLeft.moveTo(0)
    sleep(0.1)     

###RIGHT FORHEAD ONLY###

def forheadRightNeutral():
  if runtime.isStarted('i01.head.forheadRight'):
    i01_head_forheadRight.rest()
    sleep(0.1)

def forheadRightC():
  if runtime.isStarted('i01.head.forheadRight'):
    i01_head_forheadRight.moveTo(90)
    sleep(0.1)

def forheadRightU():
  if runtime.isStarted('i01.head.forheadRight'):
    i01_head_forheadRight.moveTo(180)  
    sleep(0.1)

def forheadRightD():
  if runtime.isStarted('i01.head.forheadRight'):
    i01_head_forheadRight.moveTo(0) 
    sleep(0.1)

###LEFT FORHEAD ONLY###

def forheadLeftNeutral():
  if runtime.isStarted('i01.head.forheadLeft'):
    i01_head_forheadLeft.rest()
    sleep(0.1)    

def forheadLeftC():
  if runtime.isStarted('i01.head.forheadLeft'):
    i01_head_forheadLeft.moveTo(90)  
    sleep(0.1)

def forheadLeftU():
  if runtime.isStarted('i01.head.forheadLeft'):
    i01_head_forheadLeft.moveTo(180)  
    sleep(0.1)

def forheadLeftD():
  if runtime.isStarted('i01.head.forheadLeft'):
    i01_head_forheadLeft.moveTo(0)  
    sleep(0.1)