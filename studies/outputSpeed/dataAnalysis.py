import pylab

def postProcessing ():
    myData = DataAnalysis()
    myData.loadDataFrom ("log.txt")
    
    means = myData.getMean()
    stds = myData.getSTD()
    cvs = myData.getCoefficientVariation(2)
    print (cvs)
    fivenum = myData.get5num()
    
    with open ("Results.txt", "w") as file:
        file.write("CONCEPT\t\tMEAN\t\tSTD\t\tMIN\t\tP25\t\tMEAN\t\tP75\t\tMAX\n")
        for i in range(myData.dataID2name.__len__()):
            file.write(myData.dataID2name[i] + "\t" + 
                       str(means[i]) + "\t" + str(stds[i]) + "\t" +
                       "\t".join([str(j) for j in fivenum[i]]) + "\n")
            
    pylab.figure(1)
    pylab.axes()
    pylab.hold(True)
    j = 1 #crappy hack
    X = [i for i in range(1,6)]
    for i in range(3):
        pylab.plot( X[j:], means[i*5+j:(i+1)*5], color=getColor(myData.dataID2name[i*5]) )
    """for row in range(means.__len__()-1):
        circle = pylab.Circle( (i%5, means[i]), cvs[i], fc=getColor(myData.dataID2name[i]) )
        pylab.gca().add_patch(circle)
        
    #pylab.axis('scaled')"""
    pylab.savefig('Results.png')
    pylab.show()
    
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
    
    def getMean (self):
        return [pylab.mean(row) for row in self.data]
    
    def getSTD (self):
        return [pylab.std(row) for row in self.data]
    
    def getCoefficientVariation (self, scale=1):
        return [(std/mean)*scale for std, mean in zip(self.getSTD(), self.getMean())]
    
    def get5num (self):
        mins = [min(row) for row in self.data]
        p25s = [pylab.percentile(row, 25) for row in self.data]
        medians = [pylab.percentile(row, 50) for row in self.data]
        p75s = [pylab.percentile(row, 75) for row in self.data]
        maxs = [max(row) for row in self.data]
        return [fivenum for fivenum in zip(mins, p25s, medians, p75s, maxs)]
    
def getColor (name):
    code = name[:4]
    if code == "prnt":
        color = "red"
    elif code == "OpCl":
        color = "blue"
    elif code == "OpWr":
        color = "green"
    elif code == "Total":
        color = "black"
    else:
        color = "pink"
    return color

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
    postProcessing()