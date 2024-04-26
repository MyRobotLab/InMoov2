## Yolo filter / 2 samples : what do you see / WHERE IS THE *

# We classify objects per frame and get the maximum detected for 1 frame only
# So we can list & count at one time, every available classified object in the field of view, in given time
# Also get given element (last_item_found) position if set, from all others in the field off view, from left to right

# "classifications" is the dictionary for detected objects in given time
# after aquisition & position sort, we will read collection content to play with it

## warning : yolo publisher is now inside java land to avoid threading issues because of python sleep
def onClassification(data):
    global last_item_found
    last_item_found = None
    global classifications
    classifications = data
    for key, value in data.items():
        #print(key)
        last_item_found = key

def startYoloInventory(duration):
  i01.speak(i01_chatBot.getPredicate("startupSentence"))
  sleep(5)
  if runtime.isStarted('i01.neoPixel'):
    i01_neoPixel.setAnimation("Color Wipe", 25, 5, 10, 15)
  enableYoloFor(duration)
  # interpret results ...
  collectionString=""
  for key, value in classifications.items():
    #collectionString=collectionString+str(value)+" "+key+", "
    collectionString=collectionString+" "+key+", "
    print('object detected: ',collectionString)
  #check if we have results, return key "none" if no ( aiml will understand the key 'none' )
  if len(collectionString) == 0:collectionString="none"
  # return results
  i01_chatBot.setPredicate("yoloTotalDetected",str(len(classifications)))
  return collectionString

def getYoloPosition(last_item_found):
  position = classifications.getPosition(last_item_found)
  # to not launch gesture, comment showObject :
  print ("Position of : ", last_item_found, position)
  showObject(position)
  return position

global lastPhotoFileName
#shared function to start & stop yolo filter
def enableYoloFor(duration):
  global lastPhotoFileName
  #start i01.opencv
  if runtime.isStarted('i01.opencv'):
    i01_opencv.addFilter("yolo")
    i01_opencv.setDisplayFilter("yolo")
    i01_opencv.setCameraIndex(0)
    i01_opencv.capture()
    classifications = {}
    # create a subscription to classification publication
    python.subscribe('i01.opencv', 'publishClassification')
    # wait for X
    sleep(duration)
    lastPhotoFileName = i01_opencv.recordFrame()
    #print lastPhotoFileName
    #if runtime.isStarted('i01.imageDisplay'):
      #i01_imageDisplay.display(lastPhotoFileName)
      #sleep(3)
      #i01_imageDisplay.closeAll()
    classifications.clear()
    python.unsubscribe('i01.opencv', 'publishClassification')
    i01_opencv.disableFilter("yolo")
    i01_opencv.removeFilter('yolo')
    i01_opencv.stopCapture()


def yolo():
   enableYoloFor(60)