def ready():
  i01_mouth.speak("ready")
  #i01_mouth.speak(u"готов")
  i01_mouth.speak("go")
  #i01_mouth.speak(u"Вперёд")
  i01.moveHead(90,90)
  i01.moveArm("left",65,90,75,10)
  i01.moveArm("right",20,80,25,20)
  i01.moveHand("left",130,180,180,180,180,90)
  i01.moveHand("right",50,90,90,90,100,90)
  i01.finishedGesture()



