def stoprockpaperscissors():
  global inmoov
  global human
  rest()
  sleep(5)
  if inmoov < human:
    i01_mouth.speak("congratulations you won with" + str(human - inmoov) + "points")
    sleep(3)
    i01_mouth.speak(str(human) + "points to you and" + str(inmoov) + "points to me")
  elif inmoov > human:                                                     # changed from if to  elif
    i01_mouth.speak("yes yes i won with" + str(inmoov - human) + "points")
    sleep(3)
    i01_mouth.speak("i've got " + str(inmoov) + "points and you got" + str(human) + "points")
  elif inmoov == human:                                                      # changed from if to  elif
    i01_mouth.speak("none of us won we both got" + str(inmoov) + "points")
  inmoov = 0
  human = 0
  i01_mouth.speak("that was fun")
  sleep(2)
  i01_mouth.speak("do you want to play again")
  sleep(10)
  if (data == "yes let's play again"):
    rockpaperscissors2(data)
  elif (data == "yes"):                                        # changed from if to  elif
    rockpaperscissors2(data)
  elif (data == "no thanks"):                                  # changed from if to  elif
    i01_mouth.speak("maybe some other time")
    sleep(4)
    power_down()
  elif (data == "no thank you"):                               # changed from if to  elif
    i01_mouth.speak("maybe some other time")
    sleep(4)
    power_down()
  ##i01_mouth.speak("ok i'll find something else to do then")
  ##lookaroundyou()
  i01.finishedGesture()


