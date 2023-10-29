def startkinect():
  if runtime.isStarted('i01.openni'):
    openNiInit() 
    i01_openni.run()
    sleep(1)
    i01_openni.capture()
  else:runtime.warn('openni is not started')  