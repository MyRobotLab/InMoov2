# we try to load user system language pack
  
if (os.path.isdir(RuningFolder+'localization/'+Language)):
  try:
    #push local yolo dictionary
    shutil.copy(RuningFolder+'localization/'+Language+os.getcwd().replace("\\", "/"))
    #other translations   
  except:
    pass
