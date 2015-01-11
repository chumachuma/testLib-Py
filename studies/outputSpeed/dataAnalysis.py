import pylab

class DataAnalysis:
    def __init__ (self):
        self.name2dataID = {}
        self.dataID2name = []
        self.data = []
        
    def loadDataFrom (self, filename):
        with open(filename, "r") as file:
            for index, line in enumerate(file):
                line_list = line.split(", ")
                self.dataID2name.append(line_list[0])
                self.name2dataID[line_list[0]] = index
                line_list.pop(0)
                line_list.pop()
                self.data.append([float(i) for i in line_list])

    def getData (self, data_name):
        return self.data(self.name2dataID[data_name])
    
def getColor (name):
    name2color = {
                    "prntByLines" : "red",
                    "prntChunk01" : "red",
                    "prntChunk10" : "red",
                    "prntChunk20" : "red",
                    "prntAllData" : "red",
                    "OpClByLines" : "blue",
                    "OpClChunk01" : "blue",
                    "OpClChunk10" : "blue",
                    "OpClChunk20" : "blue",
                    "OpClAllData" : "blue",   
                    "OpWrByLines" : "green",
                    "OpWrChunk01" : "green",
                    "OpWrChunk10" : "green",
                    "OpWrChunk20" : "green",
                    "OpWrAllData" : "green",
                    "TotalStringLength" : "black"
                  }
    return name2color[name]

def getPosition (name):
    code = name [-2:]
    if code == "es":
        return [1]
    elif code == "01":
        return [2]
    elif code == "10":
        return [3]
    elif code == "20":
        return [4]
    elif code == "ta":
        return [5]
    else:
        return [6]

def boxplots(myData):
    fig = pylab.figure(1)
    ax = pylab.axes()
    pylab.hold(True)
    
    """bp = pylab.boxplot(myData.data[1:5], sym='')
    pylab.setp(bp['boxes'], color="red")
    pylab.setp(bp['whiskers'], color="red")
    pylab.setp(bp['fliers'], color="red")
    pylab.setp(bp['medians'], color="red")
    pylab.setp(bp['caps'], color="red")"""
    
    bp = pylab.boxplot(myData.data[6:10], sym='')
    pylab.setp(bp['boxes'], color="blue")
    pylab.setp(bp['whiskers'], color="blue")
    pylab.setp(bp['fliers'], color="blue")
    pylab.setp(bp['medians'], color="blue")
    pylab.setp(bp['caps'], color="blue")
    
    bp = pylab.boxplot(myData.data[11:15], sym='')
    pylab.setp(bp['boxes'], color="green")
    pylab.setp(bp['whiskers'], color="green")
    pylab.setp(bp['fliers'], color="green")
    pylab.setp(bp['medians'], color="green")
    pylab.setp(bp['caps'], color="green")
    
    """for index, data  in enumerate(myData.data[:-1]):
        try:
            name = myData.dataID2name[index]
            bp = pylab.boxplot(data, positions=getPosition(name), widths = 0.6)#, showmeans=True)
            pylab.setp(bp['boxes'], color=getColor(name))
            pylab.setp(bp['whiskers'], color=getColor(name))
            pylab.setp(bp['fliers'], color=getColor(name))
        except:
            pass"""
        
    pylab.savefig('boxcompare.png')
    pylab.show()
    
if __name__ == "__main__":
    myData = DataAnalysis()
    myData.loadDataFrom ("log.txt")
    boxplots(myData)