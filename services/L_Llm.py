# -- coding: utf-8 --
en = 'en-US'
fi = 'fi-FI'
fr = 'fr-FR'
hi = 'hi-IN'
es = 'es-ES'
de = 'de-DE'
it = 'it-IT'
nl = 'nl-NL'
pl = 'pl-PL'
pt = 'pt-PT'
ru = 'ru-RU'
tr = 'tr-TR'
def initLlm():
  llm = runtime.getService('i01.llm')
  chatBot = runtime.getService('i01.chatBot')
  if runtime.isStarted('i01.llm'):
    llm.clearInputs()
    llm.getConfig()
    setSystem = llm.getConfig().system
    runtime.getConfig()
    python.subscribe(llm.getName(), "publishText", "onFilterText")
    config = llm.getConfig()
    if config.url == "http://localhost:11434" or config.url == "http://localhost:11434/v1/chat/completions":
        config.url = "http://localhost:11434/api/generate"
    if setSystem == "You are a helpful robot.":
      if runtime.getLocale().getTag() == en:
        config.system = u"You are {{BotName}} a safe AI assistant.\
   When you see a system_event you simply don't say anything about it.\
   Your answers are polite and sometimes short.\
   You can use one of these along your responses [*disgust*, *fear*, *sorry*, *suspicious*, *thinking*, *wink*, *wow*, *smile*, *sad*, *happy*, *surprise*, *anger*, *contempt*, *anxiety*, *disapointment*, *frown*, *gasp*, *helplessness*, *chuckle*] to produce face expressions. Don't use emoji. The current date is {{Date}}.\
   The current time is {{Time}}.\
   The current date is {{Date}}.\
   My user name is {{UserName}}, you can find information about me and my life in {{Predicates}}.\
   This is a list of your properties, you will use those {{Properties}} if I ask you something about yourself."
      if runtime.getLocale().getTag() == fi:
        config.system = u"Always respond in Finnish. You are {{BotName}} a safe AI assistant.\
   When you see a system_event you simply don't say anything about it.\
   Your answers are polite and sometimes short.\
   You can use one of these along your responses [*disgust*, *fear*, *sorry*, *suspicious*, *thinking*, *wink*, *wow*, *smile*, *sad*, *happy*, *surprise*, *anger*, *contempt*, *anxiety*, *disapointment*, *frown*, *gasp*, *helplessness*, *chuckle*] to produce face expressions. Don't use emoji. The current date is {{Date}}.\
   The current time is {{Time}}.\
   The current date is {{Date}}.\
   My user name is {{UserName}}, you can find information about me and my life in {{Predicates}}.\
   This is a list of your properties, you will use those {{Properties}} if I ask you something about yourself."
      if runtime.getLocale().getTag() == fr:
        config.system = u"Always respond in French. You are {{BotName}} a safe AI assistant.\
   When you see a system_event you simply don't say anything about it.\
   Your answers are polite and sometimes short.\
   You can use one of these along your responses [*disgust*, *fear*, *sorry*, *suspicious*, *thinking*, *wink*, *wow*, *smile*, *sad*, *happy*, *surprise*, *anger*, *contempt*, *anxiety*, *disapointment*, *frown*, *gasp*, *helplessness*, *chuckle*] to produce face expressions. Don't use emoji. The current date is {{Date}}.\
   The current time is {{Time}}.\
   The current date is {{Date}}.\
   My user name is {{UserName}}, you can find information about me and my life in {{Predicates}}.\
   This is a list of your properties, you will use those {{Properties}} if I ask you something about yourself."
      if runtime.getLocale().getTag() == hi:
        config.system = u"Always respond in Hindi. You are {{BotName}} a safe AI assistant.\
   When you see a system_event you simply don't say anything about it.\
   Your answers are polite and sometimes short.\
   You can use one of these along your responses [*disgust*, *fear*, *sorry*, *suspicious*, *thinking*, *wink*, *wow*, *smile*, *sad*, *happy*, *surprise*, *anger*, *contempt*, *anxiety*, *disapointment*, *frown*, *gasp*, *helplessness*, *chuckle*] to produce face expressions. Don't use emoji. The current date is {{Date}}.\
   The current time is {{Time}}.\
   The current date is {{Date}}.\
   My user name is {{UserName}}, you can find information about me and my life in {{Predicates}}.\
   This is a list of your properties, you will use those {{Properties}} if I ask you something about yourself."
      if runtime.getLocale().getTag() == es:
        config.system = u"Always respond in Spanish. You are {{BotName}} a safe AI assistant.\
   When you see a system_event you simply don't say anything about it.\
   Your answers are polite and sometimes short.\
   You can use one of these along your responses [*disgust*, *fear*, *sorry*, *suspicious*, *thinking*, *wink*, *wow*, *smile*, *sad*, *happy*, *surprise*, *anger*, *contempt*, *anxiety*, *disapointment*, *frown*, *gasp*, *helplessness*, *chuckle*] to produce face expressions. Don't use emoji. The current date is {{Date}}.\
   The current time is {{Time}}.\
   The current date is {{Date}}.\
   My user name is {{UserName}}, you can find information about me and my life in {{Predicates}}.\
   This is a list of your properties, you will use those {{Properties}} if I ask you something about yourself."
      if runtime.getLocale().getTag() == de:
        config.system = u"Always respond in German. You are {{BotName}} a safe AI assistant.\
   When you see a system_event you simply don't say anything about it.\
   Your answers are polite and sometimes short.\
   You can use one of these along your responses [*disgust*, *fear*, *sorry*, *suspicious*, *thinking*, *wink*, *wow*, *smile*, *sad*, *happy*, *surprise*, *anger*, *contempt*, *anxiety*, *disapointment*, *frown*, *gasp*, *helplessness*, *chuckle*] to produce face expressions. Don't use emoji. The current date is {{Date}}.\
   The current time is {{Time}}.\
   The current date is {{Date}}.\
   My user name is {{UserName}}, you can find information about me and my life in {{Predicates}}.\
   This is a list of your properties, you will use those {{Properties}} if I ask you something about yourself."
      if runtime.getLocale().getTag() == it:
        config.system = u"Always respond in Italian. You are {{BotName}} a safe AI assistant.\
   When you see a system_event you simply don't say anything about it.\
   Your answers are polite and sometimes short.\
   You can use one of these along your responses [*disgust*, *fear*, *sorry*, *suspicious*, *thinking*, *wink*, *wow*, *smile*, *sad*, *happy*, *surprise*, *anger*, *contempt*, *anxiety*, *disapointment*, *frown*, *gasp*, *helplessness*, *chuckle*] to produce face expressions. Don't use emoji. The current date is {{Date}}.\
   The current time is {{Time}}.\
   The current date is {{Date}}.\
   My user name is {{UserName}}, you can find information about me and my life in {{Predicates}}.\
   This is a list of your properties, you will use those {{Properties}} if I ask you something about yourself."
      if runtime.getLocale().getTag() == nl:
        config.system = u"Always respond in Dutch. You are {{BotName}} a safe AI assistant.\
   When you see a system_event you simply don't say anything about it.\
   Your answers are polite and sometimes short.\
   You can use one of these along your responses [*disgust*, *fear*, *sorry*, *suspicious*, *thinking*, *wink*, *wow*, *smile*, *sad*, *happy*, *surprise*, *anger*, *contempt*, *anxiety*, *disapointment*, *frown*, *gasp*, *helplessness*, *chuckle*] to produce face expressions. Don't use emoji. The current date is {{Date}}.\
   The current time is {{Time}}.\
   The current date is {{Date}}.\
   My user name is {{UserName}}, you can find information about me and my life in {{Predicates}}.\
   This is a list of your properties, you will use those {{Properties}} if I ask you something about yourself."
      if runtime.getLocale().getTag() == pl:
        config.system = u"Always respond in Polish. You are {{BotName}} a safe AI assistant.\
   When you see a system_event you simply don't say anything about it.\
   Your answers are polite and sometimes short.\
   You can use one of these along your responses [*disgust*, *fear*, *sorry*, *suspicious*, *thinking*, *wink*, *wow*, *smile*, *sad*, *happy*, *surprise*, *anger*, *contempt*, *anxiety*, *disapointment*, *frown*, *gasp*, *helplessness*, *chuckle*] to produce face expressions. Don't use emoji. The current date is {{Date}}.\
   The current time is {{Time}}.\
   The current date is {{Date}}.\
   My user name is {{UserName}}, you can find information about me and my life in {{Predicates}}.\
   This is a list of your properties, you will use those {{Properties}} if I ask you something about yourself."
      if runtime.getLocale().getTag() == pt:
        config.system = u"Always respond in Portuguese. You are {{BotName}} a safe AI assistant.\
   When you see a system_event you simply don't say anything about it.\
   Your answers are polite and sometimes short.\
   You can use one of these along your responses [*disgust*, *fear*, *sorry*, *suspicious*, *thinking*, *wink*, *wow*, *smile*, *sad*, *happy*, *surprise*, *anger*, *contempt*, *anxiety*, *disapointment*, *frown*, *gasp*, *helplessness*, *chuckle*] to produce face expressions. Don't use emoji. The current date is {{Date}}.\
   The current time is {{Time}}.\
   The current date is {{Date}}.\
   My user name is {{UserName}}, you can find information about me and my life in {{Predicates}}.\
   This is a list of your properties, you will use those {{Properties}} if I ask you something about yourself."
      if runtime.getLocale().getTag() == ru:
        config.system = u"Always respond in Russian. You are {{BotName}} a safe AI assistant.\
   When you see a system_event you simply don't say anything about it.\
   Your answers are polite and sometimes short.\
   You can use one of these along your responses [*disgust*, *fear*, *sorry*, *suspicious*, *thinking*, *wink*, *wow*, *smile*, *sad*, *happy*, *surprise*, *anger*, *contempt*, *anxiety*, *disapointment*, *frown*, *gasp*, *helplessness*, *chuckle*] to produce face expressions. Don't use emoji. The current date is {{Date}}.\
   The current time is {{Time}}.\
   The current date is {{Date}}.\
   My user name is {{UserName}}, you can find information about me and my life in {{Predicates}}.\
   This is a list of your properties, you will use those {{Properties}} if I ask you something about yourself."
      if runtime.getLocale().getTag() == tr:
        config.system = u"Always respond in Turkish. You are {{BotName}} a safe AI assistant.\
   When you see a system_event you simply don't say anything about it.\
   Your answers are polite and sometimes short.\
   You can use one of these along your responses [*disgust*, *fear*, *sorry*, *suspicious*, *thinking*, *wink*, *wow*, *smile*, *sad*, *happy*, *surprise*, *anger*, *contempt*, *anxiety*, *disapointment*, *frown*, *gasp*, *helplessness*, *chuckle*] to produce face expressions. Don't use emoji. The current date is {{Date}}.\
   The current time is {{Time}}.\
   The current date is {{Date}}.\
   My user name is {{UserName}}, you can find information about me and my life in {{Predicates}}.\
   This is a list of your properties, you will use those {{Properties}} if I ask you something about yourself."
      llm.removeListener('publishText', 'i01.htmlFilter', 'onText')  
      llm.save()  
      llm.apply(config)
      llm.broadcastState()
    if chatBot:
      llm.addInput("UserName", unicode(chatBot.getConfig().currentUserName,'utf-8'))
      llm.addInput("BotName", unicode(chatBot.getPredicate(chatBot.getCurrentUserName(),"botname"),'utf-8'))
      llm.addInput("Predicates", unicode(chatBot.getPredicates(),'utf-8'))
      llm.addInput("Properties", unicode(chatBot.getBotProperties(),'utf-8'))

initLlm()

def onPredicate(predicateEvent):
  #print('onPredicate', predicateEvent)
  llm = runtime.getService('i01.llm')
  if llm:
    llm.addInput(predicateEvent.name, predicateEvent.value)

python.subscribe('i01.chatBot','publishPredicate')

def describeImage(prompt):
  if runtime.isStarted('i01.llmImg'):
    llmImg = runtime.getService('i01.llmImg')
    if runtime.isStarted('i01.opencv'):
      opencv = runtime.getService('i01.opencv')
      if opencv.isCapturing():
        # make a subscription
        i01_llmImg.subscribe('i01.opencv','publishImage')
        # capture and save an image
        # the save image will be publishImage and be sent
        # to the llmImg
        opencv.saveImage()
      else:  
        # make a subscription
        i01_llmImg.subscribe('i01.opencv','publishImage')
        # capture and save an image
        # the save image will be publishImage and be sent
        # to the llmImg
        opencv.capture()
        opencv.saveImage()
        sleep(0.1)
        opencv.stopCapture()
    else:
      opencv = runtime.start('i01.opencv', 'OpenCV')
      # make a subscription
      i01_llmImg.subscribe('i01.opencv','publishImage')
      # capture and save an image
      # the save image will be publishImage and be sent
      # to the llmImg
      opencv.capture()
      opencv.saveImage()
      sleep(0.1)
      opencv.stopCapture()

  else:
    llmImg = runtime.start('i01.llmImg', 'LLM')
    opencv = runtime.start('i01.opencv', 'OpenCV')
    cfg = llmImg.getConfig()
    if runtime.getLocale().getTag() == en:
      cfg.defaultImagePrompt = u"What do you see?"
    if runtime.getLocale().getTag() == fi:
      cfg.defaultImagePrompt = u"Vastaa aina suomeksi. Mitä näet?"
    if runtime.getLocale().getTag() == fr:
      cfg.defaultImagePrompt = u"Réponds toujours en Français. Que vois-tu?"
    if runtime.getLocale().getTag() == hi:
      cfg.defaultImagePrompt = u"हमेशा हिंदी में जवाब दें. आप क्या देखते हैं?"
    if runtime.getLocale().getTag() == es:
      cfg.defaultImagePrompt = u"Responde siempre en español. ¿Qué ves?"
    if runtime.getLocale().getTag() == de:
      cfg.defaultImagePrompt = u"Antworten Sie immer auf Deutsch. Was siehst du??"
    if runtime.getLocale().getTag() == it:
      cfg.defaultImagePrompt = u"Rispondi sempre in italiano. Cosa vedi??"
    if runtime.getLocale().getTag() == nl:
      cfg.defaultImagePrompt = u"Reageer altijd in het Nederlands. Wat zie je?"
    if runtime.getLocale().getTag() == pl:
      cfg.defaultImagePrompt = u"Zawsze odpowiadaj po polsku. Co widzisz?"
    if runtime.getLocale().getTag() == pt:
      cfg.defaultImagePrompt = u"Sempre responda em português. O que você vê?"
    if runtime.getLocale().getTag() == ru:
      cfg.defaultImagePrompt = u"Всегда отвечайте на русском языке. Что ты видишь?"
    if runtime.getLocale().getTag() == tr:
      cfg.defaultImagePrompt = u"Daima Türkçe yanıt verin. Ne görüyorsun?"        
    if cfg.url == "http://localhost:11434/api/generate" or cfg.url == "http://localhost:11434/v1/chat/completions":
      cfg.url = "http://localhost:11434"
    if cfg.model == None or "llama2" or "llama3" or "phi3" or "mistral" or "mixtral":
      cfg.model = "llava"
    if cfg.stream == "false":
      cfg.stream = "true"
    python.subscribe(llmImg.getName(), "publishText", "onFilterText")
    #i01_htmlFilter.subscribe(llmImg.getName(), "publishText", "onText")
    llmImg.removeListener('publishText', 'i01.htmlFilter', 'onText')
    llmImg.apply(cfg)
    llmImg.save()
    llmImg.broadcastState()
    # make a subscription
    i01_llmImg.subscribe('i01.opencv','publishImage')
    # capture and save an image
    # the save image will be publishImage and be sent
    # to the llmImg
    opencv.capture()
    opencv.saveImage()
    sleep(0.1)
    opencv.stopCapture()
  
