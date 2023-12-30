# IMPORTANT - Jython could call overloaded methods, Py4j cannot !!!
# names are guaranteed to be unique
# the kluge of changing period to underscore
# auto create globals ? (bad idea)
# isolate to callbacks
# from py4j.java_gateway import JavaObject

# unsuccessful attempt to modularize
# class InMoov2(JavaObject):
#     global runtime

#     def __init__(self, name):
#         # super().__init__(runtime.start(name, "InMoov2"))
#         super().__init__("blah", handler.gateway)
#         self.name = name
#         self.robot = runtime.start(name, "InMoov2")

# RELOAD SCRIPT
# with open('src/main/resources/resource/InMoov2/InMoov2.py', 'r') as file:
#     script_code = file.read()
# exec(script_code)


# FOR SUBSCRIPTIONS WHOS DESTINATION IS PYTHON
# SHOULD PROBABLY BE MAINTAINED HERE


def onPythonMessage(msg):
    # FIXME - don't know hot to fix yet
    global python_runtime
    """Initial processing point for all messages.
    Messages are sent from the Java side to the Python side,
    then decoded and routed to the appropriate method.

    Decoding msg is unwrapped from the tunnelled message, and
    the python method is called with a parameter of the tunnelled.sender
    e.g.
      onCallback('i01', data):
        # msg body
    
    The preferred way would be to use a python side service class where self is the
    first parameter, and the service is returned from the registry.

    e.g.
      onCallback(self, data):
        # msg body

    But I have not figured out how to augment py4j to do this... yet.

    Args:
        msg (_type_): tunnelled message, with data message
    """
    try:

        method_name = msg.get('method')
        sender = msg.get('sender')
        params_array = msg.get('data', [])
        params_array.insert(0, sender)

        # Check if the method exists in the global namespace
        if method_name in globals() and callable(globals()[method_name]):
            cmd = f"result = {method_name}(*params_array)"
            print(f'onPythonMessage cmd {cmd}')

            # Execute the code with the globals parameter
            exec_globals = globals()
            exec_globals['params_array'] = params_array
            exec(cmd, exec_globals)

            # Access the result from the executed code
            # result = exec_globals['result']
            # print("Result:", result)  # Output the result (you can modify this as needed)
        else:
            print(f"Method '{method_name}' not found or not callable.")

    except Exception as e:
        print(e)


# FIXME - global method not name specific
def onStartSpeaking(sender, text):
    global runtime

    print("onStartSpeaking", text)

    # FIXME FIXME FIXME name delivered as a parameter or
    # make class that is created by the runtime with name
    i01 = runtime.getService("i01")

    if i01:
        # i01_neoPixel = i01.getPeer("neoPixel")
        # if i01_neoPixel and i01.getConfig().neoPixelFlashWhenSpeaking:
        # i01_neoPixel.setAnimation("Ironman", 255, 255, 255, 20)

        # Great idea, but has hardcoded translations - this should be done in the language service but the
        # raw gesture still be processed
        # if 'oui ' in text or 'yes ' in text or ' oui' in text or 'ja ' in text or text=="yes" or text=="kyllä":Yes()
        # if 'non ' in text or 'no ' in text or 'nicht ' in text or 'neen ' in text or text=="no" or text=="ei":No()
        
        # force random move while speaking, to avoid conflict with random life gesture
        if i01.getConfig().robotCanMoveHeadWhileSpeaking:
            i01_random = runtime.getService("i01.random")
            if i01_random and i01.getState() != "tracking":
                i01_random.disableAll()
                i01_random.enable("i01.setHeadSpeed")
                i01_random.enable("i01.moveHead")
                i01_random.enable()


# FIXME - global method not name specific
def onEndSpeaking(sender, text):
    global runtime
    print('onEndSpeaking', text)
    i01 = runtime.getService("i01")
    i01_random = runtime.getService("i01.random")
    if i01_random and i01.getState() != "tracking":
        # i01_random.disable("i01.setHeadSpeed")
        # i01_random.disable("i01.moveHead")
        i01_random.disable()

    # if i01:
    #     if i01.getConfig().robotCanMoveHeadWhileSpeaking:
    #         i01_random = runtime.getService("i01.random")
    #         if i01_random:
    #             i01_random.disable()
    #             i01_random.enable('i01.moveLeftArm')
    #             i01_random.enable('i01.moveRightArm')
    #             i01_random.enable('i01.moveLeftHand')
    #             i01_random.enable('i01.moveRightHand')
    #             i01_random.enable('i01.moveTorso')
    #             i01_random.enable('i01.setLeftArmSpeed')
    #             i01_random.enable('i01.setRightArmSpeed')
    #             i01_random.enable('i01.setLeftHandSpeed')
    #             i01_random.enable('i01.setRightHandSpeed')
    #             i01_random.enable('i01.setTorsoSpeed')
    #             if runtime.isStarted('i01.head'):
    #                 i01_random.addRandom(200, 1000, "i01", "setHeadSpeed", 8.0, 20.0, 8.0, 20.0, 8.0, 20.0)
    #                 i01_random.addRandom(200, 1000, "i01", "moveHead", 70.0, 110.0, 65.0, 115.0, 70.0, 110.0)
    #         i01_neoPixel = runtime.getService('i01.neoPixel')
    #         if i01.getConfig().neoPixelFlashWhenSpeaking and runtime.isStarted("i01.neoPixel"):
    #             i01_neoPixel.clear()

# Sensor events begin ========================================


def on_pir_on(name):
    robot = runtime.getService(name)
    # FIXME - chatBot.getResponse("SYSTEM_EVENT on_start")
    mouth = robot.getPeer("mouth")
    mouth.speak("I feel your presence")
    print('on_pir_on', name)


def on_pir_off(name):
    robot = runtime.getService(name)
    # FIXME - chatBot.getResponse("SYSTEM_EVENT on_start")
    mouth = robot.getPeer("mouth")
    mouth.speak("I'm so alone")
    print('on_pir_off', name)

# Sensor events end ==========================================
# Topic events begin ========================================
# FIXME - since its a direct subscribe from i01.chatBot -to-> python
# we don't have a name - so we can't use the name as a parameter


def onTopic(topic_event):
    """Called when topic changes in chatbot,
    is rebroadcasted from InMoov2
    TopicEvent.
        botname = name of bot
        use = name of user
        topic = current topic
        src = name of source

    Args:
        topic (_type_): _description_
    """
    # FIXME - find a solution for the hardcoded name !
    # route through inmoov add name as field
    robot = runtime.getService(topic_event.src)
    mouth = robot.getPeer("mouth")
    if mouth:
        mouth.speak("New topic, the topic is " + topic_event.topic)
    print('onTopic', topic_event.topic)

# Topic events end ==========================================
# State change events begin ========================================


def onStateChange(state_event):
    """The main router for state changes
    it calls the appropriate method based on the state change
    Hooked to InMoov2.publishStateChange

    Args:
        data (InMoov2State): contains src and state
    """

    # Python 2 unicode pain
    state = str(state_event.state)
    src = str(state_event.src)

    robot = runtime.getService(src)

    # leaving state changes
    fsm = robot.getPeer("fsm")
    random = robot.getPeer("random")
    mouth = robot.getPeer("mouth")
    chatBot = robot.getPeer("chatBot")

    if fsm:
        leavingState = fsm.getPreviousState()

    if random and leavingState == "random":
        random.disable()

    if chatBot:
        chatBot.setPredicate("state", state)

    # if chatBot and leavingState == "first_init":
    #     # move the botname from human predicates to new user predicates
    #     # chatBot.setPredicate("botname", chatBot.getPredicate("human","botname")
    #     # this sets the first user to be the one identified at the end of first_init
    #     chatBot.setConfigValue("username", chatBot.getUsername())
    #     # Not sure if this should only be maintained in predicates
    #     # but config.username is the first session
    #     # it is "modifying" config hower, which might be difficult to support
    #     chatBot.save()

    # FIXME - chatBot.getResponse("SYSTEM_EVENT on_start")
    if mouth:
        mouth.speak("leaving " + leavingState + " state and entering " + state)

    print("on_state_change", src, state)

    # call the new state handler
    eval("on_" + state + "('" + src + "')")


def on_start(name):
    """Start is where all custom activity can begin.
    It is the first state changed called after boot.
    At this point InMoov2 service has started and andy
    runtime configuration has been processed. 
    The few services required to be running fsm chatBot and python
    will be running.  Other services may need to be checked
    e.g.
      opencv = runtime.getService("i01.opencv")
      if opencv:
          .... do something
    Args:
        name (string): name of service
    """
    robot = runtime.getService(name)
    chatbot = robot.getPeer("chatBot")
    # FIXME - chatBot.getResponse("SYSTEM_EVENT on_start")
    mouth = robot.getPeer("mouth")
    fsm = robot.getPeer("fsm")

    # iterate through all current started peers
    # and add subscriptions to this service ?
    # remove all the python subscriptions from InMoov2Config ?

    # FIXME - chatBot.getResponse("SYSTEM_EVENT on_start")
    if mouth:
        mouth.speak("I am starting")
    print("on_start state change from", name)
    # TODO - make a boot report and give it - errors and warnings ?
    # TODO - reporting in led display or verbal or wait for verbal

    # human by default is the first user and first predicate file
    # on startup try to identify the user
    if chatbot.getUsername() == "human":
        # try to identify user go through FIRST_INIT
        fsm.fire("first_init")
    else:
        # if user is known - go through WAKE_UP
        fsm.fire("wake")


def on_first_init(name):
    """Purpose of this state is to identify the user
    and first initial configuration of the robot. 

    The user should be asked to identify themselves.

    Various other information could be gathered as well
    although the user should be able to leave at any time.

    Coming back to this state should be possible at any time.

    Args:
        name (string): name of InMoov2 robot
    """
    robot = runtime.getService(name)
    chatbot = robot.getPeer("chatBot")
    chatbot.getResponse("NEW_USER")

    # do anything else desired
    # generate picture data of the user
    # go through personal questionare
    # e.g. ask 


def on_wake(name):
    robot = runtime.getService(name)
    chatbot = robot.getPeer("chatBot")
    chatbot.getResponse("WAKE_UP")
    print("on_wake state change from", name)


def on_idle(name):
    robot = runtime.getService(name)
    mouth = robot.getPeer("mouth")
    mouth.speak("I am idle")
    print("on_idle state change from", name)


def on_random(name):
    robot = runtime.getService(name)
    mouth = robot.getPeer("mouth")
    mouth.speak("I am doing random stuff")
    print("on_random state change from", name)


def on_sleep(name):
    robot = runtime.getService(name)
    mouth = robot.getPeer("mouth")
    mouth.speak("I am going to sleep")
    print("on_sleep state change from", name)
# State change events end ========================================
# Service change events begin ========================================


def on_peer_started(name):
    robot = runtime.getService(name)
    mouth = robot.getPeer("mouth")
    mouth.speak("I am starting a new service")
    print("on_peer_started service change from", name)
    # add subscriptions for newly started peers


def on_peer_released(name):
    robot = runtime.getService(name)
    mouth = robot.getPeer("mouth")
    mouth.speak("I am releasing a service")
    print("on_peer_released service change from", name)
    # remove subscriptions for newly released peers

# Service change events end ========================================


def on_sensor_data(data):
    """generalized sensor handler

    Args:
        data (_type_): _description_
    """
    print("on_sensor_data", data)



def onPredicate(predicate_event):
    robot = runtime.getService(predicate_event.src)
    robot.info("predicate " + predicate_event.name + " changed to " + predicate_event.value)
    # mouth = robot.getPeer("mouth")
    # if mouth:
    #     mouth.speak("predicate " + predicate_event.name + " changed to " + predicate_event.value)


def onSession(session_event):
    robot = runtime.getService(session_event.src)
    mouth = robot.getPeer("mouth")
    chatBot = robot.getPeer("chatBot")
    if mouth:
        mouth.speak("new session with " + session_event.user)
    # if chatBot:
    #     chatBot.setTopic("new_user")


def onMessage(msg):
    robot = runtime.getService(msg.sender)
    print("onMessage.method", msg.method)
    print("onMessage.data", msg.data)
    robot.info("onMessage.method " + msg.method)
    robot.info("onMessage.data " + str(msg.data))
    # eval(msg.method)(msg.data
    # auto invoke method
    # expand parameters ?


def on_new_user(data):
    print("on_new_user", data)
    robot = runtime.getService(data.sender)
    chatBot = robot.getPeer("chatBot")

    # TODO - some function that identifies user and reconciles identities
    # until then we'll just create a new user
    chatBot.setUser(data[0]) # name
    chatBot.setPredicate("botname", chatBot.getPredicate("human", "botname"))


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class PythonRuntime(metaclass=SingletonMeta):
    def __init__(self):
        self.registry = {}

    def register(self, name, service):
        self.registry[name] = service

    def get_service(self, name):
        return self.registry[name]


python_runtime = PythonRuntime()


def onHeartbeat(sender: str, heartbeat):
    """onHeartbeat a incremental timer used to drive
    state machines and other time based events.
    Heartbeats here do not begin until after boot.

    Args:
        sender (string): the robot's name sending the heartbeat
    """
    print("onHeartbeat", sender, heartbeat)

    robot = runtime.getService(sender)
    neoPixel = robot.getPeer("neoPixel")

    if neoPixel:
        count = heartbeat.get("count")
        if count % 2 == 0:
            # for matrix
            # neoPixel.setPixel(count % 128, 200, 23, 200)
            neoPixel.setPixel(132, 240, 23, 170)
            neoPixel.setPixel(133, 240, 100, 150)
            neoPixel.setPixel(138, 240, 23, 170)
            neoPixel.setPixel(139, 240, 100, 150)
        else:
            neoPixel.setPixel(132, 240, 100, 150)
            neoPixel.setPixel(133, 240, 23, 170)
            neoPixel.setPixel(138, 240, 100, 150)
            neoPixel.setPixel(139, 240, 23, 170)

        hash_code = hash(heartbeat.get("state"))
        hex_hash = hex(hash_code)

        # Extract the last 6 characters to ensure a 6-digit representation
        state_hash = hex_hash[-6:]
        print(state_hash)
        neoPixel.setPixel(134, state_hash)
        neoPixel.setPixel(135, state_hash)
        neoPixel.setPixel(136, state_hash)
        neoPixel.setPixel(137, state_hash)

        # neoPixel.flash("success")
    # if robot.getState() == "first_init":
    #     robot.setRandomIdle()
        neoPixel.writeMatrix()


print('loaded InMoov2.py')
