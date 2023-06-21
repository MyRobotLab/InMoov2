def eyeslooking():
  for y in range(0, 5):
    if runtime.isStarted(('i01_eyeX') and ('i01_eyeY')):
      stopit()
    x = (random.randint(1, 6))
    if x == 1:
      i01_head_eyeX.moveTo(80)
    if x == 2:
      i01_head_eyeY.moveTo(80)
    if x == 3:
      eyesdown()
    if x == 4:
      eyesup()
    if x == 5:
      eyesleft()
    if x == 6:
      eyesright()
    sleep(0.5)
  eyesfront()
  i01.finishedGesture()
