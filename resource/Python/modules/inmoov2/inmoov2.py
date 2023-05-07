
class InMoov2(object):
    """Library to support myrobotlab in Python
    Intended to be used with Jython or Py4j.
    This will be a singleton class.

    """

    def __init__(self):
        self.name = "InMoov2"
        self.version = "1.0"
        self.license = "Apache License 2.0"
        self.robots = {}
        # TODO initialize any singleton state variables here

    def start(self, name="i01"):
        self.robots[name] = {
            "name": name,
        }
        return self.robots[name]
    
_myrobotlab = InMoov2()
start = _myrobotlab.start