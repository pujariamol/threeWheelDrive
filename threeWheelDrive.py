import pygame 

pygame.init()

while 1:
 # print pygame.event.get() 
  for event in pygame.event.get():
    print event.type
    if event.type == pygame.KEYDOWN:
      print "KEYDOWNN"
      print event.key
    if event.type == pygame.KEYUP:
      print "KEYUP"
      print event.key
