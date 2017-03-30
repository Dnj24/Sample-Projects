"""This program calculates the area of circles and triangles."""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "The calculator is now calculating!"
print "Current time: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)
hint = "Don't forget to include the correct units."

option = raw_input("Enter C for Circle or T for Triangle or S for Square: ")
opition = option.upper()

if(option == 'C'):
  radius = float(raw_input("Enter the radius: "))
  area = pi * radius ** 2
  print "The pie is baking..."
  sleep(1) 
  print ("Area: %.2f. \n%s" % (area, hint))
elif(option == 'T'):
  base = float(raw_input("Enter the base: "))
  height = float(raw_input("Enter the height: "))
  area = (0.5)*(base)*height
  print "Uni Bi Tri..."
  sleep(1)
  print("Area: %.2f. \n%s" % (area, hint))
elif(option == 'S'):
  side = float(raw_input("Enter the side: "))
  area = side**2
  print "Calculating the area..."
  sleep(1)
  print("Area: %.2f. \n%s" % (area, hint))
else:
  print "Invalid input. Program will exit!"
  
