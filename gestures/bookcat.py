def bookcat():
  sleep(3)
  i01_chatBot.getResponse("SAY " + "Tell me read the book or stop reading")
  #chatBot.getResponse("SAY " + "Скажите мне, прочитайте книгу или перестаньте читать")
  sleep(3)
  i01.finishedGesture() 

def bookcatYes():
  print "book cat yes"
  sleep(2)
  i01.speakBlocking("Tell me. turn the page, when you want me to read the next page, or say. stop reading")
  # #i01.speakBlocking(u"Скажите мне. Повернуть страницу, когда вы хотите, чтобы я прочитал следующую страницу или скажите. Прекратить чтение")
  i01.moveHead(20,90,30)
  sleep(2)
  i01.moveHead(90,90,90)
  i01.finishedGesture()

def bookcatNo():
  print "book cat no"
  sleep(2)
  i01.speakBlocking("too bad, I like this book")
  # #i01.speakBlocking(u"Слишком плохо, мне нравится эта книга")
  i01.moveHead(120,90,30)
  sleep(2)
  i01.moveHead(90,90,90)
  i01.finishedGesture()

def turnthepage(): 
  global iReadbookcat
  if iReadbookcat <= 0:
    sleep(3)
    i01.speakBlocking("Cat the cat, who is that?")
	# #i01.speakBlocking(u"Кошка кошка, кто это?")
    iReadbookcat += 1
  elif iReadbookcat == 1:
    sleep(3)
    i01.speakBlocking("It's mouse, the mouse! Hi, mouse the mouse!  Hello there")
	# #i01.speakBlocking(u"Это мышь, мышь! Привет, мышь мышь! Привет")
    iReadbookcat += 1
  elif iReadbookcat == 2:
    sleep(3)
    i01.speakBlocking("Cat the cat, who is that?")
	# #i01.speakBlocking(u"Кошка кошка, кто это?")
    iReadbookcat += 1
  elif iReadbookcat == 3:
    sleep(3)
    i01.speakBlocking("It's duck the duck! Hi, duck the duck! A pleasure, as always")
    # #i01.speakBlocking(u"Это утка утка! Привет, утка утка! Удовольствие, как всегда")
    iReadbookcat += 1
  elif iReadbookcat == 4:
    sleep(3)
    i01.speakBlocking("Cat the cat, who is that?")
	# #i01.speakBlocking(u"Кошка кошка, кто это?")
    iReadbookcat += 1
  elif iReadbookcat == 5:
    sleep(3)
    i01.speakBlocking("It's fish the fish! Hi, fish the fish! Hey dude")
	# #i01.speakBlocking(u"Это рыба рыба! Привет, рыба рыба! Привет чувак")
    iReadbookcat += 1
  elif iReadbookcat == 6:
    sleep(3)
    i01.speakBlocking("Cat the cat likes her friends. Sure do")
	# #i01.speakBlocking(u"Кошка кошка любит своих друзей. Конечно да")
    iReadbookcat += 1
  elif iReadbookcat == 7:
    sleep(3)
    i01.speakBlocking("Cat the cat, who is that?  eep")
	# #i01.speakBlocking(u"Кошка кошка, кто это? Ой")
    iReadbookcat += 1
  elif iReadbookcat == 8:
    sleep(3)
    i01.speakBlocking("I have no idea.  blarggie! blarggie")
	# #i01.speakBlocking(u"Понятия не имею.Бларги! Бларги!")
    iReadbookcat += 1
  elif iReadbookcat == 9:
    sleep(3)
    i01.speakBlocking("Maybe")
	# #i01.speakBlocking(u"Может быть")
    iReadbookcat += 1
  elif iReadbookcat == 10:
    sleep(3)
    i01.speakBlocking("Blarggie! Blarggie!  It's a new friend! Blarggie! Blarggie")
	# #i01.speakBlocking(u"Бларги! Бларги! Это новый друг! Бларги! Бларги!")
    iReadbookcat += 1
  elif iReadbookcat == 11:
    sleep(3)
    i01.speakBlocking("The end")
	# #i01.speakBlocking(u"Конец")
    iReadbookcat += 1
  elif iReadbookcat == 12:
    sleep(3)
    i01.speakBlocking("The end")
	# #i01.speakBlocking(u"Конец")
    iReadbookcat += 1
  i01.finishedGesture()  
