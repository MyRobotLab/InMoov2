def find_image(image):
  if runtime.isStarted('i01.chatBot.search'):
    python.subscribe('i01_chatBot_search', 'publishResults')
    try:
      image = image.decode( 'utf8' )
    except: 
      pass
    images = i01_chatBot_search.imageSearch(image)
    imageDisplay = Runtime.start('imageDisplay','ImageDisplay')
    if runtime.isStarted('imageDisplay'):
      for img in images:
        imageDisplay.displayFullScreen(img)
        sleep(3)
        imageDisplay.closeAll()
    i01.finishedGesture()
