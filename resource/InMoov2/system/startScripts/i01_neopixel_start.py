#########################################
# i01_neopixel_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

# create a neopixel
i01_neopixel = Runtime.start("i01.neopixel","NeoPixel")
i01.speakBlocking(i01.localize("STARTINGNEOPIXEL"))
enableNeopixel=True
