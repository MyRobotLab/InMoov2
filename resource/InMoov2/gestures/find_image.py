def find_image(image):
  if runtime.isStarted('i01.ChatBot'):
    python.subscribe('i01.chatBot', 'publishResults')
    try:
      image = image.decode( 'utf8' )
    except: 
      pass
    a = i01_chatBot.search(image)
    #a = i01_chatBot.search(+urllib2.quote(image).replace(" ", "%20"))
    imageDisplay.display(a)
  else:
    google = Runtime.start('google','GoogleSearch')
    python.subscribe('google', 'publishResults')
    try:
      image = image.decode( 'utf8' )
    except: 
      pass
    a = google.search(image)  
    imageDisplay.display(a)
    i01.finishedGesture()

