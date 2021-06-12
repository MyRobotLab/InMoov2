# ##############################################################################
#                 VIRTUAL INMOOV SERVICE
# ##############################################################################

# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')

isSimulatorActivated=ThisServicePartConfig.getboolean('MAIN', 'isSimulatorActivated')
VinmoovMonitorActivated=ThisServicePartConfig.getboolean('MAIN', 'VinmoovMonitorActivated')
ForceVinmoovDisable=False
try:
  ForceVinmoovDisable=ThisServicePartConfig.getboolean('MAIN', 'ForceVinmoovDisable')
except:
  pass

global virtualInmoovActivated
virtualInmoovActivated=False
if (ScriptType=="Virtual" or isSimulatorActivated) and not ForceVinmoovDisable:
  if os.path.isdir(RuningFolder+'/JMonkeyEngine/assets/Models') and runtime.is64bit():
  #if os.path.isdir('data/JMonkeyEngine/assets/Models') and runtime.is64bit():
    global virtualInmoovActivated
    virtualInmoovActivated=True
    i01.setVirtual(True)
    jme = i01.startSimulator()
  else:
    errorSpokenFunc("VINMOOVNOWORKY")


#virtual inmoov
# FIXME i01.VinmoovMonitorActivated=VinmoovMonitorActivated
# FIXME i01.VinmoovFullScreen=0
# FIXME i01.VinmoovBackGroundColor="Grey"
# FIXME i01.VinmoovWidth=800
