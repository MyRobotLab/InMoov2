def eyesLidsSequence():
  #i01.startedGesture()
  if isEyeLidsActivated:
    i01_mouth.speak("moving my eyelids randomly")
    x = (random.randint(1, 6))
    if x == 1:
      i01.eyelids.moveTo(180)
    if x == 2:
      i01.eyelids.moveTo(0)
    if x == 3:
      i01.eyelids.moveTo(90)
    if x == 4:
      i01.eyelids.moveTo(40)
    if x == 5:
      i01.eyelids.moveTo(160)
    if x == 6:
      i01.eyelids.moveTo(110)
    sleep(0.5)
    i01_mouth.speak("now doing a eyelid sequence")
    i01.eyelids.moveTo(110)
    sleep(0.5)
    i01.eyelids.moveTo(0)
    sleep(0.5)
    i01.eyelids.moveTo(60)
    sleep(0.5)
    i01.eyelids.moveTo(180)
    sleep(0.5)
    i01.eyelids.moveTo(90)
    i01_mouth.speak("sequence is finished")
    i01.finishedGesture()
