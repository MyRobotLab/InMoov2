#########################################
# i01_newHead_stop.py
# categories: InMoov2
# more info @: http://myrobotlab.org/service/InMoov
#########################################
# uncomment for virtual hardware
# Platform.setVirtual(True)

## stop the eyes
if runtime.isStarted('i01.head.eyeLeftUD'):
  runtime.release("i01.head.eyeLeftUD")
if runtime.isStarted('i01.head.eyeLeftLR'):
  runtime.release("i01.head.eyeLeftLR")
if runtime.isStarted('i01.head.eyeRightUD'):
  runtime.release("i01.head.eyeRightUD")
if runtime.isStarted('i01.head.eyeRightLR'):
  runtime.release("i01.head.eyeRightLR")


## stop the eyelids
if runtime.isStarted('i01.head.eyelidLeft'):
  runtime.release("i01.head.eyelidLeft")
if runtime.isStarted('i01.head.eyelidRight'):
  runtime.release("i01.head.eyelidRight")
if runtime.isStarted('i01.head.eyelidLeftUpper'):
  runtime.release("i01.head.eyelidLeftUpper")
if runtime.isStarted('i01.head.eyelidLeftLower'):
  runtime.release("i01.head.eyelidLeftLower")
if runtime.isStarted('i01.head.eyelidRightUpper'):
  runtime.release("i01.head.eyelidRightUpper")
if runtime.isStarted('i01.head.eyelidRightLower'):
  runtime.release("i01.head.eyelidRightLower")

## stop the eyebrows
if runtime.isStarted('i01.head.eyeBrowRight'):
  runtime.release("i01.head.eyeBrowRight")
if runtime.isStarted('i01.head.eyeBrowLeft'):
  runtime.release("i01.head.eyeBrowLeft")


## stop the cheeks
if runtime.isStarted('i01.head.cheekRight'):
  runtime.release("i01.head.cheekRight")
if runtime.isStarted('i01.head.cheekLeft'):
  runtime.release("i01.head.cheekLeft")


## stop the upper lip
if runtime.isStarted('i01.head.upperLip'):
  runtime.release("i01.head.upperLip")


## stop the for head
if runtime.isStarted('i01.head.forheadRight'):
  runtime.release("i01.head.forheadRight")
if runtime.isStarted('i01.head.forheadLeft'):
  runtime.release("i01.head.forheadLeft")
