# -- coding: utf-8 --
# ##############################################################################
#                 MOUTH SERVICE FILE
# ##############################################################################

def initMouth():
  i01_mouth.getConfig()
  # python.subscribe(i01_mouth.getName(),"publishStartSpeaking")
  # python.subscribe(i01_mouth.getName(),"publishEndSpeaking")

# ##############################################################################
# MRL SERVICE TWEAKS
# ##############################################################################

#analog pin listener use 
# def publishMouthcontrolPinLeft(pins):
#   global AudioInputValues
#   global AudioInputRawValue

#   for pin in range(0, len(pins)):
#     #mouth control listener
#     if runtime.isStarted('i01.head'):
#       if AudioSignalProcessingCalibration:AudioInputValues.append(pins[pin].value)
        
#       if AudioSignalProcessing:
#         if pins[pin].value>minAudioValue:
#           i01_head_jaw.setSpeed(random.uniform(200,500))
#           if not i01_head_jaw.isMoving():i01_head_jaw.moveTo(int(pins[pin].value))
 
#stop autolisten
def onEndSpeaking(text):

  if flash_when_speak==1 and runtime.isStarted('i01.neoPixel'):i01_neoPixel.clear()

  # if AudioSignalProcessing:
  #   try:
  #     left.disablePin(AnalogPinFromSoundCard)
  #     i01_head_jaw.setSpeed(500)
  #     i01_head_jaw.moveTo(0)
  #   except:
  #     print "onEndSpeaking error"
  #     pass
  
def onStartSpeaking(text):

  #if RobotIsErrorMode==0:
  if runtime.isStarted('i01.neoPixel') and flash_when_speak==1:i01_neoPixel.setAnimation("Ironman", 255, 255, 255, 20)
  if 'oui ' in text or 'yes ' in text or ' oui' in text or 'ja ' in text or text=="yes" or text=="kyllä":Yes()
  if 'non ' in text or 'no ' in text or 'nicht ' in text or 'neen ' in text or text=="no" or text=="ei":No()
  
  # if AudioSignalProcessing:
  #   try:left.enablePin(AnalogPinFromSoundCard,HowManyPollsBySecond)      
  #   except:
  #     print "onStartSpeaking error"
  #     pass

  #if runtime.isStarted('i01.random'):
    #if not i01_head_rothead.isMoving():
        #i01_head_rothead.moveTo(random.uniform(65,115))

    #force random move while speaking, to avoid conflict with random life gesture
    # if RobotCanMoveHeadWhileSpeaking==1:
    #   if random.randint(0,1)==1:
    #     RobotCanMoveHeadRandom=True #FIXME in java
    #     MoveHeadTimer.startClock()
    #   if random.randint(0,1)==1:
    #     RobotCanMoveEyesRandom=True #FIXME in java
    #     MoveEyesTimer.startClock()

