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
    "# This python script is located in the directory data/InMoov2/\n"
    "# Those commands are safe, you can copy them to your other MRL versions\n"
    "# ##############################################################################\n"
    "\n"
    "\n"
    "## These samples would be executed when starting i01:\n"
    "\n"
    "## Play a neoPixel animation while the robot speaking\n"
    "#i01_neoPixel.playAnimation('Flash Random', 255, 255, 255, 1)\n"
    "## Talk something\n"
    "#i01_mouth.speakBlocking('he is a replicant, or not?')\n"
    "## Stop neoPixel\n"
    "#i01_neoPixel.stopAnimation()\n"
    "## Move the index servo\n"
    "#i01_rightHand_index.moveTo(20)\n"
    "\n"
    "## Another example, this could be executed via aiml:\n"
    "def myScripts():\n"
    "  #execfile('data/InMoov2/myScript1.py')\n"
    "  execfile('myScript2.py')\n"
    "\n"
    "## Another example, that could be executed via aiml:\n"
    "def myScript2():\n"
    "  print('I feel good')\n"
    "\n"
    ]
    customWriter.writelines(L)
    customWriter.close()


def CheckFileExist(File):
  if not os.path.isfile(File):
    saveCustom(customFilename)
    runtime.info("custom file created : data/InMoov2/InMoovCustom.py")
    python.execFile('data/InMoov2/InMoovCustom.py')
    #execfile('data/InMoov2/InMoovCustom.py')
  else:
    python.execFile('data/InMoov2/InMoovCustom.py')
    #execfile('data/InMoov2/InMoovCustom.py')


def CheckDirectoryExist():
  if not os.path.exists("data/InMoov2"):
    os.makedirs("data/InMoov2")

CheckDirectoryExist()
CheckFileExist(ThisFilePart) 
