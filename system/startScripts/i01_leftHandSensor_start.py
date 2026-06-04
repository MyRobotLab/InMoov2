#########################################
# i01_leftSensors_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

import ConfigParser
import os
ThisServicePart = 'data/InMoov2/i01.leftHand.sensor.config'

def CheckFileExistLeft(filename):
    if not os.path.isfile(filename):
        execfile('resource/InMoov2/system/startScripts/i01_leftHandSensor_config.py')
        i01.info("config file created : %s" % filename)

CheckFileExistLeft(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart)

FINGERS = [
    "thumb",
    "index",
    "majeure",
    "ringFinger",
    "pinky"
]

pins = {}
psi = {}

for finger in FINGERS:
    pins[finger] = ThisServicePartConfig.getint(
        'MAIN',
        'left_%sPin' % finger
    )

    psi[finger] = {
        'min': ThisServicePartConfig.getint('MAIN', 'left_%s_Psi_min' % finger),
        'low': ThisServicePartConfig.getint('MAIN', 'left_%s_Psi_low' % finger),
        'mid': ThisServicePartConfig.getint('MAIN', 'left_%s_Psi_mid' % finger),
        'max': ThisServicePartConfig.getint('MAIN', 'left_%s_Psi_max' % finger)
    }

pressure = {}

for finger in FINGERS:
    pressure[finger] = 0

finger_servos = {
    "thumb": i01_leftHand_thumb,
    "index": i01_leftHand_index,
    "majeure": i01_leftHand_majeure,
    "ringFinger": i01_leftHand_ringFinger,
    "pinky": i01_leftHand_pinky
}

pin_map = {
    "A0": "thumb",
    "A1": "index",
    "A2": "majeure",
    "A3": "ringFinger",
    "A4": "pinky"
}

def stopFinger(finger, level):
    finger_servos[finger].stop()
    finger_servos[finger].disable()
    print "---Stopping %s %sSensorPin" % (level, finger)

if runtime.isStarted('i01.left'):
    leftHandSensorStarted = True

    try:
        def publishPinLeft(pinsLeft):

            for p in pinsLeft:

                finger = pin_map.get(p.pin)

                if finger is None:
                    continue

                value = p.value
                cfg = psi[finger]

                if value >= cfg['max']:
                    if pressure[finger] <= 3:
                        stopFinger(finger, 3)
                        pressure[finger] = 0

                elif value >= cfg['mid']:
                    if pressure[finger] <= 2:
                        stopFinger(finger, 2)
                        pressure[finger] = 0

                elif value >= cfg['low']:
                    if pressure[finger] == 1:
                        stopFinger(finger, 1)
                        pressure[finger] = 0

                print "Value: %s Pin: %s Finger: %s" % (value, pins[finger], finger)

        if runtime.isStarted('i01.chatBot'):
            i01_chatBot.getResponse("SYSTEM_EVENT STARTED LEFT HAND SENSOR")
        i01_left.addListener("publishPinArray","python","publishPinLeft")        

        def leftHandSensorON():
            if leftHandSensorStarted==1:
                print "=========LeftSensorON========"

                for pin in pins.values():
                    i01_left.enablePin(pin, 1)#2 is the number of polls per seconds

        def leftHandSensorOFF():
            if leftHandSensorStarted==1:

                for pin in pins.values():
                    i01_left.disablePin(pin)

                print "=========LeftSensorOFF======="

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
