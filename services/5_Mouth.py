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

def onEndSpeaking(text):
  if runtime.isStarted('i01'):
    if i01.getConfig().robotCanMoveHeadWhileSpeaking==1:
      if runtime.isStarted('i01.random'):
        if runtime.isStarted('i01.head'):
          i01_random.addRandom(200, 1000, "i01", "setHeadSpeed", 8.0, 20.0, 8.0, 20.0, 8.0, 20.0)
          i01_random.addRandom(200, 1000, "i01", "moveHead", 70.0, 110.0, 65.0, 115.0, 70.0, 110.0)
          i01_random.disable('i01.setHeadSpeed')
          i01_random.disable('i01.moveHead')
          i01_random.disable('randomBlink')
          i01_random.disable('randomFace')
    if i01.getConfig().robotCanMoveHeadWhileSpeaking==0:
      if runtime.isStarted('i01.random'):
        if runtime.isStarted('i01.head'):
          i01_random.disable('i01.setHeadSpeed')
          i01_random.disable('i01.moveHead')
          i01_random.disable('randomBlink')
          i01_random.disable('randomFace')
    if i01.getConfig().neoPixelFlashWhenSpeaking==1 and runtime.isStarted('i01.neoPixel'):i01_neoPixel.clear()
  
def onStartSpeaking(text):
  if runtime.isStarted('i01'):
  #if RobotIsErrorMode==0:
    if runtime.isStarted('i01.neoPixel') and i01.getConfig().neoPixelFlashWhenSpeaking==1:i01_neoPixel.setAnimation("Ironman", 255, 255, 255, 20)
    if 'oui ' in text or 'yes ' in text or ' oui' in text or 'ja ' in text or text=="yes" or text=="kyllä":Yes()
    if 'non ' in text or 'no ' in text or 'nicht ' in text or 'neen ' in text or text=="no" or text=="ei":No()

    #force random move while speaking, to avoid conflict with random life gesture
    if i01.getConfig().robotCanMoveHeadWhileSpeaking==1:
      if not runtime.isStarted('i01.random'):
        i01_random = i01.startPeer('random')
        if runtime.isStarted('i01.leftArm'):
          i01_random.disable('i01.setLeftArmSpeed')
          i01_random.disable('i01.moveLeftArm')
        if runtime.isStarted('i01.rightArm'):
          i01_random.disable('i01.setRightArmSpeed')
          i01_random.disable('i01.moveRightArm')
        if runtime.isStarted('i01.leftHand'):
          i01_random.disable('i01.setLeftHandSpeed')
          i01_random.disable('i01.moveLeftHand')
        if runtime.isStarted('i01.rightHand'):
          i01_random.disable('i01.setRightHandSpeed')
          i01_random.disable('i01.moveRightHand')
        if runtime.isStarted('i01.torso'):
          i01_random.disable('i01.setTorsoSpeed')
          i01_random.disable('i01.moveTorso')
        i01_random.enable()
        if runtime.isStarted('i01.head'):
          if runtime.isStarted('i01.opencv'):
            if runtime.isStarted('i01.fsm'):
              if not i01_fsm.getState()=="isTracking":
                  i01_random.addRandom(200, 1000, "i01", "setHeadSpeed", 8.0, 20.0, 8.0, 20.0, 8.0, 20.0)
                  i01_random.addRandom(100, 500, "i01", "moveHead", 70.0, 110.0, 65.0, 115.0, 70.0, 110.0)
                  i01_random.enable('i01.setHeadSpeed')
                  i01_random.enable('i01.moveHead')
                  i01_random.addRandom("randomBlink", 5000, 30000, "python", "exec", "blink()")
                  i01_random.enable('randomBlink')
                  i01_random.addRandom("randomFace", 1000, 2000, "python", "exec", "blink()", "upperLipU()", "upperLipD()", "cheeksU()", "cheeksD()", "forheadsU()", "forheadsD()")
                  i01_random.enable('randomFace')

          else:
              i01_random.addRandom("randomBlink", 5000, 30000, "python", "exec", "blink()")
              i01_random.enable('randomBlink')
              i01_random.addRandom("randomFace", 1000, 2000, "python", "exec", "blink()", "upperLipU()", "upperLipD()", "cheeksU()", "cheeksD()", "forheadsU()", "forheadsD()")
              i01_random.enable('randomFace')
      else:
        i01_random = i01.startPeer('random')
        if runtime.isStarted('i01.random'):
          i01_random.enable()
          if runtime.isStarted('i01.head'):
            if runtime.isStarted('i01.opencv'):
              if runtime.isStarted('i01.fsm'):
                if not i01_fsm.getState()=="isTracking":
                    i01_random.addRandom(200, 1000, "i01", "setHeadSpeed", 8.0, 20.0, 8.0, 20.0, 8.0, 20.0)
                    i01_random.addRandom(100, 500, "i01", "moveHead", 70.0, 110.0, 65.0, 115.0, 70.0, 110.0)
                    i01_random.enable('i01.setHeadSpeed')
                    i01_random.enable('i01.moveHead')
                    i01_random.addRandom("randomBlink", 5000, 30000, "python", "exec", "blink()")
                    i01_random.enable('randomBlink')
                    i01_random.addRandom("randomFace", 1000, 2000, "python", "exec", "blink()", "upperLipU()", "upperLipD()", "cheeksU()", "cheeksD()", "forheadsU()", "forheadsD()")
                    i01_random.enable('randomFace')

            else:
                i01_random.addRandom("randomBlink", 5000, 30000, "python", "exec", "blink()")
                i01_random.enable('randomBlink')
                i01_random.addRandom("randomFace", 1000, 2000, "python", "exec", "blink()", "upperLipU()", "upperLipD()", "cheeksU()", "cheeksD()", "forheadsU()", "forheadsD()")

def onFilterText(text):
  # filter all you want here
  # then publish to htmlfilter -> mouth
  # Splitting the text and filtering
  words = text.split()
  filtered_words = []
  extracted_word = ""
  
  for word in words:
      if word.startswith('*') and word.endswith('*'):
          # Save the extracted word without asterisks
          extracted_word = word.strip('*')
      else:
          filtered_words.append(word)
  
  # Joining the filtered words to form the filtered text
  filtered_text = ' '.join(filtered_words)
  #print(filtered_text)
  if runtime.isStarted('i01.mouth'):
      i01_mouth.speak(filtered_text) 
  #print(extracted_word)
  
  # Dynamically calling the function based on the extracted_word
  function_to_call = globals().get(extracted_word)
  if callable(function_to_call):
      result = function_to_call()
      result   
  else:
      result = "No function found matching the extracted word."
      result

if runtime.isStarted('i01.mouth'):
  initMouth()
