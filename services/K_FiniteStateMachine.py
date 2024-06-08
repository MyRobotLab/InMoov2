# -- coding: utf-8 --
# ##############################################################################
#                 FINITE STATE MACHINE SERVICE FILE
# ##############################################################################

fsm = i01.startPeer('fsm')
fsm = runtime.getService('i01.fsm')
def initFsm():
    fsm.getConfig()

if runtime.isStarted('i01.fsm'):
    initFsm()
    fsm.addTransition("idle","track","isTracking")
    fsm.addTransition("isTracking","stopTrack","idle")
    print(fsm.getState())
    sleep(1)
    
