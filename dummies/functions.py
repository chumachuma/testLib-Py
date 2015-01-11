def menu (parameter):
	if parameter == 0:
		raise Exception
	elif parameter == 1:
		return parameter
	elif parameter == 2:
		print (parameter)
		return parameter
	else:
		print (parameter)
	
def forceError ():
	raise Exception
		
		
def action ():
	print ("this is an action")

def action1 (parameter1):
	print ("action with 1 parameter: ", parameter1)
	
def action2 (parameter1, parameter2):
	print ("action with 2 parameters: ", parameter1, parameter2)

def actionN (*args):
	n = args.__len__()
	plural = "" if n == 1 else "s" 
	print ("action with %i parameter%s" % (n, plural), args)
	

def identity ():
	return 1
	
def identity1 (parameter1):
	return parameter1

def identity2 (parameter1, parameter2):
	return (parameter1, parameter2)
	
def identityN (*args):
	return (args)
	
	
def function ():
	print(0)
	return 0
	
def function1 (parameter1):
	print (parameter1)
	return parameter1

def function2 (parameter1, parameter2):
	print (parameter1, parameter2)
	return (parameter1, parameter2)
	
def functionN (*args):
	print (args)
	return (args)