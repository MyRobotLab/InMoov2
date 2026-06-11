import random

# ----------------------------------
# SPEED CONFIG (natural + controlled)
# ----------------------------------
def speechMove():

  i01.setHandSpeed("left", 30,30,30,30,30,30)
  i01.setHandSpeed("right",30,30,30,30,30,30)

  i01.setArmSpeed("left",50,50,50,50)
  i01.setArmSpeed("right",50,50,50,50)

  i01.setHeadSpeed(50,45,50)
  i01.setTorsoSpeed(50,50,50)
# ----------------------------------
# START POSITION
# ----------------------------------
  moves = [speechMove1, speechMove2, speechMove3, speechMove4, speechMove5, speechMove6, speechMove7, speechMove8]
  choice = random.choice(moves)
  choice()

# ----------------------------------
# ARM + HEAD RAMP SYSTEM
# ----------------------------------

def rampArm(side, a, b, steps=8, delay=0.05):
    for i in range(steps):
        t = i / float(steps - 1)
        k = t * t * (3 - 2 * t)

        x = a[0] + (b[0] - a[0]) * k
        y = a[1] + (b[1] - a[1]) * k
        z = a[2] + (b[2] - a[2]) * k
        r = a[3] + (b[3] - a[3]) * k

        i01.moveArm(side, x, y, z, r)
        sleep(delay)

def rampHead(yawStart, yawEnd, pitch, steps=10, delay=0.04):
    for i in range(steps):
        t = i / float(steps - 1)
        k = t * t * (3 - 2 * t)

        yaw = yawStart + (yawEnd - yawStart) * k
        i01.moveHead(yaw, pitch, 90)
        sleep(delay)

# ----------------------------------
# ✋ HAND RAMP SYSTEM
# ----------------------------------

def rampHand(side, a, b, steps=6, delay=0.04):
    for i in range(steps):
        t = i / float(steps - 1)
        k = t * t * (3 - 2 * t)

        f1 = a[0] + (b[0] - a[0]) * k
        f2 = a[1] + (b[1] - a[1]) * k
        f3 = a[2] + (b[2] - a[2]) * k
        f4 = a[3] + (b[3] - a[3]) * k
        f5 = a[4] + (b[4] - a[4]) * k
        twist = a[5] + (b[5] - a[5]) * k

        i01.moveHand(side, f1,f2,f3,f4,f5,twist)
        sleep(delay)        




def speechMove1():
  # ----------------------------------
  # INTRODUCTION
  # ----------------------------------

  rampArm("right", [55,82,42,15], [35,72,38,15])

  # ✋ presenting gesture (soft cup)
  rampHand("right",
           [30,25,25,25,25,40],
           [70,45,40,40,35,25])

  sleep(0.4)

  rampArm("right", [35,120,48,15], [40,130,40,15])
  sleep(1)
  print('speechMove1')
  speechReset()

def speechMove2():
  # ----------------------------------
  # POINT 1
  # ----------------------------------

  rampArm("right", [60,80,40,15], [45,68,35,15])

  # ✋ pointing emphasis (not rigid)
  rampHand("right",
           [30,30,30,30,30,30],
           [160,45,150,150,150,40])

  sleep(0.8)

  rampArm("right", [45,68,35,15], [60,80,40,15])

  rampHand("right",
           [160,45,150,150,150,20],
           [30,30,30,30,30,11])

  # small expressive pulse
  rampHand("right",
           [30,30,30,30,30,11],
           [80,50,60,60,50,11], steps=4)

  rampHand("right",
           [80,50,60,60,50,11],
           [30,30,30,30,30,20], steps=4)
  sleep(1)
  print('speechMove2')
  speechReset()

def speechMove3():
  # ----------------------------------
  # POINT 2
  # ----------------------------------

  rampArm("left", [35,82,42,15], [55,70,38,15])

  # ✋ “two ideas” gesture
  rampHand("left",
           [30,30,30,30,30,130],
           [160,20,20,160,160,150])

  sleep(0.7)

  rampArm("left", [55,70,38,15], [35,82,42,15])

  rampHand("left",
           [160,20,20,160,160,150],
           [30,30,30,30,30,80])

  #rampHead(90,90,90)
  sleep(1)
  print('speechMove3')
  speechReset()

def speechMove4():
  # ----------------------------------
  # COMPARISON
  # ----------------------------------

  rampArm("left",  [55,80,40,15], [40,72,38,15])
  rampArm("right", [55,80,40,15], [45,72,38,15])

  #rampHead(90,80,90)
  rampArm("left", [50,72,38,15], [60,66,35,15])

  rampHand("left",
           [30,30,30,30,30,90],
           [70,45,50,50,45,150])

  #rampHead(80,110,90)
  rampArm("right", [60,72,38,15], [50,66,35,15])

  rampHand("right",
           [30,30,30,30,30,30],
           [70,45,50,50,45,11])

  #rampHead(110,90,90)
  sleep(1)
  print('speechMove4')
  speechReset()

def speechMove5():
  # ----------------------------------
  # EXPANSION
  # ----------------------------------

  rampArm("left",  [60,82,40,15], [52,74,38,15], steps=10)
  rampArm("right", [60,82,40,15], [52,74,38,15], steps=10)

  rampHand("left",
           [40,40,40,40,40,120],
           [15,15,15,15,15,150])

  rampHand("right",
           [40,40,40,40,40,11],
           [15,15,15,15,15,30])

  sleep(0.3)

  rampArm("left",  [42,74,38,15], [52,84,32,15], steps=10)
  rampArm("right", [42,74,38,15], [52,84,32,15], steps=10)
  sleep(1)
  print('speechMove5')
  speechReset()

def speechMove6():
  # ----------------------------------
  # EMPHASIS LOOP
  # ----------------------------------

  for _ in range(3):

      #rampHead(85,95,88,steps=6)
      rampArm("right", [50,80,40,15], [25,70,38,15], steps=6)

      rampHand("right",
               [30,30,30,30,30,11],
               [90,60,70,70,60,25], steps=4)

      #rampHead(95,85,88,steps=6)
      rampArm("left", [50,80,40,15], [25,70,38,15], steps=6)

      rampHand("left",
               [30,30,30,30,30,110],
               [90,60,70,70,60,150], steps=4)

  #rampHead(90,90,90)
  sleep(1)
  print('speechMove6')
  speechReset()

def speechMove7():
  # ----------------------------------
  # AUDIENCE SWEEP
  # ----------------------------------

  #rampHead(80,110,90,steps=14)
  #rampHead(110,90,90,steps=14)

  rampHand("left",
           [20,20,20,20,20,110],
           [10,10,10,10,10,150])

  rampHand("right",
           [20,20,20,20,20,11],
           [10,10,10,10,10,25])

  sleep(1)
  print('speechMove7')
  speechReset()

def speechMove8():
  # ----------------------------------
  # CONCLUSION
  # ----------------------------------

  rampArm("left",  [22,80,42,15], [38,76,40,15], steps=8)
  rampArm("right", [22,80,42,15], [38,76,40,15], steps=8)

  #rampHead(90,80,90,steps=10)

  rampHand("left",
           [35,35,35,35,35,110],
           [40,40,40,40,40,160])

  rampHand("right",
           [35,35,35,35,35,11],
           [40,40,40,40,40,50])

  sleep(1.0)

  # gentle return
  rampArm("left",  [38,76,30,15], [40,80,40,15], steps=10)
  rampArm("right", [38,76,30,15], [40,80,40,15], steps=10)
  print('speechMove8')
  speechReset()

def speechReset():
  i01.setHandSpeed("left", 43, 43, 43, 43, 43, 43)
  i01.setHandSpeed("right", 43, 43, 43, 43, 43, 43)
  i01.setArmSpeed("right", 31, 43, 23, 43)
  i01.setArmSpeed("left", 60, 23, 31, 31)
  i01.setHeadSpeed(43, 43)
  i01.setTorsoSpeed(31, 16, 100.0)
  #i01.moveHead(79.00,100.00,122.17,64.06,0.00,90.00)
  i01.moveArm("left",5.00,84.00,25.00,12.00)
  i01.moveArm("right",5.00,82.00,25.00,12.00)
  i01.moveHand("left",92.00,33.00,37.00,71.00,66.00,25.00)
  i01.moveHand("right",81.00,66.00,82.00,60.00,23.00,160.00)
  i01.moveTorso(95.00,90.00,90.00)
  print('speechReset')
