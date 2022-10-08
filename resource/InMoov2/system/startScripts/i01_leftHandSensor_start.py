#########################################
# i01_leftSensors_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

import ConfigParser
import os
ThisServicePart = 'data/config/i01.leftHand.sensor.yml'

def CheckFileExistLeft(File):
  if not os.path.isfile(File):
    execfile('resource/InMoov2/system/startScripts/i01_leftHandSensor_config.py')
    i01.info("config file created : data/config/i01.leftHand.sensor.yml")

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
    leftHandSensorActivated = True

    try:
        # common left pin listener function
        def publishLeftSensor(pinsLeft):
            print ""
                    
            global leftThumbPressure
            global leftIndexPressure
            global leftMajeurePressure
            global leftRingFingerPressure
            global leftPinkyPressure
          

              
            for pin in range(0, len(pinsLeft)):
                if pinsLeft[pin].pin==(left_thumbPin):
                    if pinsLeft[pin].value<=(left_thumb_Psi_min) and pinsLeft[pin].value<(left_thumb_Psi_low):leftThumbPressure = 0 
                    if pinsLeft[pin].value>=(left_thumb_Psi_low)and pinsLeft[pin].value<(left_thumb_Psi_mid):
                        if leftThumbPressure == 1:
                            i01_leftHand_thumb.stop()
                            i01_leftHand_thumb.disable()
                    if pinsLeft[pin].value>=(left_thumb_Psi_mid)and pinsLeft[pin].value<(left_thumb_Psi_max):
                        if leftThumbPressure <= 2:
                            i01_leftHand_thumb.stop()
                            i01_leftHand_thumb.disable()
                    if pinsLeft[pin].value>=(left_thumb_Psi_max):
                        if leftThumbPressure <= 3:
                            i01_leftHand_thumb.stop()
                            i01_leftHand_thumb.disable()
                    print "leftThumbSensorPin:",left_thumbPin,"Value:",pinsLeft[pin].value

                if pinsLeft[pin].pin==(left_indexPin):
                    if pinsLeft[pin].value<=(left_index_Psi_min) and pinsLeft[pin].value<(left_index_Psi_low):leftIndexPressure = 0
                    if pinsLeft[pin].value>=(left_index_Psi_low)and pinsLeft[pin].value<(left_index_Psi_mid):
                        if leftIndexPressure == 1:
                            i01_leftHand_index.stop()
                            i01_leftHand_index.disable()
                    if pinsLeft[pin].value>=(left_index_Psi_mid)and pinsLeft[pin].value<(left_index_Psi_max):
                        if leftIndexPressure <= 2:
                            i01_leftHand_index.stop()
                            i01_leftHand_index.disable()
                    if pinsLeft[pin].value>=(left_index_Psi_max):
                        if leftIndexPressure <= 3:
                            i01_leftHand_index.stop()
                            i01_leftHand_index.disable()
                    print "leftIndexSensorPin:",left_indexPin,"Value:",pinsLeft[pin].value

                if pinsLeft[pin].pin==(left_majeurePin):
                    if pinsLeft[pin].value<=(left_majeure_Psi_min) and pinsLeft[pin].value<(left_majeure_Psi_low):leftMajeurePressure = 0
                    if pinsLeft[pin].value>=(left_majeure_Psi_low)and pinsLeft[pin].value<(left_majeure_Psi_mid):
                        if leftMajeurePressure == 1:
                            i01_leftHand_majeure.stop()
                            i01_leftHand_majeure.disable()                  
                    if pinsLeft[pin].value>=(left_majeure_Psi_mid)and pinsLeft[pin].value<(left_majeure_Psi_max):
                        if leftMajeurePressure <= 2:
                            i01_leftHand_majeure.stop()
                            i01_leftHand_majeure.disable()
                    if pinsLeft[pin].value>=(left_majeure_Psi_max):
                        if leftMajeurePressure <= 3:
                            i01_leftHand_majeure.stop()
                            i01_leftHand_majeure.disable()
                    print "leftMajeureSensorPin:",left_majeurePin,"Value:",pinsLeft[pin].value

                if pinsLeft[pin].pin==(left_ringFingerPin):
                    if pinsLeft[pin].value<=(left_ringFinger_Psi_min) and pinsLeft[pin].value<(left_ringFinger_Psi_low):leftRingFingerPressure = 0
                    if pinsLeft[pin].value>=(left_ringFinger_Psi_low)and pinsLeft[pin].value<(left_ringFinger_Psi_mid):
                        if leftRingFingerPressure == 1:
                            i01_leftHand_ringFinger.stop()
                            i01_leftHand_ringFinger.disable()
                    if pinsLeft[pin].value>=(left_ringFinger_Psi_mid)and pinsLeft[pin].value<(left_ringFinger_Psi_max):
                        if leftRingFingerPressure <= 2:
                            i01_leftHand_ringFinger.stop()
                            i01_leftHand_ringFinger.disable()
                    if pinsLeft[pin].value>=(left_ringFinger_Psi_max):
                        if leftRingFingerPressure <= 3:
                            i01_leftHand_ringFinger.stop()
                            i01_leftHand_ringFinger.disable()
                    print "leftRingFingerSensorPin:",left_ringFingerPin,"Value:",pinsLeft[pin].value

                if pinsLeft[pin].pin==(left_pinkyPin):
                    if pinsLeft[pin].value<=(left_pinky_Psi_min) and pinsLeft[pin].value<(left_pinky_Psi_low):leftPinkyPressure = 0
                    if pinsLeft[pin].value>=(left_pinky_Psi_low)and pinsLeft[pin].value<(left_pinky_Psi_mid):
                        if leftPinkyPressure == 1:
                            i01_leftHand_pinky.stop()
                            i01_leftHand_pinky.disable()
                    if pinsLeft[pin].value>=(left_pinky_Psi_mid)and pinsLeft[pin].value<(left_pinky_Psi_max):
                        if leftPinkyPressure <= 2:
                            i01_leftHand_pinky.stop()
                            i01_leftHand_pinky.disable()
                    if pinsLeft[pin].value>=(left_pinky_Psi_max):
                        if leftPinkyPressure <= 3:
                            i01_leftHand_pinky.stop()
                            i01_leftHand_pinky.disable()
                    print "leftPinkySensorPin:",left_pinkyPin,"Value:",pinsLeft[pin].value
                    print "-----------Left-Finger-Sensors-----------"


        i01.speakBlocking(i01.localize("STARTINGLEFTHANDSENSOR"))
        i01_left.addListener("publishPinArray","python","publishLeftSensor")

        def leftHandSensorON():
            if leftHandSensorActivated==1:
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
            if leftHandSensorActivated==1:
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
        i01.speakBlocking(i01.localize('CONFIGPARSERPROBLEM'))
        leftHandSensorActivated = False
        pass
else:
    i01.error('i01.left controller not found for left hand sensor')
    i01.speakBlocking(i01.localize('BADRDUINOCHOOSEN','left Hand Sensor'))
    leftHandSensorActivated = False