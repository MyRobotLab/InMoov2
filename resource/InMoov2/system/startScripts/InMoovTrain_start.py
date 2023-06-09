#########################################
# InMoovTrain_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

import os
ThisFilePart = 'training/alan/0a2f5b5a-7dd9-4dad-b902-371d11f144f9.png'
path = "resource/InMoov2/system/pictures"
def saveCustom():
  for file in os.listdir(path):
    if file.endswith(".png"):
       src_dir = "resource/InMoov2/system/pictures/0a2f5b5a-7dd9-4dad-b902-371d11f144f9.png"
       trainingPath='training/alan/'
       shutil.copy(src_dir,trainingPath)


def CheckFileTrainExist(File):
  if not os.path.isfile(File):
    saveCustom()
    #runtime.info("training directory created")


def CheckDirectoryTrainExist():
  if not os.path.exists("training/alan"):
    os.makedirs("training/alan")

CheckDirectoryTrainExist()
CheckFileTrainExist(ThisFilePart) 
