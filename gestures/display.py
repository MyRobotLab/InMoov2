def display(pic):

  try:
    i01_imageDisplay.displayFullScreen(pic)
  except: 
    i01_chatBot.getResponse("PICTUREPROBLEM")
    pass
  i01.finishedGesture()  
 