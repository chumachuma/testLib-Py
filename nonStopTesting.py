"""nonStopTesting.py
This module adds two decorators to have non-stop error handling when and exception is raised
"""

import inspect
import functools
import testLib.GLOBALS as GLOBALS

getmembers = inspect.getmembers

class testFunction:
	"""Test function decorator"""
	def __init__ (self, function, *fixedArgs):
		self.function = function
		self.fixedArgs = fixedArgs
		
	def __call__ (self, *args, **kwargs):
		"""Callable class"""
		try:
			return self.function(*(self.fixedArgs + args), **kwargs)
		except Exception as catchedException:
			errorLog = self.getErrorLog(catchedException, *args, **kwargs)
			GLOBALS.TESTLOG.write(errorLog)
			return errorLog
		
	def __get__ (self, instance, owner=None):
		"""Support instance methods"""
		if instance and owner:
			self.fixedArgs = (owner,) + self.fixedArgs
			return self
		
	def __repr__ (self):
		"""Return the function's docstring."""
		return self.function.__doc__
			
	def getErrorLog (self, catchedException, *args, **kwargs):
		"""The decorator displays how is the function called and the exception raised"""
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
	class NewClass (myClass):
		
		def __init__ (self, *args, **kwargs):
			myClass.__init__(self, *args, **kwargs)
			self.__setMethodsToTestMode()
			
		def __setMethodsToTestMode (self):		
			for name, method in getmembers(myClass):
				if hasattr(method, "__call__") and name[0] != "_":
					new_method = testFunction(method, self)
					setattr(self, name, new_method)
					
	return NewClass