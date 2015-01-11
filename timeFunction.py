import time

class timeFunction:
	"Decorator to calculate the time it takes to execute a function"
	def __init__ (self, function):
		self.function = function
	
	def __call__ (self, *args, **kwargs):
		initial_time = time.time()
		self.function(*args, **kwargs)
		final_time = time.time()
		return final_time-initial_time
	
	def __get__(self, instance, owner=None):
		if instance:
			method = self.function.__get__(instance, owner)
			return self.__class__(method)