#Bjknudson
#Thinkpython ch4 
#polygon.py
from TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0
print bob

def square(t,length):
    for i in range(4):
        fd(t, length)
        lt(t)


def polygon(t,length,n):
    """ Draw a polygon with turtle t, number of sides n
    and lenth of sides"""
    for i in range(n):
        fd(t, length)
        lt(t,360.0/n)

def circle(t,r):
    """Draw a circle radius r with turtle t"""
    polygon(t, 2*math.pi*r/360.0, 360)

def arc(t,r,deg):
    """Draw arc with radius r and degree deg, 
    using turtle t"""
    for i in range(360):
        fd(t,2*math.pi*r*deg/360.0/360)
	lt(t,deg/360.0)

arc(bob,r= 100,deg=270)

wait_for_user()