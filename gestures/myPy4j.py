def myPy4j():
  import os
  import codecs
  py4j = runtime.getService('i01.py4j')
  ## Here we set the path to the desired script to be run by the py4j service
  script = 'data/Py4j/i01.py4j/py4jTest.py'
  if os.path.isfile(script):
      f = codecs.open(script, 'r', 'utf-8')
      try:
          code = f.read()
      finally:
          f.close()
      py4j.exec(code)
  else:
      print "Script not found:", script
    
