def Powerglove():
  # WE CONNECT THE POWER GLOVE TO THE SENSOR SHIELD
  if runtime.isStarted('i01.rightHand'):
    #i01.startedGesture()
    i01.setHandSpeed("right", 80 ,80 ,80 ,80 ,80 ,80)
    
    #TO BE CONTINUED
    
    
    i01.finishedGesture()
  
