#########################################
# i01_leftSensors_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

import ConfigParser
import os
ThisServicePart = 'data/InMoov2/i01.leftHand.sensor.config'

def CheckFileExistLeft(File):
  if not os.path.isfile(File):
    execfile('resource/InMoov2/system/startScripts/i01_leftHandSensor_config.py')
    i01.info("config file created : data/InMoov2/i01.leftHand.sensor.config")

CheckFileExistLeft(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart)

left_thumbPin=ThisServicePartConfig.getint('MAIN', 'left_thumbPin')
left_indexPin=ThisServicePartConfig.getint('MAIN', 'left_indexPin')
left_majeurePin=ThisServicePartConfig.getint('MAIN', 'left_majeurePin')
left_ringFingerPin=ThisServicePartConfig.getint('MAIN', 'left_ringFingerPin')
left_pinkyPin=ThisServicePartConfig.getint('MAIN', 'left_pinkyPin')

left_thumb_Psi_min=ThisServicePartConfig.getint('MAIN', 'left_thumb_Psi_min')
left_thumb_Psi_low=ThisServicePartConfig.getint('MAIN', 'left_thumb_Psi_low')
left_thumb_Psi_mid=ThisServicePartConfig.getint('MAIN', 'left_thumb_Psi_mid')
left_thumb_Psi_max=ThisServicePartConfig.getint('MAIN', 'left_thumb_Psi_max')

left_index_Psi_min=ThisServicePartConfig.getint('MAIN', 'left_index_Psi_min')
left_index_Psi_low=ThisServicePartConfig.getint('MAIN', 'left_index_Psi_low')
left_index_Psi_mid=ThisServicePartConfig.getint('MAIN', 'left_index_Psi_mid')
left_index_Psi_max=ThisServicePartConfig.getint('MAIN', 'left_index_Psi_max')

left_majeure_Psi_min=ThisServicePartConfig.getint('MAIN', 'left_majeure_Psi_min')
left_majeure_Psi_low=ThisServicePartConfig.getint('MAIN', 'left_majeure_Psi_low')
left_majeure_Psi_mid=ThisServicePartConfig.getint('MAIN', 'left_majeure_Psi_mid')
left_majeure_Psi_max=ThisServicePartConfig.getint('MAIN', 'left_majeure_Psi_max')

left_ringFinger_Psi_min=ThisServicePartConfig.getint('MAIN', 'left_ringFinger_Psi_min')
left_ringFinger_Psi_low=ThisServicePartConfig.getint('MAIN', 'left_ringFinger_Psi_low')
left_ringFinger_Psi_mid=ThisServicePartConfig.getint('MAIN', 'left_ringFinger_Psi_mid')
left_ringFinger_Psi_max=ThisServicePartConfig.getint('MAIN', 'left_ringFinger_Psi_max')

left_pinky_Psi_min=ThisServicePartConfig.getint('MAIN', 'left_pinky_Psi_min')
left_pinky_Psi_low=ThisServicePartConfig.getint('MAIN', 'left_pinky_Psi_low')
left_pinky_Psi_mid=ThisServicePartConfig.getint('MAIN', 'left_pinky_Psi_mid')
left_pinky_Psi_max=ThisServicePartConfig.getint('MAIN', 'left_pinky_Psi_max')

A0=left_thumbPin
A1=left_indexPin
A2=left_majeurePin
A3=left_ringFingerPin
A4=left_pinkyPin

# Used by finger sensors
# Left Hand
global leftThumbPressure
leftThumbPressure=0
global leftIndexPressure
leftIndexPressure=0
global leftMajeurePressure
leftMajeurePressure=0
global leftRingFingerPressure
leftRingFingerPressure=0
global leftPinkyPressure
leftPinkyPressure=0

if runtime.isStarted('i01.left'):
    leftHandSensorStarted = True
    # configFilename="data/InMoov2/i01.life.yml"
    # # open the file
    # file = open(configFilename, "r")
    # # read the file
    # text = file.read()
    # # search & replace the word
    # replaced_text = text.replace("leftHandSensorStarted=False", "leftHandSensorStarted=True")

    # # save the file
    # file = open(configFilename, "w")
    # file.write(replaced_text)
    # file.close()

    # execfile('resource/InMoov2/life/0_inmoovLife.py')

    try:
        # common left pin listener function
        def publishPinLeft(pinsLeft):
            #print(pinsLeft)
                    
            global leftThumbPressure
            global leftIndexPressure
            global leftMajeurePressure
            global leftRingFingerPressure
            global leftPinkyPressure
          

              
            for pin in range(0, len(pinsLeft)):
                if pinsLeft[pin].pin==("A0"):
                    #if pinsLeft[pin].value<=(left_thumb_Psi_min) and pinsLeft[pin].value<(left_thumb_Psi_low):leftThumbPressure=0 
                    if pinsLeft[pin].value>=(left_thumb_Psi_low)and pinsLeft[pin].value<(left_thumb_Psi_mid):
                        if leftThumbPressure==1:
                            i01_leftHand_thumb.stop()
                            i01_leftHand_thumb.disable()
                            print "---Stopping 1 leftThumbSensorPin"
                            leftThumbPressure=0
                    if pinsLeft[pin].value>=(left_thumb_Psi_mid):
                        if leftThumbPressure<=2:
                            i01_leftHand_thumb.stop()
                            i01_leftHand_thumb.disable()
                            print "---Stopping 2 leftThumbSensorPin"
                            leftThumbPressure=0
                    if pinsLeft[pin].value>=(left_thumb_Psi_max):
                        if leftThumbPressure<=3:
                            i01_leftHand_thumb.stop()
                            i01_leftHand_thumb.disable()
                            print "---Stopping 3 leftThumbSensorPin"
                            leftThumbPressure=0
                    print pinsLeft[pin].value,"Value:",left_thumbPin,"leftThumbSensorPin:"

                if pinsLeft[pin].pin==("A1"):
                    #if pinsLeft[pin].value<=(left_index_Psi_min) and pinsLeft[pin].value<(left_index_Psi_low):leftIndexPressure=0
                    if pinsLeft[pin].value>=(left_index_Psi_low)and pinsLeft[pin].value<(left_index_Psi_mid):
                        if leftIndexPressure==1:
                            i01_leftHand_index.stop()
                            i01_leftHand_index.disable()
                            print "---Stopping 1 leftIndexSensorPin"
                            leftIndexPressure=0
                    if pinsLeft[pin].value>=(left_index_Psi_mid):
                        if leftIndexPressure<=2:
                            i01_leftHand_index.stop()
                            i01_leftHand_index.disable()
                            print "---Stopping 2 leftIndexSensorPin"
                            leftIndexPressure=0
                    if pinsLeft[pin].value>=(left_index_Psi_max):
                        if leftIndexPressure<=3:
                            i01_leftHand_index.stop()
                            i01_leftHand_index.disable()
                            print "---Stopping 3 leftIndexSensorPin"
                            leftIndexPressure=0
                    print pinsLeft[pin].value,"Value:",left_indexPin,"leftIndexSensorPin:"

                if pinsLeft[pin].pin==("A2"):
                    #if pinsLeft[pin].value<=(left_majeure_Psi_min) and pinsLeft[pin].value<(left_majeure_Psi_low):leftMajeurePressure=0
                    if pinsLeft[pin].value>=(left_majeure_Psi_low)and pinsLeft[pin].value<(left_majeure_Psi_mid):
                        if leftMajeurePressure==1:
                            i01_leftHand_majeure.stop()
                            i01_leftHand_majeure.disable()
                            print "---Stopping 1 leftMajeureSensorPin"
                            leftMajeurePressure=0                  
                    if pinsLeft[pin].value>=(left_majeure_Psi_mid):
                        if leftMajeurePressure<=2:
                            i01_leftHand_majeure.stop()
                            i01_leftHand_majeure.disable()
                            print "---Stopping 2 leftMajeureSensorPin"
                            leftMajeurePressure=0 
                    if pinsLeft[pin].value>=(left_majeure_Psi_max):
                        if leftMajeurePressure<=3:
                            i01_leftHand_majeure.stop()
                            i01_leftHand_majeure.disable()
                            print "---Stopping 3 leftMajeureSensorPin"
                            leftMajeurePressure=0 
                    print pinsLeft[pin].value,"Value:",left_majeurePin,"leftMajeureSensorPin:"

                if pinsLeft[pin].pin==("A3"):
                    #if pinsLeft[pin].value<=(left_ringFinger_Psi_min) and pinsLeft[pin].value<(left_ringFinger_Psi_low):leftRingFingerPressure=0
                    if pinsLeft[pin].value>=(left_ringFinger_Psi_low)and pinsLeft[pin].value<(left_ringFinger_Psi_mid):
                        if leftRingFingerPressure==1:
                            i01_leftHand_ringFinger.stop()
                            i01_leftHand_ringFinger.disable()
                            print "---Stopping 1 leftRingFingerSensorPin"
                            leftRingFingerPressure=0 
                    if pinsLeft[pin].value>=(left_ringFinger_Psi_mid):
                        if leftRingFingerPressure<=2:
                            i01_leftHand_ringFinger.stop()
                            i01_leftHand_ringFinger.disable()
                            print "---Stopping 2 leftRingFingerSensorPin"
                            leftRingFingerPressure=0
                    if pinsLeft[pin].value>=(left_ringFinger_Psi_max):
                        if leftRingFingerPressure<=3:
                            i01_leftHand_ringFinger.stop()
                            i01_leftHand_ringFinger.disable()
                            print "---Stopping 3 leftRingFingerSensorPin"
                            leftRingFingerPressure=0
                    print pinsLeft[pin].value,"Value:",left_ringFingerPin,"leftRingFingerSensorPin:"

                if pinsLeft[pin].pin==("A4"):
                    #if pinsLeft[pin].value<=(left_pinky_Psi_min) and pinsLeft[pin].value<(left_pinky_Psi_low):leftPinkyPressure=0
                    if pinsLeft[pin].value>=(left_pinky_Psi_low)and pinsLeft[pin].value<(left_pinky_Psi_mid):
                        if leftPinkyPressure==1:
                            i01_leftHand_pinky.stop()
                            i01_leftHand_pinky.disable()
                            print "---Stopping 1 leftPinkySensorPin"
                            leftPinkyPressure=0
                    if pinsLeft[pin].value>=(left_pinky_Psi_mid):
                        if leftPinkyPressure<=2:
                            i01_leftHand_pinky.stop()
                            i01_leftHand_pinky.disable()
                            print "---Stopping 2 leftPinkySensorPin"
                            leftPinkyPressure=0
                    if pinsLeft[pin].value>=(left_pinky_Psi_max):
                        if leftPinkyPressure<=3:
                            i01_leftHand_pinky.stop()
                            i01_leftHand_pinky.disable()
                            print "---Stopping 3 leftPinkySensorPin"
                            leftPinkyPressure=0
                    print pinsLeft[pin].value,"Value:",left_pinkyPin,"leftPinkySensorPin:"
                    print "-----------Left-Finger-Sensors-----------"

        if runtime.isStarted('i01.chatBot'):
            i01_chatBot.getResponse("SYSTEM_EVENT STARTED LEFT HAND SENSOR")
        i01_left.addListener("publishPinArray","python","publishPinLeft")

        def leftHandSensorON():
            if leftHandSensorStarted==1:
                print "=========LeftSensorON========" 
                i01_left.enablePin(left_thumbPin, 2) #2 is the number of polls per seconds
                i01_left.enablePin(left_indexPin, 2)
                i01_left.enablePin(left_majeurePin, 2)
                i01_left.enablePin(left_ringFingerPin, 2)
                i01_left.enablePin(left_pinkyPin, 2)
            else:
                pass

        def leftHandSensorOFF():
            #sleep(5)
            if leftHandSensorStarted==1:
                i01_left.disablePin(left_thumbPin)
                i01_left.disablePin(left_indexPin)
                i01_left.disablePin(left_majeurePin)
                i01_left.disablePin(left_ringFingerPin)
                i01_left.disablePin(left_pinkyPin)
                print "=========LeftSensorOFF======="
            else:
                pass

    except:
        i01.error('could not start left hand sensor')
        if runtime.isStarted('i01.chatBot'):
            i01_chatBot.getResponse("ALERT")
            i01_chatBot.getResponse("SYSTEM_ERROR_LEFTHANDSENSOR_1")
        leftHandSensorStarted = False
        pass
else:
    i01.error('i01.left controller not found for left hand sensor')
    if runtime.isStarted('i01.chatBot'):
            i01_chatBot.getResponse("ALERT")
            i01_chatBot.getResponse("SYSTEM_ERROR_LEFTHANDSENSOR_2")
    leftHandSensorStarted = False