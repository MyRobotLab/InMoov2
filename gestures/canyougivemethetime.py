def canyougivemethetime():
  #i01.startedGesture()
  i01_mouth.speak("sure")
  #i01_mouth.speak(u"конечно")
  fullspeed()
  i01.setHandSpeed("left", 43.0, 43.0, 43.0, 43.0, 43.0, 100.0)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 59, 59, 59, 43.0)
  i01.setArmSpeed("left", 59, 59, 59, 43.0)
  i01.setHeadSpeed(31.0, 31.0)
  #1
  i01.moveHead(20,100,85,85,65)
  i01.moveArm("left",47,86,41,14)
  i01.moveArm("right",5,82,28,15)
  i01.moveHand("left",180,180,180,180,180,119)
  i01.moveHand("right",20,40,40,30,30,72)
  i01.moveTorso(90,90,90)
  sleep(1)
  #2
  i01.moveHead(20,100,85,85,65)
  i01.moveArm("left",47,86,41,14)
  i01.moveArm("right",60,82,28,15)
  i01.moveHand("left",180,180,180,180,180,119)
  i01.moveHand("right",138,40,180,145,139,156)
  i01.moveTorso(90,90,90)
  sleep(1)
  #3
  i01.moveHead(20,100,85,85,65)
  i01.moveArm("left",47,86,41,14)
  i01.moveArm("right",67,40,47,15)
  i01.moveHand("left",180,180,180,180,180,119)
  i01.moveHand("right",138,40,180,145,139,156)
  i01.moveTorso(90,90,90)
  sleep(1)
  #4
  i01.moveHead(20,100,85,85,65)
  i01.moveArm("left",14,86,55,14)
  i01.moveArm("right",67,40,47,15)
  i01.moveHand("left",180,180,180,180,180,119)
  i01.moveHand("right",138,40,180,145,139,156)
  i01.moveTorso(90,90,90)
  sleep(1)
  #5
  i01.moveHead(20,100,85,85,65)
  i01.moveArm("left",14,71,62,14)
  i01.moveArm("right",67,40,47,15)
  i01.moveHand("left",180,180,180,180,180,119)
  i01.moveHand("right",138,40,180,145,139,156)
  i01.moveTorso(90,90,90)
  sleep(1)
  #6
  i01.moveHead(20,100,85,85,65)
  i01.moveArm("left",20,66,66,14)
  i01.moveArm("right",73,40,47,15)
  i01.moveHand("left",180,180,180,180,180,119)
  i01.moveHand("right",138,40,180,145,139,156)
  i01.moveTorso(90,90,90)
  sleep(1)
  #7
  i01.moveHead(20,100,85,85,65)
  i01.moveArm("left",23,66,66,14)
  i01.moveArm("right",78,40,47,15)
  i01.moveHand("left",180,180,180,180,180,119)
  i01.moveHand("right",138,40,180,145,139,156)
  i01.moveTorso(90,90,90)
  sleep(2)
  #8
  i01.moveHead(20,100,85,85,65)
  i01.moveArm("left",23,60,66,14)
  i01.moveArm("right",78,40,47,15)
  i01.moveHand("left",180,180,180,180,180,119)
  i01.moveHand("right",138,40,180,145,139,156)
  i01.moveTorso(90,90,90)
  sleep(2)
  #9
  i01_chatBot.getResponse('TIME')
  i01.moveHead(20,100,85,85,65)
  i01.moveArm("left",25,120,41,31)
  i01.moveArm("right",5,82,28,15)
  i01.moveHand("left",180,180,180,180,180,35)
  i01.moveHand("right",20,40,40,30,30,72)
  i01.moveTorso(90,90,90)
  sleep(3)
  i01.finishedGesture()
  relax()
   
