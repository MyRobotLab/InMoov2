# -- coding: utf-8 --
# ##############################################################################
#                 FINITE STATE MACHINE SERVICE FILE
# ##############################################################################

i01_fsm = i01.startPeer('fsm')
def initFsm():
    i01_fsm.getConfig()

if runtime.isStarted('i01.fsm'):
    initFsm()
    i01_fsm.addTransition("idle","track","isTracking")
    i01_fsm.addTransition("isTracking","stopTrack","idle")
    print(i01_fsm.getState())
    sleep(1)