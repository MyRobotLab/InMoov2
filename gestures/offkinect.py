def offkinect():
  if runtime.isStarted('i01.openni'):
    i01_openni.stopCapture()
    openNiStop()
    #i01.copyGesture(False)
    i01.finishedGesture()
    rest()
  else:runtime.warn('openni is not started')  
