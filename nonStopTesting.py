"""nonStopTesting.py
This module adds two decorators to have non-stop error handling when and exception is raised
"""

import testLib.GLOBALS as GLOBALS
import testLib.prettyArguments
import testLib.testErrors

parseArguments = testLib.prettyArguments.parseArguments
SilencedError = testLib.testErrors.SilencedError


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
		arguments = parseArguments(*args, **kwargs)
		return SilencedError(catchedException, self.function.__name__ + arguments)
	
	
def testClass (myClass):
	"""Pass testing decorator to all the methods in a class"""
	class NewClass (myClass):
		
		def __init__ (self, *args, **kwargs):
			myClass.__init__(self, *args, **kwargs)
			self.__setMethodsToTestMode()
			
		def __setMethodsToTestMode (self):		
			for name in dir(myClass):
				method = getattr(myClass, name)
				if hasattr(method, "__call__") and name[0] != "_":
					new_method = testFunction(method, self)
					setattr(self, name, new_method)
					
	return NewClass