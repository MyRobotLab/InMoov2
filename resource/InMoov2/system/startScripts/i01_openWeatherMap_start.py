#########################################
# i01_openWeatherMap_start.py
# categories: inmoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################

i01_openWeatherMap = Runtime.start("i01.openWeatherMap","OpenWeatherMap")

#apikey = XXXXXXXXXX
# Get your KEY : https://home.openweathermap.org
#setUnits = metric
# or imperial
#townParam = paris,FR
#period = 1

# forecast index 1 is next 3 hours , so 24 hours is 8
def isTheSunShiny(townParam="town",period=1):  
    if townParam=="town" or townParam=="":townParam=town
    i01_openWeatherMap.setLocation(townParam)
    i01_openWeatherMap.setPeriod(period)
    curtemperature=i01_openWeatherMap.getDegrees()
    rawCode=i01_openWeatherMap.getWeatherCode()
    if not rawCode==0:
        if runtime.isStarted('i01.chatBot'):
            i01_chatBot.getResponse("SYSTEM METEO curtemperature " + str(int(curtemperature)) + " Town " + str(townParam.split(',')[0] + " COMMENTAIRE " + str(rawCode)))
        else:
            i01_chatBot.getResponse("SYSTEM openweathermapError")
    else:
        i01.warn("there no chatBot set to give a response")