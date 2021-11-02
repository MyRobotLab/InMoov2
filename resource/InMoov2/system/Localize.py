# we try to load user system language localization
if Language=="fr-FR"or"en-US"or"es-ES"or"de-DE"or"nl-NL"or"ru-RU"or"hi-IN"or"it-IT"or"fi-FI"or"pt-PT"or"tr-TR"or"cn-ZH":
  languageError=False
  Runtime.setAllLocales(Language)
else:
  if Language==None:
    languageError=True
    Runtime.setAllLocales('en-US')
  if (os.path.isdir(RuningFolder+'localization/'+Language)):
    try:
      #push local yolo dictionary
      shutil.copy(RuningFolder+'localization/'+Language+os.getcwd().replace("\\", "/"))
      #other translations   
    except:
      pass
