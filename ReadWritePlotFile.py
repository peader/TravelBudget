import os

# Full file path to the folder containing this file
full_path = os.path.realpath(__file__)

def readPlotFile(PlotDict):
    """ PlotDict is the dictionary of variables which will be eventually plotted """
    filename = (os.path.dirname(full_path)) + '/' + 'PlotFile.csv'
    # Try opening  the plot file, if it doesn't exist create it and return
    try:
      PlotFile = open(filename, 'r')
    except:
      PlotFile = open(filename, 'w')
      PlotFile.close()
      return
        
    lines = PlotFile.readlines()
    for line in lines:
        #print line
        if len(line) == 0 or line[0] == '#' or line.strip() == '':
            
            continue
        # text files have the \n character for new lines, remove this
        else:
          line=line.replace('\n','')
          line = line.split(',')
          #print line
          key = line[0]
          Vars =[line[1],line[2]]
          PlotDict[key] = Vars 
    PlotFile.close()
    
def writePlotFile(PlotDict):
    filename = (os.path.dirname(full_path)) + '/' + 'PlotFile.csv'
    PlotFile = open(filename, 'w')
    
    for key in PlotDict:
        PlotFile.write(str(key) + ',' + str(PlotDict[key][0]) + ',' + str(PlotDict[key][1])+ '\n')

    

    PlotFile.close()
    
    
 
def Createplot(PlotDict):
  import matplotlib.pyplot as plt

 # D = {u'Label1':26, u'Label2': 17, u'Label3':30}

  plt.bar(range(len(PlotDict)), PlotDict.values(), align='center')
  plt.xticks(range(len(PlotDict)), PlotDict.keys())

  plt.show() 

