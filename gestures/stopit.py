def stopit():
  lookinmiddle()
  sleep(1)
  relax()
  i01_mouth.speak("yes")
  #i01_mouth.speak(u"да")
  if (data == "pause"):# пауза
    i01_mouth.speak("yes")
	#i01_mouth.speak(u"да")
  i01.finishedGesture()

