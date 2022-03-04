import os
configFilename='skeleton_rightHand.config'
configPath='data/InMoov2/config/'
def saveConfig(configFilename):
    configFile = configFilename
    configWriter = 0
    configWriter = open(configPath+configFile, "w+")
    L =[
    ";---------------- RIGHT HAND CONFIGURATION -------------------\n"
    "[MAIN]\n"
    
    "##############################################################\n"
    "#                     InMoov2 rightHand                      #\n"
    "#               auto generated configuration                 #\n"
    "##############################################################\n"
    "\n"
    "\n"
    "isRightHandActivated=True\n"
    "\n"
    "\n"
    "[SERVO_MINIMUM_MAP_OUTPUT]\n"
    ";your servo minimal limits\n"
    "\n"
    "\n"
    ]
    configWriter.writelines(L)
    #configWriter.write("EXAMPLE\n")
    configWriter.write("[SERVO_PIN]\n")
    for InMoov2Hand in Runtime.getServices():
        if isinstance(InMoov2Hand, Servo):
            s = Servo #+os.getcwd().replace('i01.rightHand.','')
            #configWriter.write("# Servo Name : " + s.getName(InMoov2Hand) + "\n")
            #configWriter.write("[SERVO_PIN]\n")
            #configWriter.write("# " + s.getName(InMoov2Hand) + " pin = " + s.getPin(InMoov2Hand) + "\n")
            configWriter.write(s.getName(InMoov2Hand) + " = " + s.getPin(InMoov2Hand) + "\n")
            #configWriter.write(s.getControllerName(InMoov2Hand) + "\n")
            #configWriter.write("rest = " + s.getRest(InMoov2Hand) + "\n")
            #for root, subdirs, files in os.walk(configPath+configFile):
                #os.path.basename([0][1]).replace('i01.rightHand.','')
    configWriter.write("[CONTROLLER]\n")
    for i01_right in Runtime.getServices():
        if isinstance(i01_right, Arduino):
            a = Arduino
            configWriter.write(a.getName(i01_right) + " = " + a.getPortName(i01_right) + "\n")           
    configWriter.write("finitum\n")
    configWriter.close()

saveConfig(configFilename)
