#########################################
# i01_InMoovCustom_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

import os
ThisFilePart = 'data/InMoov2/InMoovCustom.py'
customFilename="InMoovCustom.py"

def saveCustom(customFilename):
    customPath='data/InMoov2/'
    customFile = customFilename
    customWriter = 0
    customWriter = open(customPath+customFile, "w+")
    L =[
    "###############################################################################\n"
    "# InMoovCustom.py\n"
    "# categories: inmoov2\n"
    "# more info @: http://myrobotlab.org/service/InMoov\n"
    "# #############################################################################\n"
    "# YOUR INMOOV CUSTOM SCRIPT\n"
    "# Here you can add your own commands to play and test with InMoov\n"
    "# Those commands are safe, you can copy them to your other MRL versions\n"
    "# ##############################################################################\n"


    "## sample:\n"
    "## play a neopixel animation while the robot speaking\n"
    "#PlayNeopixelAnimation('Flash Random', 255, 255, 255, 1)\n"
    "## talk something\n"
    "#i01_mouth.speakBlocking('he is a replicant, or not?')\n"
    "## stop neopixel\n"
    "#StopNeopixelAnimation()\n"
    "## move the index servo\n"
    "#i01_rightHand_index.moveTo(20)\n"
    "\n"
    ]
    customWriter.writelines(L)
    customWriter.close()


def CheckFileExist(File):
  if not os.path.isfile(File):
    saveCustom(customFilename)
    i01.info("custom file created : data/InMoov2/InMoovCustom.py")
  else:
    execfile('data/InMoov2/InMoovCustom.py')  

CheckFileExist(ThisFilePart)
