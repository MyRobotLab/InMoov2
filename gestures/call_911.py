def call_911():
  #i01.startedGesture()
  if runtime.isStarted('i01.chatBot'):
    i01_chatBot.getResponse("call_911_1")
  i01.setHandSpeed("left", 500.0, 500.0, 500.0, 500.0, 500.0, 500.0)
  i01.setHandSpeed("right", 500.0, 500.0, 500.0, 500.0, 500.0, 500.0)
  i01.setArmSpeed("left", 500.0, 500.0, 500.0, 500.0)
  i01.setArmSpeed("right", 500.0, 500.0, 500.0, 500.0)
  i01.setHeadSpeed(500.0, 90.0)
  i01.setTorsoSpeed(500.0, 500.0, 500.0)
  i01.moveHead(120,90)
  sleep(0.5)
  i01.moveHead(20,90)
  sleep(0.5)
  i01.moveArm("left",20,93,42,16)
  i01.moveArm("right",20,93,37,18)
  i01.moveHand("left",180,180,65,81,41,143)
  i01.moveHand("right",180,180,18,61,36,21)
  i01.moveTorso(90,90,90)
  sleep(1.5)
  i01_audioPlayer.playFileBlocking('resource/InMoov2/system/sounds/Notifications/alarm.wav')
  sleep(0.5)
  i01_audioPlayer.playFileBlocking('resource/InMoov2/system/sounds/911.mp3')
  sleep(0.5)
  if runtime.isStarted('i01.chatBot'):
    i01_chatBot.getResponse("call_911_2")
  i01.moveHead(90,90)
  sleep(0.5)
  i01.finishedGesture()
  relax()
