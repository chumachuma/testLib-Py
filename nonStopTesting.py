"""nonStopTesting.py
This module adds wrappers to have non-stop error handling
"""

import testLib.GLOBALS as GLOBALS

class testFunction:
	"""Test function decorator"""
	def __init__ (self, function):
		self.function = function
		
	def __call__ (self, *args, **kwargs):
		try:
			return self.function(*args, **kwargs)
		except Exception as catchedException:
			errorLog = self.getErrorLog(catchedException, *args, **kwargs)
			GLOBALS.TESTLOG.write(errorLog)
			return errorLog
			
	def getErrorLog (self, catchedException, *args, **kwargs):
		"""The decorator displays how is the function called and the exception"""
		track_error = self.trackError()
		arguments = self.parseArguments(*args, **kwargs)
		return track_error + "\tCalled: " + self.function.__name__ + arguments +"\n"+ repr(catchedException)
	
	def trackError(self):
		GLOBALS.ERROR_COUNT += 1
		return "!Error  " + str(GLOBALS.ERROR_COUNT).zfill(5) + "!"

	def parseArguments(self, *args, **kwargs):
		"""Pretty display of arguments"""
		return "("+ self.parseArgs(*args) + self.splitArgsKwargs(*args, **kwargs) + self.parseKwargs(**kwargs) +")"
	
	def parseArgs (self, *args):
		args_str = ""
		for value in args:
			args_str += repr(value) + ", "
		return args_str[:-2]
	
	def splitArgsKwargs (self, *args, **kwargs):
		spliter_str = ""
		if args and kwargs:
			spliter_str = ", "
		return spliter_str
	
	def parseKwargs (self, **kwargs):
		kwargs_str=""
		for name, value in kwargs.items():
			kwargs_str += name + "=" + repr(value) + ", "
		return kwargs_str[:-2]

def testClass (myClass):
	"""Pass testing decorator to all the methods in a class"""
	for name, methods in getmembers(myClass):
		if hasattr(methods, "__call__"):
		#if isinstance(methods, FunctionType):
			#types.UnboundMethodType(python 2) 
			#types.FunctionType(python 3)
			#types.MethodType?
			#print (name)
			setattr(myClass, name, testing(methods))