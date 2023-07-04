def iknow():
  x = (random.randint(1, 3))
  if x == 1:
    i01_mouth.speak("yes, me too")
	#i01_mouth.speak(u"Да, я тоже")
  if x == 2:
    i01_mouth.speak("I do too")
	#i01_mouth.speak(u"я тоже")
  if x == 3:
    i01_mouth.speak("sorry about that")
	#i01_mouth.speak(u"Извини за это")
  i01.finishedGesture()
