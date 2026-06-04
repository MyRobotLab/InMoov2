def ultrasonicRight(returnText):
  i01.speakBlocking(unicode(returnText,'utf-8')+str(i01.getUltrasonicRightDistance()).replace(".0", ""))
  print("right side:"+ str(i01.getUltrasonicRightDistance()).replace(".0", "")+ "cm")
