def darkSide():
  if runtime.isStarted('i01.neoPixel'):
    i01_neoPixel.setAnimation("Ironman", 255, 255, 255, 1)
    sleep(1)
    i01_neoPixel.stopAnimation()
    fullspeed()
    i01_head.moveTo(0, 90)
    handsclose()
    i01_audioPlayer.playFile('resource/InMoov2/system/sounds/Darth Vader Breathing.mp3')
    sleep(9)
    relax()
