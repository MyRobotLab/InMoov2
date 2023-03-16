# -- coding: utf-8 --
# ##############################################################################
#                 OPENWEATHERMAP FILE
# ##############################################################################


security.loadStore()
apikey = security.getSecret("OPENWEATHERMAP")
def initOwm():
  apikey = security.getSecret("OPENWEATHERMAP")

# forecast index 1 is next 3 hours , so 24 hours is 8
def isTheSunShiny(townParam="town",period=1):
  if runtime.isStarted('i01.openWeatherMap'):
    initOwm()
    if apikey==None:
      runtime.warn('open weathermap key error')
      errorSpokenFunc("ALERT",", open weathermap key error")
    else:
      openWeatherMap=i01_openWeatherMap
      town=openWeatherMap.getConfig().currentTown
      if town==None:
        runtime.warn('open weathermap town is unrecognized')
        errorSpokenFunc("ALERT",", open weathermap town is unrecognized")
      else:
        setUnits=openWeatherMap.getConfig().currentUnits
        if setUnits==None:
          runtime.warn('open weathermap units not defined')
          errorSpokenFunc("ALERT",", open weathermap units not defined") 
        else:
          if townParam=="town" or townParam=="":townParam=town  
          openWeatherMap.setUnits(setUnits)
          openWeatherMap.setLocation(townParam)
          openWeatherMap.setPeriod(period)
          curtemperature=openWeatherMap.getDegrees()
          rawCode=openWeatherMap.getWeatherCode()
          i01_chatBot.getResponse("SYSTEM METEO curtemperature " + str(int(curtemperature)) + " Town " + str(townParam.split(',')[0] + " COMMENTAIRE " + str(rawCode)))
  else:
      errorSpokenFunc("ALERT",", open weathermap not started or maybe not configured")
