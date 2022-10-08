#########################################
# i01_rightSensors_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

import ConfigParser
import os
ThisServicePart = 'data/config/i01.rightHand.sensor.yml'

def CheckFileExistRight(File):
  if not os.path.isfile(File):
    execfile('resource/InMoov2/system/startScripts/i01_rightHandSensor_config.py')
    i01.info("config file created : data/config/i01.rightHand.sensor.yml")

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
    rightHandSensorActivated = True

    try:
        # common right pin listener function
        def publishRightSensor(pinsRight):
            print ""
                    
            global rightThumbPressure
            global rightIndexPressure
            global rightMajeurePressure
            global rightRingFingerPressure
            global rightPinkyPressure
          

              
            for pin in range(0, len(pinsRight)):
                if pinsRight[pin].pin==(right_thumbPin):
                    if pinsRight[pin].value<=(right_thumb_Psi_min) and pinsRight[pin].value<(right_thumb_Psi_low):rightThumbPressure = 0 
                    if pinsRight[pin].value>=(right_thumb_Psi_low) and pinsRight[pin].value<(right_thumb_Psi_mid):
                        if rightThumbPressure == 1:
                            i01_rightHand_thumb.stop()
                            i01_rightHand_thumb.disable()
                    if pinsRight[pin].value>=(right_thumb_Psi_mid) and pinsRight[pin].value<(right_thumb_Psi_max):
                        if rightThumbPressure <= 2:
                            i01_rightHand_thumb.stop()
                            i01_rightHand_thumb.disable()
                    if pinsRight[pin].value>=(right_thumb_Psi_max):
                        if rightThumbPressure <= 3:
                            i01_rightHand_thumb.stop()
                            i01_rightHand_thumb.disable()
                    print "rightThumbSensorPin:",right_thumbPin,"Value:",pinsRight[pin].value

                if pinsRight[pin].pin==(right_indexPin):
                    if pinsRight[pin].value<=(right_index_Psi_min) and pinsRight[pin].value<(right_index_Psi_low):rightIndexPressure = 0
                    if pinsRight[pin].value>=(right_index_Psi_low) and pinsRight[pin].value<(right_index_Psi_mid):
                        if rightIndexPressure == 1:
                            i01_rightHand_index.stop()
                            i01_rightHand_index.disable()
                    if pinsRight[pin].value>=(right_index_Psi_mid) and pinsRight[pin].value<(right_index_Psi_max):
                        if rightIndexPressure <= 2:
                            i01_rightHand_index.stop()
                            i01_rightHand_index.disable()
                    if pinsRight[pin].value>=(right_index_Psi_max):
                        if rightIndexPressure <= 3:
                            i01_rightHand_index.stop()
                            i01_rightHand_index.disable()
                    print "rightIndexSensorPin:",right_indexPin,"Value:",pinsRight[pin].value

                if pinsRight[pin].pin==(right_majeurePin):
                    if pinsRight[pin].value<=(right_majeure_Psi_min) and pinsRight[pin].value<(right_majeure_Psi_low):rightMajeurePressure = 0
                    if pinsRight[pin].value>=(right_majeure_Psi_low) and pinsRight[pin].value<(right_majeure_Psi_mid):
                        if rightMajeurePressure == 1:
                            i01_rightHand_majeure.stop()
                            i01_rightHand_majeure.disable()                  
                    if pinsRight[pin].value>=(right_majeure_Psi_mid) and pinsRight[pin].value<(right_majeure_Psi_max):
                        if rightMajeurePressure <= 2:
                            i01_rightHand_majeure.stop()
                            i01_rightHand_majeure.disable()
                    if pinsRight[pin].value>=(right_majeure_Psi_max):
                        if rightMajeurePressure <= 3:
                            i01_rightHand_majeure.stop()
                            i01_rightHand_majeure.disable()
                    print "rightMajeureSensorPin:",right_majeurePin,"Value:",pinsRight[pin].value

                if pinsRight[pin].pin==(right_ringFingerPin):
                    if pinsRight[pin].value<=(right_ringFinger_Psi_min) and pinsRight[pin].value<(right_ringFinger_Psi_low):rightRingFingerPressure = 0
                    if pinsRight[pin].value>=(right_ringFinger_Psi_low) and pinsRight[pin].value<(right_ringFinger_Psi_mid):
                        if rightRingFingerPressure == 1:
                            i01_rightHand_ringFinger.stop()
                            i01_rightHand_ringFinger.disable()
                    if pinsRight[pin].value>=(right_ringFinger_Psi_mid) and pinsRight[pin].value<(right_ringFinger_Psi_max):
                        if rightRingFingerPressure <= 2:
                            i01_rightHand_ringFinger.stop()
                            i01_rightHand_ringFinger.disable()
                    if pinsRight[pin].value>=(right_ringFinger_Psi_max):
                        if rightRingFingerPressure <= 3:
                            i01_rightHand_ringFinger.stop()
                            i01_rightHand_ringFinger.disable()
                    print "rightRingFingerSensorPin:",right_ringFingerPin,"Value:",pinsRight[pin].value

                if pinsRight[pin].pin==(right_pinkyPin):
                    if pinsRight[pin].value<=(right_pinky_Psi_min) and pinsRight[pin].value<(right_pinky_Psi_low):rightPinkyPressure = 0
                    if pinsRight[pin].value>=(right_pinky_Psi_low) and pinsRight[pin].value<(right_pinky_Psi_mid):
                        if rightPinkyPressure == 1:
                            i01_rightHand_pinky.stop()
                            i01_rightHand_pinky.disable()
                    if pinsRight[pin].value>=(right_pinky_Psi_mid) and pinsRight[pin].value<(right_pinky_Psi_max):
                        if rightPinkyPressure <= 2:
                            i01_rightHand_pinky.stop()
                            i01_rightHand_pinky.disable()
                    if pinsRight[pin].value>=(right_pinky_Psi_max):
                        if rightPinkyPressure <= 3:
                            i01_rightHand_pinky.stop()
                            i01_rightHand_pinky.disable()
                    print "rightPinkySensorPin:",right_pinkyPin,"Value:",pinsRight[pin].value
                    print "-----------Right-Finger-Sensors-----------"


        i01.speakBlocking(i01.localize("STARTINGRIGHTHANDSENSOR"))
        i01_right.addListener("publishPinArray","python","publishRightSensor")

        def rightHandSensorON():
            if rightHandSensorActivated==1:
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
            if rightHandSensorActivated==1:
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
        i01.speakBlocking(i01.localize('CONFIGPARSERPROBLEM'))
        rightHandSensorActivated = False
        pass
else:
    i01.error('i01.right controller not found for right hand sensor')
    i01.speakBlocking(i01.localize('BADRDUINOCHOOSEN','right Hand Sensor'))
    rightHandSensorActivated = False
