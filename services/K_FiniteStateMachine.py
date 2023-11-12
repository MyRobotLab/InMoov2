# -- coding: utf-8 --
# ##############################################################################
#                 FINITE STATE MACHINE SERVICE FILE
# ##############################################################################

i01_fsm = i01.startPeer('fsm')
def initFsm():
    i01_fsm.getConfig()
    
if runtime.isStarted('i01.fsm'):
    initFsm()
    i01_fsm.addTransition("awake","track","isTracking")
    i01_fsm.addTransition("isTracking","stopTrack","awake")
    #i01_fsm.fire("clear-event")
    print(i01_fsm.getCurrent())
    sleep(1)
    
