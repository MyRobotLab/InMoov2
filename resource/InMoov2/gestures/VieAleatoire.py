def VieAleatoire():
    if runtime.isStarted('MoveRandomTimer'):
        MoveRandomTimer.startClock()
        MoveRandomStart()
    if runtime.isStarted('moveHeadRandomize'):
        moveHeadRandomize.enable()
    if runtime.isStarted('moveBodyRandomize'):
        moveBodyRandomize.enable()
