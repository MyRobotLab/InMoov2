def find_image(image):
  imageDisplay = runtime.start('i01.imageDisplay','ImageDisplay')
  chatBot_search = runtime.start('i01.chatBot.search','Wikipedia')
  chatBot_search.attach(imageDisplay)
  chatBot_search.search(image)
  print('print picture of', image)
  sleep(3)
  imageDisplay.closeAll()
  
