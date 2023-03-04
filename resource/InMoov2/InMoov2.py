##						   ___  ________   _____ ______   ________  ________  ___      ___ 
##						  |\  \|\   ___  \|\   _ \  _   \|\   __  \|\   __  \|\  \    /  /|
##						  \ \  \ \  \\ \  \ \  \\\__\ \  \ \  \|\  \ \  \|\  \ \  \  /  / /
##						   \ \  \ \  \\ \  \ \  \\|__| \  \ \  \\\  \ \  \\\  \ \  \/  / / 
##						    \ \  \ \  \\ \  \ \  \    \ \  \ \  \\\  \ \  \\\  \ \    / /  
##						     \ \__\ \__\\ \__\ \__\    \ \__\ \_______\ \_______\ \__/ /   
##						      \|__|\|__| \|__|\|__|     \|__|\|_______|\|_______|\|__|/    
version='1.1.12'

# this will run with Nixie versions of MRL above :
# THIS IS NOT FOR MANTICORE
mrlCompatible='1.1.1060'


##############
# Main inmoov service
#i01 = runtime.start("i01", "InMoov2")
#runtime.startConfig('InMoov2_Full')
##############
# robot checkup and initialisation ( skeleton & services )
RuningFolder="resource/InMoov2"
execfile(RuningFolder+'/system/InitCheckup2.py')
