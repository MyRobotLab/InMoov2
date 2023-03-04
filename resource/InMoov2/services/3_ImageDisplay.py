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
    errorSpokenFunc("ALERT",", imageDisplay not started")
    if error_red==1:
      if runtime.isStarted('i01.neopixel'):
        i01.setNeopixelAnimation("Flash Random", 255, 0, 0, 5)
