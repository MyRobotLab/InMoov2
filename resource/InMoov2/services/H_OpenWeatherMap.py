# -- coding: utf-8 --
# ##############################################################################
#                 OPENWEATHERMAP FILE
# ##############################################################################

security.loadStore()
apikey = security.getSecret("OPENWEATHERMAP")

# forecast index 1 is next 3 hours , so 24 hours is 8
def isTheSunShiny(townParam="town",period=1):
  if runtime.isStarted('i01.openWeatherMap'):
    if apikey==None:
      i01_chatBot.getResponse("SYSTEM openweathermapError")
      runtime.error("open weathermap, key error")
    else:
      openWeatherMap=i01_openWeatherMap
      town=openWeatherMap.getConfig().currentTown
      if town==None:
        i01_chatBot.getResponse("SYSTEM openweathermapError")
        runtime.error("open weathermap error, this town is unrecognized")
      else:
        setUnits=openWeatherMap.getConfig().currentUnits
        if setUnits==None:
          i01_chatBot.getResponse("SYSTEM openweathermapError")
          runtime.error("open weathermap error, units are not defined")
        else:
          if townParam=="town" or townParam=="":townParam=town  
          openWeatherMap.setUnits(setUnits)
          openWeatherMap.setLocation(townParam)
          openWeatherMap.setPeriod(period)
          curtemperature=openWeatherMap.getDegrees()
          rawCode=openWeatherMap.getWeatherCode()
          i01_chatBot.getResponse("SYSTEM METEO curtemperature " + str(int(curtemperature)) + " Town " + str(townParam.split(',')[0] + " COMMENTAIRE " + str(rawCode)))
  else:
      i01_chatBot.getResponse("SYSTEM openweathermapNotStarted")
      runtime.error("open weathermap not started or maybe not configured")
