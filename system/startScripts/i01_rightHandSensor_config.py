#########################################
# i01_rightHand_sensor_config.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

import os
configFilename="i01.rightHand.sensor.config"
def saveConfig(configFilename):
    configPath='data/InMoov2/'
    configFile = configFilename
    configWriter = 0
    configWriter = open(configPath+configFile, "w+")
    L =[
    "; !!org.myrobotlab.service.config.SensorConfig\n"
    "\n"
    "; right_thumb_Psi_min: 544  # Put here the minimum value when the sensor is NOT pressed\n"
    "; right_thumb_Psi_low: 545  # In average cases take the minimum value and add +1 if using a AH3503 Hall Sensor\n"
    "; right_thumb_Psi_mid: 547  # In average cases take the minimum value and add +4\n"
    "; right_thumb_Psi_max: 550  # In average cases take the minimum value and add +7\n"
    "\n"
    "; analog pin range are 14-18 on uno, 54-70 on mega, A0,A1,A2...\n"
    "\n"
    "[MAIN]\n"
    "\n"
    "right_thumb_Psi_min: 544\n"
    "right_thumb_Psi_low: 545\n"
    "right_thumb_Psi_mid: 547\n"
    "right_thumb_Psi_max: 550\n"
    "\n"
    "right_index_Psi_min: 544\n"
    "right_index_Psi_low: 545\n"
    "right_index_Psi_mid: 547\n"
    "right_index_Psi_max: 550\n"
    "\n"
    "right_majeure_Psi_min: 544\n"
    "right_majeure_Psi_low: 545\n"
    "right_majeure_Psi_mid: 547\n"
    "right_majeure_Psi_max: 550\n"
    "\n"
    "right_ringFinger_Psi_min: 544\n"
    "right_ringFinger_Psi_low: 545\n"
    "right_ringFinger_Psi_mid: 547\n"
    "right_ringFinger_Psi_max: 550\n"
    "\n"
    "right_pinky_Psi_min: 544\n"
    "right_pinky_Psi_low: 545\n"
    "right_pinky_Psi_mid: 547\n"
    "right_pinky_Psi_max: 550\n"
    "\n"
    "right_thumbPin: 54\n"
    "right_indexPin: 55\n"
    "right_majeurePin: 56\n"
    "right_ringFingerPin: 57\n"
    "right_pinkyPin: 58\n"
    "\n"
    ]
    configWriter.writelines(L)
    configWriter.close()

saveConfig(configFilename)
