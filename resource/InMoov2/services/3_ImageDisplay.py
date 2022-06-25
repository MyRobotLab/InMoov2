# ##############################################################################
#                 ImageDisplay SERVICE
# ##############################################################################

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

imagedisplay = runtime.start("imagedisplay","ImageDisplay")

def display(pic):
  imagedisplay.closeAll()
  r=imagedisplay.displayFullScreen(pic)
