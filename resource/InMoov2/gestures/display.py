def display(pic):

  try:
    i01.displayFullScreen(pic)
  except: 
    inmoovWebKit.getResponse("PICTUREPROBLEM")
    pass
 