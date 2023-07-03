# ##############################################################################
#                 INMOOV SERVICE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

inMoov=i01
#temporary speed simulation trick ( i2c can compute speed )
if ScriptType=="Virtual":
  Platform.setVirtual(True)
  # right = runtime.start("i01.right", "Adafruit16CServoDriver")
  # left = runtime.start("i01.left", "Adafruit16CServoDriver")
  # virtualRaspi = runtime.start("virtualRaspi","RasPi")
  # virtualRaspi.setWiringPi(False)
  # left.attach(virtualRaspi,"1","0x40")
  # right.attach(virtualRaspi,"1","0x41")
  right = runtime.start("i01.right", "Arduino")
  left = runtime.start("i01.left", "Arduino")

  RightPortIsConnected=True
  LeftPortIsConnected=True

#Inmoov Left / right arduino connect
if ScriptType=="RightSide" or ScriptType=="Full":
  right = runtime.start("i01.right", "Arduino")
  right.setBoard(BoardTypeMyRightPort)
  RightPortIsConnected=CheckArduinos(right,MyRightPort)
  if RightPortIsConnected:right.setAref(ArefRightArduino)


if ScriptType=="LeftSide" or ScriptType=="Full":
  left = runtime.start("i01.left", "Arduino")
  left.setBoard(BoardTypeMyLeftPort)
  LeftPortIsConnected=CheckArduinos(left,MyLeftPort)
  if LeftPortIsConnected:left.setAref(ArefLeftArduino)
  
if ScriptType=="LeftSide":i01.speakBlocking(i01.localize("STARTINGLEFTONLY"))
if ScriptType=="RightSide":i01.speakBlocking(i01.localize("STARTINGRIGHTONLY"))
if ScriptType=="Full":i01.speakBlocking(i01.localize("STARTINGFULL"))
if ScriptType=="NoArduino":i01.speakBlocking(i01.localize("STARTINGNOARDUINO"))


