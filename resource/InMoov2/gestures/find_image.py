def find_image(image):
  # FIXME - if you had a reference of a bot e.g. robot = i01
  # then you could robot.startPeer('imageDisplay')
  # wich doesn't need absolute name
  # robot.isPeerStarted('imageDisplay')
  # what you do not want to do is use i01 or absolute paths !!!
  # if not i01.isPeerStarted('imageDisplay'):
    
  # imageDisplay = runtime.getService('i01.imageDisplay')
  # search = runtime.start('i01.search','Wikipedia')
  # search.attach(imageDisplay)
  # search.search(image)
  # print('should print picture of', image)

  # if runtime.isStarted('i01.ChatBot'):
  #   python.subscribe('i01.chatBot', 'publishResults')
  #   try:
  #     image = image.decode( 'utf8' )
  #   except: 
  #     pass
  #   a = i01_chatBot.search(image)
  #   #a = i01_chatBot.search(+urllib2.quote(image).replace(" ", "%20"))
  #   imageDisplay.display(a)
  # else:
  #   google = runtime.start('google','GoogleSearch')
  #   python.subscribe('google', 'publishResults')
  #   try:
  #     image = image.decode( 'utf8' )
  #   except: 
  #     pass
  #   a = google.search(image)  
  #   imageDisplay.display(a)
  #   i01.finishedGesture()

  if runtime.isStarted('i01.chatBot.search'):
    python.subscribe('i01_chatBot_search', 'publishResults')
    try:
      image = image.decode( 'utf8' )
    except: 
      pass
    images = i01_chatBot_search.imageSearch(image)
    i01_imageDisplay = Runtime.start('i01.imageDisplay','ImageDisplay')
    if runtime.isStarted('i01_imageDisplay'):
      for img in images:
        i01_imageDisplay.displayFullScreen(img)
        sleep(3)
        i01_imageDisplay.closeAll()
    i01.finishedGesture()
