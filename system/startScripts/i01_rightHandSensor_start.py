#########################################
# i01_rightSensors_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

import ConfigParser
import os
ThisServicePart = 'data/InMoov2/i01.rightHand.sensor.config'

def CheckFileExistRight(File):
  if not os.path.isfile(File):
    execfile('resource/InMoov2/system/startScripts/i01_rightHandSensor_config.py')
    i01.info("config file created : data/InMoov2/i01.rightHand.sensor.config")

CheckFileExistRight(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart)

right_thumbPin=ThisServicePartConfig.getint('MAIN', 'right_thumbPin')
right_indexPin=ThisServicePartConfig.getint('MAIN', 'right_indexPin')
right_majeurePin=ThisServicePartConfig.getint('MAIN', 'right_majeurePin')
right_ringFingerPin=ThisServicePartConfig.getint('MAIN', 'right_ringFingerPin')
right_pinkyPin=ThisServicePartConfig.getint('MAIN', 'right_pinkyPin')

right_thumb_Psi_min=ThisServicePartConfig.getint('MAIN', 'right_thumb_Psi_min')
right_thumb_Psi_low=ThisServicePartConfig.getint('MAIN', 'right_thumb_Psi_low')
right_thumb_Psi_mid=ThisServicePartConfig.getint('MAIN', 'right_thumb_Psi_mid')
right_thumb_Psi_max=ThisServicePartConfig.getint('MAIN', 'right_thumb_Psi_max')

right_index_Psi_min=ThisServicePartConfig.getint('MAIN', 'right_index_Psi_min')
right_index_Psi_low=ThisServicePartConfig.getint('MAIN', 'right_index_Psi_low')
right_index_Psi_mid=ThisServicePartConfig.getint('MAIN', 'right_index_Psi_mid')
right_index_Psi_max=ThisServicePartConfig.getint('MAIN', 'right_index_Psi_max')

right_majeure_Psi_min=ThisServicePartConfig.getint('MAIN', 'right_majeure_Psi_min')
right_majeure_Psi_low=ThisServicePartConfig.getint('MAIN', 'right_majeure_Psi_low')
right_majeure_Psi_mid=ThisServicePartConfig.getint('MAIN', 'right_majeure_Psi_mid')
right_majeure_Psi_max=ThisServicePartConfig.getint('MAIN', 'right_majeure_Psi_max')

right_ringFinger_Psi_min=ThisServicePartConfig.getint('MAIN', 'right_ringFinger_Psi_min')
right_ringFinger_Psi_low=ThisServicePartConfig.getint('MAIN', 'right_ringFinger_Psi_low')
right_ringFinger_Psi_mid=ThisServicePartConfig.getint('MAIN', 'right_ringFinger_Psi_mid')
right_ringFinger_Psi_max=ThisServicePartConfig.getint('MAIN', 'right_ringFinger_Psi_max')

right_pinky_Psi_min=ThisServicePartConfig.getint('MAIN', 'right_pinky_Psi_min')
right_pinky_Psi_low=ThisServicePartConfig.getint('MAIN', 'right_pinky_Psi_low')
right_pinky_Psi_mid=ThisServicePartConfig.getint('MAIN', 'right_pinky_Psi_mid')
right_pinky_Psi_max=ThisServicePartConfig.getint('MAIN', 'right_pinky_Psi_max')

A0=right_thumbPin
A1=right_indexPin
A2=right_majeurePin
A3=right_ringFingerPin
A4=right_pinkyPin

# Used by finger sensors
# Right Hand
global rightThumbPressure
rightThumbPressure=0
global rightIndexPressure
rightIndexPressure=0
global rightMajeurePressure
rightMajeurePressure=0
global rightRingFingerPressure
rightRingFingerPressure=0
global rightPinkyPressure
rightPinkyPressure=0

if runtime.isStarted('i01.right'):
    rightHandSensorStarted = True
    # configFilename="data/InMoov2/i01.life.yml"
    # # open the file
    # file = open(configFilename, "r")
    # # read the file
    # text = file.read()
    # # search & replace the word
    # replaced_text = text.replace("rightHandSensorStarted=False", "rightHandSensorStarted=True")

    # # save the file
    # file = open(configFilename, "w")
    # file.write(replaced_text)
    # file.close()

    # execfile('resource/InMoov2/life/0_inmoovLife.py')

    try:
        # common right pin listener function
        def publishPinRight(pinsRight):
            #print(pinsRight)
                    
            global rightThumbPressure
            global rightIndexPressure
            global rightMajeurePressure
            global rightRingFingerPressure
            global rightPinkyPressure

            #print (rightIndexPressure)
          

              
            for pin in range(0, len(pinsRight)):
                if pinsRight[pin].pin==("A0"):
                    #if pinsRight[pin].value<=(right_thumb_Psi_min) and pinsRight[pin].value<(right_thumb_Psi_low):rightThumbPressure=0 
                    if pinsRight[pin].value>=(right_thumb_Psi_low) and pinsRight[pin].value<(right_thumb_Psi_mid):
                        if rightThumbPressure==1:
                            i01_rightHand_thumb.stop()
                            i01_rightHand_thumb.disable()
                            print "---Stopping 1 rightThumbSensorPin"
                            rightThumbPressure=0
                    if pinsRight[pin].value>=(right_thumb_Psi_mid):
                        if rightThumbPressure<=2:
                            i01_rightHand_thumb.stop()
                            i01_rightHand_thumb.disable()
                            print "---Stopping 2 rightThumbSensorPin"
                            rightThumbPressure=0
                    if pinsRight[pin].value>=(right_thumb_Psi_max):
                        if rightThumbPressure<=3:
                            i01_rightHand_thumb.stop()
                            i01_rightHand_thumb.disable()
                            print "---Stopping 3 rightThumbSensorPin"
                            rightThumbPressure=0
                    print pinsRight[pin].value,"Value:",right_thumbPin,"rightThumbSensorPin:"
                    #print "rightThumbSensorPin:",right_thumbPin,"Value:",pinsRight[pin].value

                if pinsRight[pin].pin==("A1"):
                    #if pinsRight[pin].value<(right_index_Psi_low):rightIndexPressure=0
                    if pinsRight[pin].value>=(right_index_Psi_low) and pinsRight[pin].value<(right_index_Psi_mid):    
                        if rightIndexPressure==1:
                            i01_rightHand_index.stop()
                            i01_rightHand_index.disable()
                            print "---Stopping 1 rightIndexSensorPin"
                            rightIndexPressure=0
                    if pinsRight[pin].value>=(right_index_Psi_mid):
                        if rightIndexPressure<=2:
                            i01_rightHand_index.stop()
                            i01_rightHand_index.disable()
                            print "---Stopping 2 rightIndexSensorPin"
                            rightIndexPressure=0
                    if pinsRight[pin].value>=(right_index_Psi_max):
                        if rightIndexPressure<=3:
                            i01_rightHand_index.stop()
                            i01_rightHand_index.disable()
                            print "---Stopping 3 rightIndexSensorPin"
                            rightIndexPressure=0
                    print pinsRight[pin].value,"Value:",right_indexPin,"rightIndexSensorPin:"

                if pinsRight[pin].pin==("A2"):
                    #if pinsRight[pin].value<=(right_majeure_Psi_min) and pinsRight[pin].value<(right_majeure_Psi_low):rightMajeurePressure=0
                    if pinsRight[pin].value>=(right_majeure_Psi_low) and pinsRight[pin].value<(right_majeure_Psi_mid):
                        if rightMajeurePressure==1:
                            i01_rightHand_majeure.stop()
                            i01_rightHand_majeure.disable()
                            print "---Stopping 1 rightMajeureSensorPin"
                            rightMajeurePressure=0
                    if pinsRight[pin].value>=(right_majeure_Psi_mid):
                        if rightMajeurePressure<=2:
                            i01_rightHand_majeure.stop()
                            i01_rightHand_majeure.disable()
                            print "---Stopping 2 rightMajeureSensorPin"
                            rightMajeurePressure=0
                    if pinsRight[pin].value>=(right_majeure_Psi_max):
                        if rightMajeurePressure<=3:
                            i01_rightHand_majeure.stop()
                            i01_rightHand_majeure.disable()
                            print "---Stopping 3 rightMajeureSensorPin"
                            rightMajeurePressure=0
                    print pinsRight[pin].value,"Value:",right_majeurePin,"rightMajeureSensorPin:"

                if pinsRight[pin].pin==("A3"):
                    #if pinsRight[pin].value<=(right_ringFinger_Psi_min) and pinsRight[pin].value<(right_ringFinger_Psi_low):rightRingFingerPressure=0
                    if pinsRight[pin].value>=(right_ringFinger_Psi_low) and pinsRight[pin].value==(right_ringFinger_Psi_mid):
                        if rightRingFingerPressure==1:
                            print(rightRingFingerPressure)
                            i01_rightHand_ringFinger.stop()
                            i01_rightHand_ringFinger.disable()
                            print "---Stopping 1 rightRingFingerSensorPin"
                            rightRingFingerPressure=0
                    if pinsRight[pin].value>=(right_ringFinger_Psi_mid):
                        if rightRingFingerPressure<=2:
                            print(rightRingFingerPressure)
                            i01_rightHand_ringFinger.stop()
                            i01_rightHand_ringFinger.disable()
                            print "---Stopping 2 rightRingFingerSensorPin"
                            rightRingFingerPressure=0
                    if pinsRight[pin].value>=(right_ringFinger_Psi_max):
                        if rightRingFingerPressure<=3:
                            print(rightRingFingerPressure)
                            i01_rightHand_ringFinger.stop()
                            i01_rightHand_ringFinger.disable()
                            print "---Stopping 3 rightRingFingerSensorPin"
                            rightRingFingerPressure=0
                    print pinsRight[pin].value,"Value:",right_ringFingerPin,"rightRingFingerSensorPin:"

                if pinsRight[pin].pin==("A4"):
                    #if pinsRight[pin].value<=(right_pinky_Psi_min) and pinsRight[pin].value<(right_pinky_Psi_low):rightPinkyPressure=0
                    if pinsRight[pin].value>=(right_pinky_Psi_low) and pinsRight[pin].value<(right_pinky_Psi_mid):
                        if rightPinkyPressure==1:
                            i01_rightHand_pinky.stop()
                            i01_rightHand_pinky.disable()
                            print "---Stopping 1 rightPinkySensorPin"
                            rightPinkyPressure=0
                    if pinsRight[pin].value>=(right_pinky_Psi_mid) and pinsRight[pin].value<(right_pinky_Psi_max):
                        if rightPinkyPressure<=2:
                            i01_rightHand_pinky.stop()
                            i01_rightHand_pinky.disable()
                            print "---Stopping 2 rightPinkySensorPin"
                            rightPinkyPressure=0
                    if pinsRight[pin].value>=(right_pinky_Psi_max):
                        if rightPinkyPressure<=3:
                            i01_rightHand_pinky.stop()
                            i01_rightHand_pinky.disable()
                            print "---Stopping 3 rightPinkySensorPin"
                            rightPinkyPressure=0
                    print pinsRight[pin].value,"Value:",right_pinkyPin,"rightPinkySensorPin:"
                    print "-----------Right-Finger-Sensors-----------"

        if runtime.isStarted('i01.chatBot'):
            i01_chatBot.getResponse("SYSTEM_EVENT STARTED RIGHT HAND SENSOR")
        i01_right.addListener("publishPinArray","python","publishPinRight")

        def rightHandSensorON():
            if rightHandSensorStarted==1:
                print "=========RightSensorON========" 
                i01_right.enablePin(right_thumbPin, 2) #2 is the number of polls per seconds
                i01_right.enablePin(right_indexPin, 2)
                i01_right.enablePin(right_majeurePin, 2)
                i01_right.enablePin(right_ringFingerPin, 2)
                i01_right.enablePin(right_pinkyPin, 2)
            else:
                pass

        def rightHandSensorOFF():
            #sleep(5)
            if rightHandSensorStarted==1:
                i01_right.disablePin(right_thumbPin)
                i01_right.disablePin(right_indexPin)
                i01_right.disablePin(right_majeurePin)
                i01_right.disablePin(right_ringFingerPin)
                i01_right.disablePin(right_pinkyPin)
                print "=========RightSensorOFF======="
            else:
                pass

    except:
        i01.error('could not start right hand sensor')
        if runtime.isStarted('i01.chatBot'):
            i01_chatBot.getResponse("ALERT")
            i01_chatBot.getResponse("SYSTEM_ERROR_RIGHTHANDSENSOR_1")
        rightHandSensorStarted = False
        pass
else:
    i01.error('i01.right controller not found for right hand sensor')
    if runtime.isStarted('i01.chatBot'):
            i01_chatBot.getResponse("ALERT")
            i01_chatBot.getResponse("SYSTEM_ERROR_RIGHTHANDSENSOR_2")
    rightHandSensorStarted = False
