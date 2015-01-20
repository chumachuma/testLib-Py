"""OUTPUT SPEED
The following script studies the difference in time to perform an output via console and to write into a file.

The output methods studied are:
    - print: the default output via console
    - open: the default file input/output system
        - open-write-close
        - open-write...write-close
    
To perform this study a random string of 25k lines will be generated, this same string will passed into the the 
different chosen output methods.
And it will be passed in different ways in order to determine which presents the best behaviour:
    - line by line
    - chunk of data
        - chunks of 01k lines
        - chunks of 10k lines
        - chunks of 20k lines
    - all the data at once 

Finally, each test will be performed 100 and with the data obtained it will be performed a statistical analysis.
"""
import sys
sys.path.append('D:/Desktop/Desktop_Temp/Programacio/')

import random
import testLib

gl = testLib.GLOBALS
timeFunction = testLib.timeFunction.timeFunction

__author__ = "JiaJiunn Chiou"
__version__  = "1.0"
__status__ = "Study"
__python_version__ = "3.4"
__since__ = "07/01/2015"
__change__ = "11/01/2015"

NUMBER_OF_LINES = 50000 #~2.9GB!
MAX_CHARACTERS_IN_LINE = 80
CHUNK_SIZES = [1, 1000, 10000, 20000, NUMBER_OF_LINES]
NTEST = 5
TEST_ITERATIONS = 150
LOG_FILENAME = "temp_log.txt"
RESULTS_FILENAME = "log.txt"
STRING_COMPONENT = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"

@timeFunction
def studyOutputSpeed():
    print( "Output Methods Simulation started" )
    
    # PREPROCESSING
    Cases = (
            "prntByLines", "prntChunk01", "prntChunk10", "prntChunk20", "prntAllData",
            "OpClByLines", "OpClChunk01", "OpClChunk10", "OpClChunk20", "OpClAllData",
            "OpWrByLines", "OpWrChunk01", "OpWrChunk10", "OpWrChunk20", "OpWrAllData",
            "TotalStringLength"
            )
    name2ID = {name: ID for (ID, name) in enumerate(Cases)}
    Results = [[] for i in range(Cases.__len__())]
    
    stringCases = RandomStringGenerator(NUMBER_OF_LINES)
    outputMethods = OutputMethodsTimer()
    
    # PROCESSINNG 
    for test_iteration in range(TEST_ITERATIONS):
        stringCases.generateRandomStringList()
        Results[name2ID["TotalStringLength"]].append( str(stringCases.getTotalLength()) )
        for i in range(NTEST):
            chunk_size = CHUNK_SIZES[i]
            chunked_list = stringCases.generateChunkedStringList(chunk_size)
            outputMethods.setStringList(chunked_list)            
            Results[name2ID["prntByLines"] + i].append( str(outputMethods.prntBy()))
            clearLog(LOG_FILENAME)
            Results[name2ID["OpClByLines"] + i].append( str(outputMethods.OpCLBy()) )
            clearLog(LOG_FILENAME)
            Results[name2ID["OpWrByLines"] + i].append( str(outputMethods.OpWrBy()) )
        
    clearLog(LOG_FILENAME)
    
    with open(RESULTS_FILENAME, "w") as file:
        for i in range(Cases.__len__()):
            file.write(Cases[i] +", " + ", ".join(Results[i]) + "\n")
        
    print( "Output Methods Simulation ended" )
    
    
class RandomStringGenerator:
    
    def __init__ (self, lines):
        self.lines = lines
        self.randomStringList = []
     
    def generateRandomStringList (self):
        self.randomStringList = []
        for line in range(self.lines):
           self.randomStringList.append(self.generateRandomLine(MAX_CHARACTERS_IN_LINE))
        
    def generateRandomLine (self, max_characters):
        return "".join( random.choice(STRING_COMPONENT) for i in range(random.randint(1, max_characters)) )
    
    def generateChunkedStringList (self, chunk_size):
        return [stringChunk for stringChunk in self.getChunk(chunk_size)]
    
    def getChunk (self, chunk_size):
        remainder_chunk = self.lines % chunk_size
        i = 0
        while i < self.lines-remainder_chunk:
            yield ( "".join(self.randomStringList[i:i+chunk_size]) )
            i += chunk_size
        if self.randomStringList[i:]:
            yield ( "".join(self.randomStringList[i:]) )
            
    def getTotalLength (self):
        return "".join(self.randomStringList).__len__()

def clearLog (log_name):
    open(log_name, 'w').close()

class OutputMethodsTimer:
    
    def __init__ (self):
        self.stringList = []
        
    def setStringList (self, stringList):
        self.stringList = stringList
    
    @timeFunction
    def prntBy (self):
        for string_chunk in self.stringList:
            print(string_chunk)
    
    @timeFunction
    def OpCLBy (self):
        for string_chunk in self.stringList:
            with open(LOG_FILENAME, "a") as file:
                file.write(string_chunk)
    
    @timeFunction
    def OpWrBy (self):
        file = open(LOG_FILENAME, "w")
        for string_chunk in self.stringList:
            file.write(string_chunk)
        file.close()
        
if __name__ == "__main__":
    print (studyOutputSpeed())