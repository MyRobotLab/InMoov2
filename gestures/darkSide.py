def darkSide():
  fullspeed()    
  if runtime.isStarted('i01.neoPixel'):
    i01_neoPixel.setAnimation("Ironman", 255, 0, 17, 50)
    i01_head.moveTo(0, 90)
    handsclose()
    i01_audioPlayer.playFile('resource/InMoov2/system/sounds/Darth Vader Breathing.mp3')
    sleep(9)
    i01_neoPixel.clear()
    relax()
