configFilename="data/InMoov2/i01.life.yml"
# open the file
file = open(configFilename, "r")

# read the file
text = file.read()
print("false")
# search & replace the word
replaced_text = text.replace("flash_when_speak=True", "flash_when_speak=False")

# save the file
file = open(configFilename, "w")
file.write(replaced_text)
file.close()