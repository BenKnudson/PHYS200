#thinkpython ch7 exercise 4
#bjknudson
# 7.4  eval loop function

def eval_loop():
    while True:
	string=raw_input('> ')
	if string== 'done':
	    print "Done."
	    break
	result=eval(string)
	print result

eval_loop()