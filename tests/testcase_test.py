#######################################################################
#Temporary until paths are fixed
import sys
sys.path.append('D:/Desktop/Desktop_Temp/Programacio/')
#######################################################################

import testLib.TestCase
import testLib.dummies.classes as dummyClass

TestCase = testLib.TestCase

class TestDummyClass (TestCase.TestCase):
    
    def __init__ (self):
        TestCase.TestCase.__init__(self)
    
    def preprocessing (self):
        self.TITLE("Testing the methods of a dummy class")
        self.DESCRIPTION("3 methods of a dummy class will be tested.")
        self.DESCRIPTION("The class requires one arbitrary input.")
        self.DESCRIPTION("The three methods are simple actions.")
        
        self.appendClassToTest(dummyClass.MyC)
        
    def testprocessing (self):
        self.setClass("MyC", 1)
        
        self.setMethod("action")
        self.COMMENT("Only non fail case")
        self.assertTest(
            expected = None)

        self.setMethod("getMyvar")
        self.COMMENT("Only non fail case")
        self.assertTest(
            expected = 1)
        self.COMMENT("This is not what is expected")
        self.assertTest(
            expected = 2)

        self.setMethod("forceError")
        self.COMMENT("Now it's all about errors")
        self.assertTest()
        self.assertTest(
            args = [1],
            kwargs = {"argument":0},
            expected = 1)
        

if __name__ == "__main__":
    testing_dummyClass = TestDummyClass()
    testing_dummyClass.run()