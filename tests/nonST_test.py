import nonStopTesting as testDeco
import dummies.functions as dummyFunc

testFunction = testDeco.testFunction

menuFunction = testFunction(dummyFunc.menu)
errorFunction = testFunction(dummyFunc.forceError)

menuFunction()
menuFunction(0)
menuFunction(1)
menuFunction(2)
menuFunction(3)
menuFunction(parameter=4)
menuFunction(fasle_parameter=5)

errorFunction()
errorFunction(1)
errorFunction(b)
errorFunction(1,2,b=1)
errorFunction(b=1)

print ("If you read this sentence the test does work properly")