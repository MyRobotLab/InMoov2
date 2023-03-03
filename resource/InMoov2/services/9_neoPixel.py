# ##############################################################################
#            *** MRL SERVICE - NEOPIXEL  ***
# ##############################################################################

  
# ##############################################################################
#                 SET SERVICE
# ##############################################################################

#neopixel = runtime.start("neopixel","Neopixel")
  if runtime.isStarted('i01.neopixel'):
    i01.speakBlocking(i01.localize("STARTINGNEOPIXEL"))
    if boot_green:
      i01.setNeopixelAnimation("Theater Chase", 0, 255, 50, 1)
