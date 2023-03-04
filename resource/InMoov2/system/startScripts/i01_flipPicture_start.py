configFilename="data/InMoov2/i01.life.yml"
# open the file
file = open(configFilename, "r")
print("true")
# read the file
text = file.read()

# search & replace the word
replaced_text = text.replace("flipPicture=False", "flipPicture=True")

# save the file
file = open(configFilename, "w")
file.write(replaced_text)
file.close()

execfile('resource/InMoov2/life/0_inmoovLife.py')

if runtime.isStarted('i01.opencv'):
  if flipPicture==1:i01_opencv.addFilter("Flip")
