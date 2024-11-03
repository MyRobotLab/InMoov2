# IMPORTANT - Jython could call overloaded methods, Py4j cannot !!!
# names are guaranteed to be unique
# the kluge of changing period to underscore
# auto create globals ? (bad idea)
# isolate to callbacks
# from py4j.java_gateway import JavaObject

# RELOAD SCRIPT
# python.execFile('src/main/resources/resource/InMoov2/InMoov2.py')
# with open('src/main/resources/resource/InMoov2/InMoov2.py', 'r') as file:
#     script_code = file.read()
# exec(script_code)


# FOR SUBSCRIPTIONS WHOS DESTINATION IS PYTHON
# SHOULD PROBABLY BE MAINTAINED HERE
from __future__ import print_function 
from __future__ import division
from __future__ import unicode_literals 

import sys
import os
import json
import time
import threading
from datetime import datetime

import time
import random
import urllib
import io
import itertools
import textwrap
import codecs
import socket
import shutil
import hashlib
import csv
import glob
import inspect

# Check Python version and import appropriate module
if sys.version_info[0] == 2:
    import thread
else:
    import _thread as thread


# from java.lang import String
# from org.myrobotlab.net import BareBonesBrowserLaunch
# from org.myrobotlab.arduino.Msg import MRLCOMM_VERSION
# import org.myrobotlab.framework.Platform as Platform
# import org.myrobotlab.service.Runtime as Runtime

def printx(format_string, *args):
    import datetime
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    formatted_message = format_string % args  # Using old % formatting suitable for Python 2.7
    print("%s: %s" % (current_time, formatted_message))



def onPythonMessage(msg):
    """Initial processing and routing for all messages.
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
    # print("onPythonMessage", msg)
    try:
        if not isinstance(msg, dict):
            # From Jython msg is a java object
            # py4j is a dict because it gets decoded from json
            # normalizing format
            from org.myrobotlab.codec import CodecUtils

            msg_json = CodecUtils.toJson(msg)
            msg = json.loads(msg_json)

        method_name = msg.get("method")
        name = msg.get("sender")
        params_array = msg.get("data")

        if not params_array:
            params_array = []

        # first parameter will always be InMoov2 name
        params_array.insert(0, name)

        # filter out chatty heartbeat and peak
        if method_name != "onHeartbeat" and method_name != "onPeak":
            printx("%s", method_name)

        # Check if the method exists in the global namespace
        if method_name in globals() and callable(globals()[method_name]):
            cmd = "result = {}(*params_array)".format(method_name)
            # filter out chatty heartbeat
            # if method_name != "onHeartbeat" and method_name != "onPeak":
            #     print("onPythonMessage cmd {}".format(cmd))

            # Execute the code with the globals parameter
            exec_globals = globals()
            exec_globals["params_array"] = params_array
            exec(cmd, exec_globals)

            # Access the result from the executed code
            # result = exec_globals['result']
            # print("Result:", result)  # Output the result (you can modify this as needed)
        else:
            print("method {} not found or not callable.".format(method_name))

    except Exception as e:
        print(e)

def onAudioStart(name, data):
    """onAudioStart is a callback for when audioPlayer starts
    it is rebroadcasted from InMoov2 AudioFile service.
    """
    print("onAudioStart", name, data)
    robot = runtime.getService(name)
    ear = robot.getPeer("ear")
    if ear:
        ear.stopListening()

def onAudioEnd(name, data):
    """onAudioEnd is a callback for when audioPlayer stops
    it is rebroadcasted from InMoov2 AudioFile service.
    """
    print("onAudioEnd", name, data)
    robot = runtime.getService(name)
    ear = robot.getPeer("ear")
    if ear:
        ear.startListening()        


def onStartSpeaking(name, text):
    print("onStartSpeaking", text)

    global runtime

    # print("onStartSpeaking", text)

    # FIXME FIXME FIXME name delivered as a parameter or
    # make class that is created by the runtime with name
    robot = runtime.getService(name)

    # i01_neoPixel = i01.getPeer("neoPixel")
    # if i01_neoPixel and i01.getConfig().neoPixelFlashWhenSpeaking:
    # i01_neoPixel.setAnimation("Ironman", 255, 255, 255, 20)

    # Great idea, but has hardcoded translations - this should be done in the language service but the
    # raw gesture still be processed
    # if 'oui ' in text or 'yes ' in text or ' oui' in text or 'ja ' in text or text=="yes" or text=="kyllä":Yes()
    # if 'non ' in text or 'no ' in text or 'nicht ' in text or 'neen ' in text or text=="no" or text=="ei":No()

    # force random move while speaking, to avoid conflict with random life gesture
    if robot.getConfig().robotCanMoveHeadWhileSpeaking:
        robot.enableRandomHead()


def onEndSpeaking(name, text):
    print("onEndSpeaking", text)
    robot = runtime.getService(name)
    robot.disableRandom()

    # random = robot.getPeer("random")
    # if random and robot.getState() != "tracking":
    #     # random.disable("i01.setHeadSpeed")
    #     # random.disable("i01.moveHead")
    #     random.disable()

    # if i01:
    #     if i01.getConfig().robotCanMoveHeadWhileSpeaking:
    #         random = runtime.getService("i01.random")
    #         if random:
    #             random.disable()
    #             random.enable('i01.moveLeftArm')
    #             random.enable('i01.moveRightArm')
    #             random.enable('i01.moveLeftHand')
    #             random.enable('i01.moveRightHand')
    #             random.enable('i01.moveTorso')
    #             random.enable('i01.setLeftArmSpeed')
    #             random.enable('i01.setRightArmSpeed')
    #             random.enable('i01.setLeftHandSpeed')
    #             random.enable('i01.setRightHandSpeed')
    #             random.enable('i01.setTorsoSpeed')
    #             if runtime.isStarted('i01.head'):
    #                 random.addRandom(200, 1000, "i01", "setHeadSpeed", 8.0, 20.0, 8.0, 20.0, 8.0, 20.0)
    #                 random.addRandom(200, 1000, "i01", "moveHead", 70.0, 110.0, 65.0, 115.0, 70.0, 110.0)
    #         i01_neoPixel = runtime.getService('i01.neoPixel')
    #         if i01.getConfig().neoPixelFlashWhenSpeaking and runtime.isStarted("i01.neoPixel"):
    #             i01_neoPixel.clear()


# Sensor events begin ========================================

def onPirOn(name):
    current_time = datetime.now().strftime("%H:%M:%S")
    print('onPirOn("{}") at {}'.format(name, current_time))
    robot = runtime.getService(name)
    if robot:
        robot.setPredicate(name + ".pir", True)

        # sleeping
        if "sleep" == robot.getState():
            robot.fire("wake")

        # FIXME - chatBot.getResponse("SYSTEM_EVENT onPirOn")
        # robot.speak("I feel your presence")

        # FIXME - "remove" this is custom
        neoPixel = robot.getPeer("neoPixel")
        if neoPixel:
            neoPixel.setPixel(130, 120, 200, 150)
            neoPixel.setPixel(131, 120, 200, 170)
            neoPixel.setPixel(140, 120, 200, 150)
            neoPixel.setPixel(141, 120, 200, 170)
            neoPixel.writeMatrix()


def onPirOff(name):
    current_time = datetime.now().strftime("%H:%M:%S")
    print('onPirOff("{}") at {}'.format(name, current_time))
    robot = runtime.getService(name)
    robot.setPredicate(name + ".pir", False)
    # FIXME - chatBot.getResponse("SYSTEM_EVENT onPirOff")
    # robot.speak("I'm so alone")
    # FIXME - "remove" this is custom
    neoPixel = robot.getPeer("neoPixel")
    if neoPixel:
        neoPixel.setPixel(130, 0, 0, 0)
        neoPixel.setPixel(131, 0, 0, 0)
        neoPixel.setPixel(140, 0, 0, 0)
        neoPixel.setPixel(141, 0, 0, 0)
        neoPixel.writeMatrix()


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
    print("onTopic", topic_event.topic)
    # FIXME - find a solution for the hardcoded name !
    # route through inmoov add name as field
    robot = runtime.getService(topic_event.src)
    mouth = robot.getPeer("mouth")
    if mouth:
        # mouth.speak("New topic, the topic is " + topic_event.topic)
        pass


# Topic events end ==========================================
# State change events begin ========================================


def onStateChange(name, state_event):
    """The main router for state changes
    it calls the appropriate method based on the state change
    Hooked to InMoov2.publishStateChange

    Args:
        data (InMoov2State): contains src and state
    """
    print("onStateChange {} {}".format(name, state_event))

    # Python 2 unicode pain
    state = str(state_event.get("state"))
    robot = runtime.getService(name)

    # leaving state changes
    fsm = robot.getPeer("fsm")
    mouth = robot.getPeer("mouth")
    chatBot = robot.getPeer("chatBot")

    if fsm:
        leavingState = fsm.getPreviousState()

    # A way to hook transitions from one state to another
    if leavingState == "random":
        robot.disableRandom()

    if chatBot:
        chatBot.setPredicate("state", state)

    # FIXME - chatBot.getResponse("SYSTEM_EVENT on_start")
    if mouth:
        # mouth.speak("leaving " + leavingState + " state and entering " + state)
        pass

    # call the new state handler
    eval("on_" + state + "('" + name + "')")

# =============  STATE CHANGE EVENTS BEGIN ========================
def on_wake(name):
    """
    State: wake
    Waking from slumber, sensors begin to flow in data and the robot
    should try to identify where it is and switch their attention to
    the person of focus.

    Args:
        name (string): name of InMoov2 robot

    TODO - remove all non boot fire() calls from java - all fire() calls should be in python
    Who am I - getPredicate botname
    Where am I - sensors, opencv, slam, gps, etc, time i've been a sleep
    When am I - time since last wake
    How do I feel - battery, errors, etc
    What senses do I have - what is around me
    What is around me
    Who is around me - face recognition, voice recognition, etc
    What date is it
    What time is it
    How long have I been asleep

    if person -- greet, query who they are, etc

    What should I do based on the above information

    """
    # check time good morning, evening, etc
    # use topic or not ?
    # ON_WAKE_GREETING
    # TODO - most common function getResponse getPredicate setPredicate

    print("on_wake", name)

    robot = runtime.getService(name)
    robot.setHeadSpeed(45, 45, 45)
    robot.moveHead(90, 90, 90)
    chatbot = robot.getPeer("chatBot")
    fsm = robot.getPeer("fsm")
#    chatbot.getResponse("STATE_WAKE_BEGIN")

    # sets predicates with system data
    robot.systemCheck()
#    chatbot.getResponse("SYSTEM_REPORT")

    # check if lastUsername is set - ie single default session
    # check if setup has been done or dismissed
    # determine the last person who was using the robot

    # state_on_setup
    # lastUsername = robot.getPredicate("human", "state_on_setup_name")
    # print("lastUsername", lastUsername)
    lastUsername = robot.getPredicate("human", "lastUsername")

    # report status, errors, battery, etc
    # e.g. I'm afraid I have errors, would you like me to show you ?

    # set session
    print("startSession", lastUsername)
    chatbot.startSession(lastUsername)

    # get text response
#    chatbot.getResponse("STATE_WAKE_END")

    setup = chatbot.getPredicate("human", "setup")

    if setup == "unknown" or setup == "human" or setup == "started":
        # try to identify user go through SETUP
        # fsm.fire("setup") - FIXME - disabled until ready for new setup
        fsm.fire("idle")
    else:
        # if user is known - go through WAKE_UP
        fsm.fire("idle")


def on_setup(name):
    """Purpose of this state is to identify the user
    and first initial configuration of the robot.

    The user should be asked to identify themselves.

    Various other information could be gathered as well
    although the user should be able to leave at any time.

    Coming back to this state should be possible at any time.

    Args:
        name (string): name of InMoov2 robot
    """
    print("on_setup", name)
    robot = runtime.getService(name)
    chatbot = robot.getPeer("chatBot")
    chatbot.getResponse("STATE_SETUP_INTRODUCTION")
#    chatbot.getResponse("STATE_SETUP_BEGIN")

    # if resuming a pause
    # chatbot.getResponse("STATE_SETUP_RESUME")
    # YES, NO, LATER  (YES & NO are finalizing)

    # do anything else desired
    # generate picture data of the user
    # go through personal questionare
    # setup hardware


def on_idle(name):
    print("on_idle", name)
    robot = runtime.getService(name)
    mouth = robot.getPeer("mouth")
    if mouth:
        # mouth.speak("I am idle")
        pass
    print("on_idle state change from", name)


def on_telepresence(name):
    print("on_telepresence", name)


def on_random(name):
    print("on_random", name)
    robot = runtime.getService(name)
#    robot.getRespone("RANDOM")
    random = robot.getPeer("random")
    if random:
        random.enable()


def on_sleep(name):
    print("on_sleep", name)
    robot = runtime.getService(name)
#    robot.getResponse("STATE_SLEEP")
    robot.disableRandom()
    # center and tilt head down
    robot.setHeadSpeed(5, 5, 5)
    robot.moveHead(10, 90, 90)


def on_power_down(name):
    print("on_power_down", name)

# =============  STATE CHANGE EVENTS END ========================

# Service change events begin ========================================


def on_peer_started(name):
    print("on_peer_started", name)
    robot = runtime.getService(name)
    mouth = robot.getPeer("mouth")
    # mouth.speak("I am starting a new service")
    print("on_peer_started service change from", name)
    # add subscriptions for newly started peers


def on_peer_released(name):
    print("on_peer_released", name)
    robot = runtime.getService(name)
    mouth = robot.getPeer("mouth")
    # mouth.speak("I am releasing a service")
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
    print("onPredicate", predicate_event)
    robot = runtime.getService(predicate_event.src)
    robot.info(
        "predicate " + predicate_event.name + " changed to " + predicate_event.value
    )
    # mouth = robot.getPeer("mouth")
    # if mouth:
    #     mouth.speak("predicate " + predicate_event.name + " changed to " + predicate_event.value)


def onSession(session_event):
    """
    Args:
        session_event (_type_): _description_
    """
    print("onSession", session_event)
    robot = runtime.getService(session_event.src)
    mouth = robot.getPeer("mouth")
    chatBot = robot.getPeer("chatBot")
    if mouth:
        pass
        # mouth.speak("new session with " + session_event.user)
    # if chatBot:
    #     chatBot.setTopic("new_user")



def on_new_user(data):
    print("on_new_user", data)
    robot = runtime.getService(data.sender)
    chatBot = robot.getPeer("chatBot")

    # TODO - some function that identifies user and reconciles identities
    # until then we'll just create a new user
    chatBot.setUser(data[0])  # name
    chatBot.setPredicate("botname", chatBot.getPredicate("human", "botname"))


def onClassification(name, classification):
    print("onClassification {} {}".format(name, classification))
    # get response hello classification.label if confidence > x


def onHeartbeat(name, heartbeat):
    """onHeartbeat a incremental timer used to drive
    state machines and other time based events.
    Heartbeats here do not begin until after boot.

    Args:
        name (string): the robot's name sending the heartbeat
    """
    # print("onHeartbeat {} {}".format(name, heartbeat))

    robot = runtime.getService(name)
    state = robot.getState()
    neoPixel = robot.getPeer("neoPixel")
    # errors = heartbeat.get("errors")
    count = heartbeat.get("count")

    if robot.getState() == "idle":
        current_time = int(time.time() * 1000)
        time_in_idle = current_time - int(robot.getPredicate("idle.start"))
        # FIXME - this should be a configurable value 15 minutes
        # print("time_in_idle", time_in_idle)
        # FIXME - configurable value
        if time_in_idle > 900000:
            robot.fire("sleep")

    # print("onHeartbeat", name, state, count)

    # FIXME - this needs to be removed
    if neoPixel:
        # This is Grog's neopixel matrix - it needs to be removed
        if count % 2 == 0:
            # heartbeat tick
            neoPixel.setPixel(132, 240, 23, 170)
            neoPixel.setPixel(133, 240, 100, 150)
            neoPixel.setPixel(138, 240, 23, 170)
            neoPixel.setPixel(139, 240, 100, 150)
        else:
            # heartbeat tock
            neoPixel.setPixel(132, 240, 100, 150)
            neoPixel.setPixel(133, 240, 23, 170)
            neoPixel.setPixel(138, 240, 100, 150)
            neoPixel.setPixel(139, 240, 23, 170)

        # if len(errors):
        #     for i in range(0, len(errors)):
        #         neoPixel.setPixel(118 + i, 240, 0, 0)

        hash_code = hash(state)
        hex_hash = hex(hash_code)

        # Extract the last 6 characters to ensure a 6-digit representation
        state_hash = hex_hash[-6:]
        # print(state, state_hash)
        neoPixel.setPixel(134, state_hash)
        neoPixel.setPixel(135, state_hash)
        neoPixel.setPixel(136, state_hash)
        neoPixel.setPixel(137, state_hash)

        neoPixel.writeMatrix()


def onPeak(name, volume):
    # print("onPeak", name, volume)
    robot = runtime.getService(name)

    # FIXME - remove this custom
    neoMouth = runtime.getService("neoMouth")
    if neoMouth:
        neoMouth.fill(0, 183, 93)
        neoMouth.setBrightness(10 * int(volume)) 
#        neoMouth.flash("speaking")
        # neoMouth.clear()
        # neoMouth.fill(0, 183, 93)
        # neoMouth.clear()


print("loaded InMoov2.py")
