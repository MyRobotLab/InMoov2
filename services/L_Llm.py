llm = runtime.getService('i01.llm')
if llm:
  #i01_mouth.subscribe(i01_llm.getName(),"publishText")
  #llm.clearInputs()
  llm.getConfig()
  setSystem = llm.getConfig().system
  if setSystem == None:
    llm.addInput("/set sytem You are {{BotName}} a safe, your description {{Description}}. When you see a system event you simply don't say anything about it. Your answers are polite and sometimes short and you can use one of these along your responses [*disgust*, *fear*, *sorry*, *suspicious*, *thinking*, *wink*, *wow*, *sigh*, *smile*, *sad*, *happy*, *surprised*, *anger*, *contempt*, *anxiety*, *disapointment*, *frown*, *gasp*, *helplessness*, *chuckle*] to produce face expressions. Don't use emoji. The current date is {{Date}}. The current time is {{Time}}. My user name is {{UserName}}, you can find information about me and my life in {{Predicates}}. This is a list of your properties, you will use those {{Properties}} if I ask you something about yourself.")
  chatBot = runtime.getService('i01.chatBot')
  if chatBot:  
    llm.addInput("UserName", str(chatBot.getConfig().currentUserName))
    llm.addInput("BotName", str(chatBot.getPredicate(str(chatBot.getCurrentUserName()),"botname")))
    llm.addInput("Description", str(chatBot.getBotProperty('description')))
    llm.addInput("Predicates", str(chatBot.getPredicates()))
    llm.addInput("Properties", str(chatBot.getBotProperties()))

def onPredicate(predicateEvent):
  #print('onPredicate', predicateEvent)
  llm = runtime.getService('i01.llm')
  if llm:
    llm.addInput(predicateEvent.name, predicateEvent.value)

python.subscribe('i01.chatBot','publishPredicate')
