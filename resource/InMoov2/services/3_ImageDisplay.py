# ##############################################################################
#                 ImageDisplay SERVICE
# ##############################################################################

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

i01_imageDisplay = runtime.start("i01.imageDisplay","ImageDisplay")

def display(pic):
  i01_imageDisplay.closeAll()
  r=i01_imageDisplay.displayFullScreen(pic)
