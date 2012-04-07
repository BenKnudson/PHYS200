#Bjknudson
#ThinkPython ch 4
#4.2
from TurtleWorld import *
import math

World = TurtleWorld()
bob=Turtle()
bob.delay = 0
print bob

def arc(t,r,deg,length):
    """Draw an arc radius r and degree d with turtle t"""
    #length was calculated in flower 
    #so it only had to do it once
    n=360
    turn=deg/360.0
    for i in range(n):
	fd(t,length)
	lt(t,turn)


def flower(t,p,l):
    """draw a flower with p petals with length l
    using turtle t
    only works for odd p"""
    deg=360.0/p
    n=p
    r=l/(2*(1-math.cos(deg*math.pi/180/2)))
    turn=180-180.0/p
    length=2*math.pi*r*deg/360.0/360
    for i in range(n):
        arc(t,r,deg,length)  
        lt(t,turn)


flower(bob, p=8, l=50)

wait_for_user()  