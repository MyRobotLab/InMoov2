configFilename="data/InMoov2/i01.life.yml"
# open the file
file = open(configFilename, "r")
# read the file
text = file.read()
# search & replace the word
replaced_text = text.replace("boot_green=True", "boot_green=False")

# save the file
file = open(configFilename, "w")
file.write(replaced_text)
file.close()
