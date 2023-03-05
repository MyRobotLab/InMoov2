def close_image():
  if runtime.isStarted('i01.imageDisplay'):
    i01_imageDisplay.closeAll()
    i01.finishedGesture()
  else:
    errorSpokenFunc("ALERT",", imageDisplay not started")
