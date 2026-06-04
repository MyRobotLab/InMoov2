def ultrasonicLeft(returnText):
  i01.speakBlocking(unicode(returnText,'utf-8')+str(i01.getUltrasonicLeftDistance()).replace(".0", ""))
  print("left side:"+ str(i01.getUltrasonicLeftDistance()).replace(".0", "")+ "cm")
