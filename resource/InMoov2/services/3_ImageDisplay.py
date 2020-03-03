# ##############################################################################
#                 ImageDisplay SERVICE
# ##############################################################################

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

imagedisplay = Runtime.start("imagedisplay","ImageDisplay")

def display(pic):
  imagedisplay.closeAll()
  r=imagedisplay.displayFullScreen(pic)
