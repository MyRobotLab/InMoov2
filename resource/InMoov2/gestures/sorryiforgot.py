def sorryiforgot():
  x = (random.randint(1, 2))
  if x == 1:
    i01_mouth.speak("that's alright")
	#i01_mouth.speak(u"все в порядке")
  if x == 2:
    i01_mouth.speak("you forget all the time")
	#i01_mouth.speak(u"Вы всё время забываете")
  i01.finishedGesture()
