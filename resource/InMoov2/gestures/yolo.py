## Yolo filter / 2 samples : what do you see / WHERE IS THE *

# We classify objects per frame and get the maximum detected for 1 frame only
# So we can list & count at one time, every available classified object in the field of view, in given time
# Also get given element (label) position if set, from all others in the field off view, from left to right

# "i01_vision_collectionCount" is the dictionary for detected objects in given time
# after aquisition & position sort, we will read collection content to play with it

## warning : yolo publisher is now inside java land to avoid threading issues because of python sleep


def startYoloInventory(duration):
  i01.speak(i01_chatBot.getPredicate("startupSentence"))
  sleep(5)
  if runtime.isStarted('i01.neoPixel'):
    i01_neoPixel.setAnimation("Color Wipe", 25, 5, 10, 15)
  enableYoloFor(duration)
  # interpret results ...
  collectionString=""
  for key, value in i01_vision_collectionCount.iteritems():
    collectionString=collectionString+str(value)+" "+key+", "
  #check if we have results, return key "none" if no ( aiml will understand the key 'none' )
  if len(collectionString) == 0:collectionString="none"
  # return results
  i01_chatBot.setPredicate("yoloTotalDetected",str(len(i01_vision_collectionCount)))
  return collectionString

def getYoloPosition(label):
  position=i01_vision.getPosition(label)
  # to not launch gesture, comment showObject :
  print "Position of : ",label,position
  showObject(position)
  return position  

# TODO classify while head moves ! ( count )
# TODO what do you see in front of you ( few centimeters -> use gael mods )

global lastPhotoFileName
#shared function to start & stop yolo filter
def enableYoloFor(duration):
  global lastPhotoFileName
  i01_vision_collectionCount.clear()
  i01_vision_collectionPositions.clear()
  #start i01.opencv
  i01.cameraOn()
  # yolo filter in the pipeline ( add if no exist + enable + setActive )
  i01_vision.setActiveFilter("Yolo")
  try:
    gui.setActiveTab("i01_opencv")
    #os.remove(lastPhotoFileName)
    imageDisplay.closeAll()
  except:
    pass
  # wait for X
  sleep(duration)
  lastPhotoFileName = i01_opencv.recordFrame()
  #print lastPhotoFileName
  imageDisplay.display(lastPhotoFileName)
  i01_opencv.disableFilter("Yolo")
  print i01_vision_collectionCount
