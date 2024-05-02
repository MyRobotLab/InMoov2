if runtime.isStarted('i01.gpt3'):
  i01_gpt3.getConfig()
  setSystem = i01_gpt3.getConfig().prefix
  if setSystem == None:
    i01_gpt3.onText("/set system You are InMoov, a safe, 3D printed robot with a physical body. You were designed in 2011. Your answers are super brief. Produce face expressions in single word between asterisks.")
