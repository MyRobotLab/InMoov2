# -- coding: utf-8 --
# ##############################################################################
#                 FINITE STATE MACHINE SERVICE FILE
# ##############################################################################

i01.startPeer('fsm')
if runtime.isStarted('i01.fsm'):
    i01_fsm.getConfig()

    i01_fsm.addTransition("awake","track","isTracking")
    i01_fsm.addTransition("isTracking","stopTrack","awake")
    #i01_fsm.fire("clear-event")
    print(i01_fsm.getCurrent())
    sleep(1)
