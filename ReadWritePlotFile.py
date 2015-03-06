import os
import collections

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
    od = collections.OrderedDict(sorted(PlotDict.items()))
    filename = (os.path.dirname(full_path)) + '/' + 'PlotFile.csv'
    PlotFile = open(filename, 'w')
    
    for key in od:
        PlotFile.write(str(key) + ',' + str(od[key][0]) + ',' + str(od[key][1])+ '\n')

    

    PlotFile.close()
    
    
 
def Createplot(PlotDict):
  import matplotlib.pyplot as plt
  import datetime as dt
  import matplotlib.dates as mdates
 
  # order the PlotDict by date   
  od = collections.OrderedDict(sorted(PlotDict.items()))
  #print od
  dates = od.keys()
  x = [dt.datetime.strptime(d,'%d/%m/%Y').date() for d in dates]
  #print 'the is x:', x

 # D = {u'Label1':26, u'Label2': 17, u'Label3':30}
  y1 = []
  for value in od.values():
      y1.append(value)
      
      

  #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
  #plt.gca().xaxis.set_major_locator(mdates.DayLocator())
  plt.plot(x, y1)
  plt.gcf().autofmt_xdate()

  

  plt.show() 

