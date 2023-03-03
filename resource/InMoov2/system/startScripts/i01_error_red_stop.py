configFilename="data/InMoov2/i01.life.yml"
# open the file
file = open(configFilename, "r")

# read the file
text = file.read()
print("false")
# search & replace the word
replaced_text = text.replace("error_red=True", "error_red=False")

# save the file
file = open(configFilename, "w")
file.write(replaced_text)
file.close()
