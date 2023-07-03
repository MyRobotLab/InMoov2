# -- coding: utf-8 --
# ##############################################################################
#                 FINITE STATE MACHINE SERVICE FILE
# ##############################################################################

i01_fsm = runtime.start("i01.fsm","FiniteStateMachine")
if runtime.isStarted('i01.fsm'):
    i01_fsm.getConfig()

    i01_fsm.fire("clear-event")
    print(i01_fsm.getCurrent())
    sleep(1)
