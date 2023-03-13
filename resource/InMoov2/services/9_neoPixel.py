# ##############################################################################
#            *** MRL SERVICE - NEOPIXEL  ***
# ##############################################################################

  
# ##############################################################################
#                 SET SERVICE
# ##############################################################################

#i01_neoPixel = runtime.start("i01.neoPixel","Neopixel")
if runtime.isStarted('i01.neoPixel'):
  i01.speakBlocking(i01.localize("STARTINGNEOPIXEL"))
  if boot_green==1:
    i01_neoPixel.setAnimation("Theater Chase", 0, 255, 50, 10)
