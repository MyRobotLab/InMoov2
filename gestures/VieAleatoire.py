def VieAleatoire():
    execfile('resource/InMoov2/system/startScripts/i01_random_start.py')
    if runtime.isStarted('MoveRandomTimer'):
        MoveRandomTimer.startClock()
        MoveRandomStart()
    if runtime.isStarted('moveHeadRandomize'):
        moveHeadRandomize.enable()
    if runtime.isStarted('moveBodyRandomize'):
        moveBodyRandomize.enable()
