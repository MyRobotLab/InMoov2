def DisplayPic(pic):
  r=0
  try:
    r=imageDisplay.displayFullScreen(pic,1)
  except: 
    i01_chatBot.getResponse("PICTUREPROBLEM")
    pass
  time.sleep(0.1)
  try:
    r=imageDisplay.displayFullScreen(pic,1)
  except:
      pass
  i01.finishedGesture()