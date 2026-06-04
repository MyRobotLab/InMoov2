def ultrasonic(returnText):
  i01.speakBlocking(unicode(returnText,'utf-8')+str(i01.getUltrasonicRightDistance()).replace(".0", ""))
  sleep(0.5)
  i01.speakBlocking(unicode(returnText,'utf-8')+str(i01.getUltrasonicLeftDistance()).replace(".0", ""))
  print("right side:"+ str(i01.getUltrasonicRightDistance()).replace(".0", "")+ "cm")
  print("left side:"+ str(i01.getUltrasonicLeftDistance()).replace(".0", "")+ "cm")
  
