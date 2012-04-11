#thinkpython ch5 work
#bjknudson

import math

#Exercise 5.1
def check_fermat(a,b,c,n):
    if n>2:
        ab=a**n+b**n
	if ab==c**n:
	    print "Fermat was right"
	else:
	    print "that doesn't work"
    else:
	print "n is too small"


def checker():
    a=input('give a value for a\n')
    b=input('give a value for b\n')
    c=input('give a value for c\n')
    n=input('give a value for n\n')
    check_fermat(a,b,c,n)

#Exercise 5.2
def is_triangle(a,b,c):
    if a>b+c or b>a+c or c>a+b:
	print "No"
    else:
	print "Yes"

def triangle_test():
    a=input('imput stick length a\n')
    b=input('imput stick length b\n')
    c=input('imput stick length c\n')
    is_triangle(a,b,c)

Exercise 5.3

#def draw(t, length, n):
#    if n == 0:
#	return
#    angle = 50
#    fd(t, length*n)
#    lt(t, angle)
#    draw(t, length, n-1)
#    rt(t, 2*angle)
#    draw(t, length, n-1)
#    bk(t, length*n)      This uses a turtle to draw a square sprial, I'm not going to do it now because this file isn't in the right directory.