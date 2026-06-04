#########################################
# i01_rightSensors_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

import ConfigParser
import os
ThisServicePart = 'data/InMoov2/i01.rightHand.sensor.config'

def CheckFileExistRight(filename):
    if not os.path.isfile(filename):
        execfile('resource/InMoov2/system/startScripts/i01_rightHandSensor_config.py')
        i01.info("config file created : %s" % filename)

CheckFileExistRight(ThisServicePart)
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
        'right_%sPin' % finger
    )

    psi[finger] = {
        'min': ThisServicePartConfig.getint('MAIN', 'right_%s_Psi_min' % finger),
        'low': ThisServicePartConfig.getint('MAIN', 'right_%s_Psi_low' % finger),
        'mid': ThisServicePartConfig.getint('MAIN', 'right_%s_Psi_mid' % finger),
        'max': ThisServicePartConfig.getint('MAIN', 'right_%s_Psi_max' % finger)
    }

pressure = {}

for finger in FINGERS:
    pressure[finger] = 0

finger_servos = {
    "thumb": i01_rightHand_thumb,
    "index": i01_rightHand_index,
    "majeure": i01_rightHand_majeure,
    "ringFinger": i01_rightHand_ringFinger,
    "pinky": i01_rightHand_pinky
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

if runtime.isStarted('i01.right'):
    rightHandSensorStarted = True

    try:
        def publishPinRight(pinsRight):

            for p in pinsRight:

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
            i01_chatBot.getResponse("SYSTEM_EVENT STARTED RIGHT HAND SENSOR")
        i01_right.addListener("publishPinArray","python","publishPinRight")        

        def rightHandSensorON():
            if rightHandSensorStarted==1:
                print "=========RightSensorON========"

                for pin in pins.values():
                    i01_right.enablePin(pin, 1)#2 is the number of polls per seconds

        def rightHandSensorOFF():
            if rightHandSensorStarted==1:

                for pin in pins.values():
                    i01_right.disablePin(pin)

                print "=========RightSensorOFF======="

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
