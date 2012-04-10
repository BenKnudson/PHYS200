#thinkpython ch5 work
#bjknudson

import math

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

checker()