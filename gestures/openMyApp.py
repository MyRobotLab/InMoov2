import os
## Below you can add path to your favorite apps,
## to be launched with the voice command EXECUTE *
## As an exemple the command would be EXECUTE OPEN OFFICE 
def openMyApp(data):
  if (data == 'kisslicer'):
    path1 =  'D:\\Programs\\kisslicer_1.6.3\\KISSlicer64.exe'
    os.system('"' + path1 + '"')
  if (data == 'open office'):
    path2 = 'C:\\Program Files (x86)\\OpenOffice 4\\program\\soffice.exe'
    os.system('"' + path2 + '"')
  else:
    i01_chatBot.getResponse("SAY " + "This program is not in my data" + str(data))
