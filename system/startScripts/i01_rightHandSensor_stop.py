# configFilename="data/InMoov2/i01.life.yml"
# # open the file
# file = open(configFilename, "r")
# # read the file
# text = file.read()
# # search & replace the word
# replaced_text = text.replace("rightHandSensorStarted=True", "rightHandSensorStarted=False")

# # save the file
# file = open(configFilename, "w")
# file.write(replaced_text)
# file.close()

# execfile('resource/InMoov2/life/0_inmoovLife.py')

if runtime.isStarted('i01.chatBot'):
  i01_chatBot.getResponse("SYSTEM_EVENT STOPPED RIGHT HAND SENSOR")
