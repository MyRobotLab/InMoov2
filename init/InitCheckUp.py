# ##############################################################################
#                 INITIAL CHECKUP2
# ##############################################################################

################################
# INIT.1 - system dependencies
################################
DEBUG = 0
# libraries import
execfile("resource/InMoov2/system/Import_Libraries.py")
# common functions
execfile("resource/InMoov2/system/Import_Functions.py")

# RuningFolder=os.getcwd().replace("\\", "/")+"/"+RuningFolder+"/"
# global vars import
execfile("resource/InMoov2/system/Robot_Satus_GlobalsVars.py")

# we load our custom script
execfile("resource/InMoov2/custom/InMoovCustom_start.py")

# we load alan's face for facerecognition
execfile("resource/InMoov2/system/startScripts/InMoovTrain_start.py")

# we get InMoov2 service
i01 = Runtime.getService("i01")

# mute for starting action vocals
# if IsMute==1:i01.setMute(True)

################################
# INIT.2 - services call
################################
# we load services python side from services folder
execfile("resource/InMoov2/services/1_AudioFile.py")
execfile("resource/InMoov2/services/3_ImageDisplay.py")
execfile("resource/InMoov2/services/4_Ear.py")
execfile("resource/InMoov2/services/5_Mouth.py")
# 8_NervoBoardRelay.py  ##NEED FIXING FOR NIXIE
execfile("resource/InMoov2/services/9_neoPixel.py")
execfile("resource/InMoov2/services/A_Chatbot.py")
execfile("resource/InMoov2/services/C_Pir.py")
execfile("resource/InMoov2/services/D_OpenCv.py")
execfile("resource/InMoov2/services/E_OpenNi.py")
# E_Oak.py ## WOULD REPLACE KINECT
# G_Translator.py ## NEED FIXING FOR NIXIE
execfile("resource/InMoov2/services/H_OpenWeatherMap.py")
# J_SensorFinger.py ## NEED FIXING FOR NIXIE
execfile('resource/InMoov2/services/K_FiniteStateMachine.py')
execfile("resource/InMoov2/services/L_Llm.py")

################################
# INIT.3- inmoov loading
################################

# we launch Inmoov life
execfile("resource/InMoov2/life/HealthCheck.py")
execfile("resource/InMoov2/life/shutdown.py")
execfile("resource/InMoov2/life/shutdownComplete.py")
execfile("resource/InMoov2/life/sleepMode.py")

################################
# INIT.4 - great, inmoov is alive
################################

if runtime.isStarted("i01.neoPixel"):
    if i01.getConfig().neoPixelDownloadBlue==1:
        i01_neoPixel.setAnimation("Color Wipe", 10, 204, 243, 50)
        sleep(4)
        i01_neoPixel.clear()
sleep(1)
welcomeMessage()
print("initCheckUp.py loaded")
