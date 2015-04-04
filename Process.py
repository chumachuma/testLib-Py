import testLib.GLOBALS as GLOBALS

class Process:
    def __init__ (self):
        self.processTitle = ""
        self.processDescription = ""
        self.processResults = ""
        self.processSummary = ""
        self.log = GLOBALS.TESTLOG
    
    def preprocess (self):
        pass # To be implemented in process class
    
    def process (self):
        pass # To be implemented in process class
    
    def postprocess (self):
        pass # To be implemented in process class
    
    def preprocessing (self):
        pass # To be implemented in each test case
    
    def processing (self):
        pass # To be implemented in each test case
    
    def postprocessing (self):
        pass # To be implemented in each test case
    
    def run (self):
        self.preprocess()
        self.process()
        self.postprocess()
        
    def TITLE (self, title):
        self.processTitle = title
    
    def DESCRIPTION (self, description):
        self.processDescription += description
        
    def RESULT (self, result):
        self.processResults = result
    
    def COMMENT (self, comment):
    	self.log.buffer(comment)
    
    def SUMMARY (self, summary):
        self.processSummary = summary
        