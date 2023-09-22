def howdoyoudo():
  global helvar
  if helvar <= 2:
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.getResponse("HOWDOYOUDO_1")
    helvar += 1
  elif helvar == 3:
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.getResponse("HOWDOYOUDO_2")
    i01.moveArm("left",43,88,22,10)
    i01.moveArm("right",20,90,30,10)
    i01.moveHand("left",0,0,0,0,0,119)
    i01.moveHand("right",0,0,0,0,0,119)
    sleep(2)
    relax()
    helvar += 1
  elif helvar == 4:
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.getResponse("HOWDOYOUDO_3")
    i01.moveArm("left",30,83,22,10)
    i01.moveArm("right",40,85,30,10)
    i01.moveHand("left",130,180,180,180,180,119)
    i01.moveHand("right",130,180,180,180,180,119)
    sleep(1.5)
    relax()
    helvar += 1
  elif helvar == 5:
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.getResponse("HOWDOYOUDO_4")
    unhappy()
    sleep(3)
    relax()
    helvar += 1
  elif helvar == 6:
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.getResponse("HOWDOYOUDO_5")
    tiltHeadAgree()
    helvar = 0  
  i01_chatBot.setPredicate("parameterHowDoYouDo",str(helvar))
  i01.finishedGesture()
