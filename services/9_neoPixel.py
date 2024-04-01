# ##############################################################################
#            *** MRL SERVICE - NEOPIXEL  ***
# ##############################################################################

  
# ##############################################################################
#                 SET SERVICE
# ##############################################################################

# if runtime.isStarted('i01.neoPixel'):
#   if i01.getConfig().neoPixelBootGreen==1:
#     i01_neoPixel.setAnimation("Theater Chase", 0, 255, 50, 10)
def errors():
  if i01.getConfig().neoPixelErrorRed==1:
      if runtime.isStarted('i01.neoPixel'):
        i01_neoPixel.setAnimation("Theater Chase", 255, 0, 0, 50)
        sleep(4)
        i01_neoPixel.clear()
