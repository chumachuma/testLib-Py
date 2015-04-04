import testLib.GLOBALS as GLOBALS

class ExpectedError (Exception):
    def __init__ (self):
        self.__trackError()
        
    
    def __trackError (self):
        GLOBALS.ERROR_COUNT += 1
        self.trackedError = "!Error  " + str(GLOBALS.ERROR_COUNT).zfill(5) + "!"
    
    def expectError (self):
        if self.__isCalledConsequently():
            GLOBALS.ERROR_COUNT -= 1
            self.trackedError = "!Known Error!"
    
    def __isCalledConsequently (self):
        "Forward, back, then hack"
        return str(GLOBALS.ERROR_COUNT).zfill(5) == self.trackedError[8:-1]
        
        
class SilencedError (ExpectedError):

    def __init__ (self, catchedException, called):
        self.catchedException = catchedException
        self.called = called
        ExpectedError.__init__(self)
        
    def getErrorLog (self):
        return self.trackedError + "\tCalled: " + self.called +"\n"+ repr(self.catchedException)        
        
    def __eq__ (self, other):
        try:
            return self.trackedError == other.trackedError
        except:
            return False
        
    def __repr__ (self):
        return (self.trackedError, self.called, str(self.catchedException))
        
    def __str__ (self):
        return self.getErrorLog()