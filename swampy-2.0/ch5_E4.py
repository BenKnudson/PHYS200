#Thinkpython ch5 exercise 5.4
#bjknudson
#

from TurtleWorld import *
world=TurtleWorld()
bob=Turtle()
print bob
bob.delay=0

def koch(t,x):
    if x<3:
        fd(t,x)
        return
    koch(t,x/3.0)
    lt(t,60)
    koch(t,x/3.0)
    rt(t,120)
    koch(t,x/3.0)
    lt(t,60)
    koch(t,x/3.0)

def snowflake(t,x,n):
    for i in range(n):
	koch(t,x)
	rt(t,360.0/n)

    
snowflake(bob,100,5)

wait_for_user()