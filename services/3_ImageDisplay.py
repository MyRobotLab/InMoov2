# ##############################################################################
#                 ImageDisplay SERVICE
# ##############################################################################

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

def display(pic):
  if runtime.isStarted('i01.imageDisplay'):
    i01_imageDisplay.closeAll()
    r=i01_imageDisplay.displayFullScreen(pic)
  else:
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.getResponse("ALERT")
      i01_chatBot.getResponse("SYSTEM_ERROR_IMAGE_DISPLAY_1")
    if i01.getConfig().neoPixelErrorRed==1:
      if runtime.isStarted('i01.neoPixel'):
        i01_neoPixel.setAnimation("Theater Chase", 255, 0, 0, 50)
