# -- coding: utf-8 --
# ##############################################################################
#                 OPENWEATHERMAP FILE
# ##############################################################################


def initOwm():
  security.loadStore()
  global apikey
  apikey = security.getSecret("OPENWEATHERMAP")

# forecast index 1 is next 3 hours , so 24 hours is 8
def isTheSunShiny(townParam="town",period=1):
  if runtime.isStarted('i01.openWeatherMap'):
    initOwm()
    global apikey
    if apikey==None:
      runtime.warn('open weathermap key error')
      if runtime.isStarted('i01.chatBot'):
        i01_chatBot.getResponse("SYSTEM_ERROR_OPENWEATHERMAP_1")
    else:
      openWeatherMap=i01_openWeatherMap
      town=openWeatherMap.getConfig().currentTown
      if town==None:
        runtime.warn('open weathermap town is unrecognized')
        if runtime.isStarted('i01.chatBot'):
          i01_chatBot.getResponse("SYSTEM_ERROR_OPENWEATHERMAP_2")
      else:
        setUnits=openWeatherMap.getConfig().currentUnits
        if setUnits==None:
          runtime.warn('open weathermap units not defined')
          if runtime.isStarted('i01.chatBot'):
            i01_chatBot.getResponse("SYSTEM_ERROR_OPENWEATHERMAP_3") 
        else:
          if townParam=="town" or townParam=="":townParam=town  
          openWeatherMap.setUnits(setUnits)
          openWeatherMap.setLocation(townParam)
          openWeatherMap.setPeriod(period)
          curtemperature=openWeatherMap.getDegrees()
          rawCode=openWeatherMap.getWeatherCode()
          i01_chatBot.getResponse("SYSTEM METEO curtemperature " + str(int(curtemperature)) + " Town " + str(townParam.split(',')[0] + " COMMENTAIRE " + str(rawCode)))
  else:
    if runtime.isStarted('i01.chatBot'):
      i01_chatBot.getResponse("SYSTEM_ERROR_OPENWEATHERMAP_4")

