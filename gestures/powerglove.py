def Powerglove():
  # WE CONNECT THE POWER GLOVE TO THE SENSOR SHIELD
  if i01.isRightHandActivated()==1:
    i01.startedGesture()
    i01.setRightHandVelocity(80,80,80,80,80,80)
    
    #TO BE CONTINUED
    
    
    i01.finishedGesture()
  
