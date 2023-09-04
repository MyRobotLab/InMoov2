def close_image():
  if runtime.isStarted('i01.imageDisplay'):
    i01_imageDisplay.closeAll()
    i01.finishedGesture()
  else:
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.getResponse("ALERT")
      i01_chatBot.getResponse("SYSTEM_ERROR_IMAGE_DISPLAY_1")
