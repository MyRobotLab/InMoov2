def find_image(image):
  if isChatBotActivated:
    python.subscribe('i01.chatBot', 'publishResults')
    try:
      image = image.decode( 'utf8' )
    except: 
      pass
    a = i01_chatBot.search(image)
    #a = i01_chatBot.search(+urllib2.quote(image).replace(" ", "%20"))
    display(a)
  else:
    google = Runtime.start('google','GoogleSearch')
    python.subscribe('google', 'publishResults')
    try:
      image = image.decode( 'utf8' )
    except: 
      pass
    a = google.search(image)  
    display(a)
