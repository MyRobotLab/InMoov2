def find_image(image):
  imageDisplay = runtime.start('i01.imageDisplay','ImageDisplay')
  chatBot_search = runtime.start('i01.chatBot.search','Wikipedia')
  chatBot_search.attach(imageDisplay)
  chatBot_search.search(image)
  print('print picture of', image)

  if runtime.isStarted('i01.ChatBot'):
    python.subscribe('i01.chatBot', 'publishResults')
    try:
      image = image.decode( 'utf8' )
    except: 
      pass
      a = i01_chatBot.search(image)
      #a = i01_chatBot.search(+urllib2.quote(image).replace(" ", "%20"))
      imageDisplay.display(a)
      sleep(3)
      imageDisplay.closeAll()
      i01.finishedGesture()
      
