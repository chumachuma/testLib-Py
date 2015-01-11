class MyC:
    def __init__(self, myvar):
        self.myvar = myvar
        self.classvar = 1
        
    def action (self):
        print (self.myvar)
        
    def getMyvar (self):
        return self.myvar
    
    def forceError (self):
        raise Exception