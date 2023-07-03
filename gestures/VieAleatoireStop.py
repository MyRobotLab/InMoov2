def VieAleatoireStop():
    if runtime.isStarted('MoveRandomTimer'):
        MoveRandomTimer.stopClock()
        MoveRandomStop()
    if runtime.isStarted('moveHeadRandomize'):
        moveHeadRandomize.disable()
    if runtime.isStarted('moveBodyRandomize'):
        moveBodyRandomize.disable()

  