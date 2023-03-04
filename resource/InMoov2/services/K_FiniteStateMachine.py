# -- coding: utf-8 --
# ##############################################################################
#                 FINITE STATE MACHINE SERVICE FILE
# ##############################################################################

#i01_fsm = runtime.start("i01.fsm","FiniteStateMachine")
if runtime.isStarted('i01.fsm'):
    i01_fsm.getConfig()

    # add states
    i01_fsm.addState("boot")# fist time
    i01_fsm.addState("applyingConfig")# fist time
    i01_fsm.addState("getUserInfo")
    i01_fsm.addState("systemCheck")
    i01_fsm.addState("start")# fist time
    i01_fsm.addState("init")# fist time
    i01_fsm.addState("identify_user")# fist time
    i01_fsm.addState("detected_face")# fist time
    i01_fsm.addState("sleeping")# pir running ? wake word ?
    i01_fsm.addState("executing_gesture")# gesture running
    i01_fsm.addState("safe_random_movements")# random movements
    i01_fsm.addState("unsafe_random_movements")# random movements
    i01_fsm.addState("tracking")# tracking
    i01_fsm.addState("power_down")# process of shutting down stuff
    i01_fsm.addState("awake")
    i01_fsm.addState("sleeping")

    # woah - can handle multiple states - it propegates
    # events across all of them


    # add 8 transitions of 2 types
    i01_fsm.addTransition("start", "first_time", "init")
    i01_fsm.addTransition("init", "first_time", "identify_user")
    i01_fsm.addTransition("detected_face", "first_time", "identify_user")
    i01_fsm.addTransition("awake", "sleep", "sleeping")
    i01_fsm.addTransition("sleeping", "wake", "awake")
    i01_fsm.addTransition("boot", "configStarted", "applyingConfig")
    i01_fsm.addTransition("applyingConfig", "getUserInfo", "getUserInfo")
    i01_fsm.addTransition("applyingConfig", "systemCheck", "systemCheck")
    i01_fsm.addTransition("applyingConfig", "wake", "awake")
    i01_fsm.addTransition("getUserInfo", "systemCheck", "systemCheck")
    i01_fsm.addTransition("systemCheck", "wake", "awake")

    i01_fsm.fire("clear-event")
    print(i01_fsm.getCurrentState())
    sleep(1)

    #i01_fsm.fire("wake")
    #print(i01_fsm.getCurrentState())
    #sleep(1)
