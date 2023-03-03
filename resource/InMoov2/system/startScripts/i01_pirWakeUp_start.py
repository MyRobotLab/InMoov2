configFilename="data/InMoov2/i01.life.yml"
# open the file
file = open(configFilename, "r")
print("true")
# read the file
text = file.read()

# search & replace the word
replaced_text = text.replace("pirWakeUp=False", "pirWakeUp=True")

# save the file
file = open(configFilename, "w")
file.write(replaced_text)
file.close()    
