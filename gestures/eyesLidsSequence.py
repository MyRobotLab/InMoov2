def eyesLidsSequence():
  #i01.startedGesture()
  if runtime.isStarted(('i01.head.eyelidLeft') and ('i01.head.eyelidRight')):
    i01_mouth.speak("moving my eyelids randomly")
    x = (random.randint(1, 6))
    if x == 1:
      i01_head_eyelidLeft.moveTo(180)
      i01_head_eyelidRight.moveTo(180)
    if x == 2:
      i01_head_eyelidLeft.moveTo(0)
      i01_head_eyelidRight.moveTo(0)
    if x == 3:
      i01_head_eyelidLeft.moveTo(90)
      i01_head_eyelidRight.moveTo(90)
    if x == 4:
      i01_head_eyelidLeft.moveTo(40)
      i01_head_eyelidRight.moveTo(40)
    if x == 5:
      i01_head_eyelidLeft.moveTo(160)
      i01_head_eyelidRight.moveTo(160)
    if x == 6:
      i01_head_eyelidLeft.moveTo(110)
      i01_head_eyelidRight.moveTo(110)
    sleep(0.5)
    i01_mouth.speak("now doing a eyelid sequence")
    i01_head_eyelidLeft.moveTo(110)
    i01_head_eyelidRight.moveTo(110)
    sleep(0.5)
    i01_head_eyelidLeft.moveTo(0)
    i01_head_eyelidRight.moveTo(0)
    sleep(0.5)
    i01_head_eyelidLeft.moveTo(60)
    i01_head_eyelidRight.moveTo(60)
    sleep(0.5)
    i01_head_eyelidLeft.moveTo(180)
    i01_head_eyelidRight.moveTo(180)
    sleep(0.5)
    i01_head_eyelidLeft.moveTo(90)
    i01_head_eyelidRight.moveTo(90)
    i01_mouth.speak("sequence is finished")
    i01.finishedGesture()
