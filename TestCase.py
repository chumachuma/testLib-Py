import tools.Process as prInterface
import testLib.nonStopTesting as testDeco
import testLib.prettyArguments

testFunction = testDeco.testFunction
testClass = testDeco.testClass
parseArguments = testLib.prettyArguments.parseArguments

Process = prInterface.Process

class TestCase (Process):
    def __init__ (self):
        Process.__init__(self)
        self.processing = self.testprocessing
        self.process = self.testprocess
        self.listFunctions = []
        self.dicTestFunctions = {}
        self.listClasses = []
        self.dicTestClasses = {}
        self.activeClass = None
        self.activeFunction = None
        self.activeFunctionName = ""
        
    def preprocess (self):
        self.preprocessing()
        self. log.buffer(self.processTitle)
        self.log.buffer(self.processDescription)
        self.prepareTestFunctions()
        self.prepareTestClasses()
        
    def prepareTestFunctions (self):
        for funtion in self.listFunctions:
            self.dicTestFunctions[function.__name__] = testFunction(funtion)
            
    def prepareTestClasses (self):
        for type_class in self.listClasses:
            self.dicTestClasses[type_class.__name__] = testClass(type_class)
            
    def testprocess (self):
        self.processing()
        
    def postprocess (self):
        self.postprocessing()
        self.log.executeBuffer
            
    ### API ###
    
    def appendFunctionToTest (self, func):
        self.listFunctions.append(func)
    
    def appendClassToTest (self, obj):
        self.listClasses.append(obj)
        
    def setFunction (self, myFunction):
        self.activeFunctionName = myFunction
        self.log.buffer(myFunction)
        self.active = self.dicTestFunctions[myFunction]
        
    def setClass (self, myClass, *args, **kwargs):
        arguments = parseArguments(*args, **kwargs)
        self.log.buffer(myClass + arguments)
        self.activeClass = self.dicTestClasses[myClass](*args, **kwargs)
    
    def setMethod (self, myMethod):
        self.activeFunctionName = myMethod
        self.log.buffer(myMethod)
        self.active = getattr(self.activeClass, myMethod)
            
    def assertTest (self, args=(), kwargs={}, expected=None):
        arguments = parseArguments(*args, **kwargs)
        self.log.buffer(self.activeFunctionName + arguments)
        try:
            assert self.active(*args, **kwargs) == expected
        except:
            self.log.buffer("failed lol")
