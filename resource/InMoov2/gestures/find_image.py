def find_image(image):
#  print('please implement by using a image search service')
#  RetourServer=Parse("http://www.myai.cloud/version.html")
  try:
    image = image.decode( "utf8" )
  except: 
    pass
  a = Parse("https://www.google.com/search?tbm=isch&q="+urllib2.quote(image).replace(" ", "%20"))
  
  i01.displayFullScreen(a)
  print "https://www.google.com/search?tbm=isch&q="+urllib2.quote(image).replace(" ", "%20")
#Light(1,1,1)
