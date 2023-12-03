# -- coding: utf-8 --
# ##############################################################################
#                 MOUTH SERVICE FILE
# ##############################################################################

def initMouth():
  i01_mouth.getConfig()
  python.subscribe(i01_mouth.getName(),"publishStartSpeaking")
  python.subscribe(i01_mouth.getName(),"publishEndSpeaking")

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
  if runtime.isStarted('i01'):
    if i01.getConfig().robotCanMoveHeadWhileSpeaking==1:
      if runtime.isStarted('i01.random'):
        i01_random.disable()
        i01_random.enable('i01.moveLeftArm')
        i01_random.enable('i01.moveRightArm')
        i01_random.enable('i01.moveLeftHand')
        i01_random.enable('i01.moveRightHand')
        i01_random.enable('i01.moveTorso')
        i01_random.enable('i01.setLeftArmSpeed')
        i01_random.enable('i01.setRightArmSpeed')
        i01_random.enable('i01.setLeftHandSpeed')
        i01_random.enable('i01.setRightHandSpeed')
        i01_random.enable('i01.setTorsoSpeed')
        if runtime.isStarted('i01.head'):
          i01_random.addRandom(200, 1000, "i01", "setHeadSpeed", 8.0, 20.0, 8.0, 20.0, 8.0, 20.0)
          i01_random.addRandom(200, 1000, "i01", "moveHead", 70.0, 110.0, 65.0, 115.0, 70.0, 110.0)

    if i01.getConfig().neoPixelFlashWhenSpeaking==1 and runtime.isStarted('i01.neoPixel'):i01_neoPixel.clear()
    # if AudioSignalProcessing:
    #   try:
    #     left.disablePin(AnalogPinFromSoundCard)
    #     i01_head_jaw.setSpeed(500)
    #     i01_head_jaw.moveTo(0)
    #   except:
    #     print "onEndSpeaking error"
    #     pass
  
def onStartSpeaking(text):
  if runtime.isStarted('i01'):
  #if RobotIsErrorMode==0:
  #  if runtime.isStarted('i01.neoPixel') and i01.getConfig().neoPixelFlashWhenSpeaking==1:i01_neoPixel.setAnimation("Ironman", 255, 255, 255, 20)
    if 'oui ' in text or 'yes ' in text or ' oui' in text or 'ja ' in text or text=="yes" or text=="kyllä":Yes()
    if 'non ' in text or 'no ' in text or 'nicht ' in text or 'neen ' in text or text=="no" or text=="ei":No()
    
    # if AudioSignalProcessing:
    #   try:left.enablePin(AnalogPinFromSoundCard,HowManyPollsBySecond)      
    #   except:
    #     print "onStartSpeaking error"
    #     pass

    #force random move while speaking, to avoid conflict with random life gesture
    if i01.getConfig().robotCanMoveHeadWhileSpeaking==1:
      i01_random = i01.startPeer('random')
      if runtime.isStarted('i01.random'):
        i01_random.disable('i01.moveLeftArm')
        i01_random.disable('i01.moveRightArm')
        i01_random.disable('i01.moveLeftHand')
        i01_random.disable('i01.moveRightHand')
        i01_random.disable('i01.moveTorso')
        i01_random.disable('i01.setLeftArmSpeed')
        i01_random.disable('i01.setRightArmSpeed')
        i01_random.disable('i01.setLeftHandSpeed')
        i01_random.disable('i01.setRightHandSpeed')
        i01_random.disable('i01.setTorsoSpeed')
        i01_random.enable()  
        if runtime.isStarted('i01.head'):
          if runtime.isStarted('i01.opencv'):
            if runtime.isStarted('i01.fsm'):
              if not i01_fsm.getCurrent()=="isTracking":
                  i01_random.addRandom(200, 1000, "i01", "setHeadSpeed", 8.0, 20.0, 8.0, 20.0, 8.0, 20.0)
                  i01_random.addRandom(100, 500, "i01", "moveHead", 70.0, 110.0, 65.0, 115.0, 70.0, 110.0)
                  i01_random.enable('i01.setHeadSpeed')
                  i01_random.enable('i01.moveHead')

          else:
              i01_random.addRandom(200, 1000, "i01", "setHeadSpeed", 8.0, 20.0, 8.0, 20.0, 8.0, 20.0)
              i01_random.addRandom(100, 500, "i01", "moveHead", 70.0, 110.0, 65.0, 115.0, 70.0, 110.0)
              i01_random.enable('i01.setHeadSpeed')
              i01_random.enable('i01.moveHead')
