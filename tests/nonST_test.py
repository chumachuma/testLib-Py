#######################################################################
#Temporary until paths are fixed
import sys
sys.path.append('D:/Desktop/Desktop_Temp/Programacio/')
#######################################################################

TUTORIAL = """
nonStopTesting.py
_________________________________________
This module adds two decorators to have non-stop error handling when 
and exception is raised

import testLib.nonStopTesting as testDeco

testFunction = testDeco.testFunction
testClass = testDeco.testClass
_________________________________________
1 - testFunction
_________________________________________
    1.1 @testFunction
        def foo (vars):
            ...
            # This also works for classes instances
            
    1.2 testFoo = testFunction(foo)
        # The function can be replaced with variable normal procedure
    
    1.3 MyClass.foo = testFunction(MyClass.foo)
        # This will replace the current instance in the class
    
    1.4 setattr(MyClass, "foo", testFunction(MyClass.foo))
        # This will replace the current instance in the class
        
_________________________________________
2 - testClass
_________________________________________
    2.1 testMyClass = testClass(MyClass)
        # The class can be replaced with variable normal procedure
"""

"""PREPROCESSING"""
import testLib.nonStopTesting as testDeco
import testLib.dummies.functions as dummyFunc
import testLib.dummies.classes as dummyClass

testFunction = testDeco.testFunction
testClass = testDeco.testClass

menuFunction = testFunction(dummyFunc.menu)
errorFunction = testFunction(dummyFunc.forceError)
class errorClass:
    def __init__(self, myvar):
        self.myvar = myvar
        self.classvar = 1
        
    @testFunction    
    def forceError (self):
        raise Exception
purposeClass = testClass(dummyClass.MyC)

"""TESTPROCESSING"""
# Errors are handled in functions
menuFunction()
menuFunction(0)
menuFunction(1)
menuFunction(2)
menuFunction(3)
menuFunction()
menuFunction(parameter=4)
menuFunction(false_parameter=5)
manualMenuFunction = testFunction(menuFunction)
manualMenuFunction(0)


# Errors are displayed correctly
errorFunction()
errorFunction(1)
#errorFunction(b) # error outside function scope
errorFunction(1,2,b=1)
errorFunction(b=1)


# Errors are handled in methods    
errorClass(1).forceError()

# Errors are handled in classes
ppClass = purposeClass(1)
#ppClass = purposeClass() # __init__ can't be test
ppClass.action()
ppClass.action(1)
ppClass.getMyvar()
ppClass.getMyvar(1)
ppClass.forceError()

# A copy of the class is made, so the original remains untouched
oClass = dummyClass.MyC(1)
try:
    oClass.forceError()
except:
    print("Origianl still fails")
# Change original class
setattr(dummyClass.MyC, "forceError", testFunction(dummyClass.MyC.forceError))
dummyClass.MyC.getMyvar = testFunction(dummyClass.MyC.getMyvar)
dummyClass.MyC(1).forceError()
dummyClass.MyC(1).getMyvar(1)

    
"""POSTPROCESSING"""
print ("""
*********************************************************
* If you read this sentence the test does work properly *
*********************************************************
""")
print (TUTORIAL)