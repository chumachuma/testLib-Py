"""logInterface.py
Interface to print into terminal and write to files
"""

class LogInterface:
	def __init__(self):
		self.bufferData = ""
		self.defaults()
	
	def defaults (self):
		self.logFilename = "log.txt"
		self.logPath = "."
		self.DS = "\\" # Running on windows ("/" for linux)
		self.bufferSize = 640 # 5MB
		self.outputModes = {
			"PRINT": True, 
			"WRITE": False}
		self.show = self.printToTerminal
	
	def setMyLog (self):
		output_functions = []
		if self.outputModes["PRINT"]:
			output_functions.append(self.printToTerminal)
		if self.outputModes["WRITE"]:
			output_functions.append(self.writeToFile)
		self.show = self.__joinActions(*output_functions)
	
	
	def __joinActions(self, *args):
		def joined ():
			for function in args:
				function()
		return joined
		
	def buffer (self, new_data):
		self.bufferData += "\n" + new_data
		self.__bufferAutomation()
	
	def __bufferAutomation (self):
		if self.isBufferFull():
			self.executeBuffer()
	
	def isBufferFull (self):
		return self.bufferData.__len__() > self.bufferSize
		
	def executeBuffer (self):
		self.show()
		self.clearBuffer()
	
	def clearBuffer (self):
		self.bufferData = ""
		
	def printToTerminal (self):
		if self.bufferData:
			print (self.bufferData[1:])
		
	def clearFile (self):
		open(self.logPath+self.DS+self.logFilename, 'w').close()	
	
	def writeToFile (self):
		if self.bufferData:
			with open (self.logPath+self.DS+self.logFilename, "a") as file:  
				file.write(self.bufferData[1:] + "\n")
			
	def __del__ (self):
		self.executeBuffer()
	
	### API ###
	
	def write (self, new_data):
		self.buffer(new_data)
		if self.bufferData:
			self.executeBuffer()