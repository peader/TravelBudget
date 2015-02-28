#import string

#Set up classes
class Currency(object):
    def __init__(self, configFilename ):
        """ configFile = string containing the full path to the config file"""
        self.configFilename = configFilename
        self.ExchangeDict = {}        
        self.LastUpdated = self.ReadConfigFile(configFilename)
        
        
     # Read config file
    def ReadConfigFile(self,filename):
      EuroExchangeconfigfile = open(filename,'r')
      lines =  EuroExchangeconfigfile.readlines()
      #print lines
      ExchangeDictVars = []
      DateUpdated = ''
      key = ''
   
      for line in lines:
        #print line
        if 'LAST UPDATED:' in line:
           DateUpdated = line[line.index('LAST UPDATED:') + 14:]
           DateUpdated = DateUpdated.replace('\n','')
        elif 'TITLE:' in line:
           key = line[line.index('TITLE:') + 7:]
           key = key.replace('\n','')
        elif 'DESCRIPTION: 1 Euro =' in line:
           ExchangeDictVars = line[line.index('DESCRIPTION: 1 Euro =') + 21:].split(' ')
           ExchangeDictVars[2] = ' '.join(ExchangeDictVars[2:])
           ExchangeDictVars[2] = ExchangeDictVars[2].replace('\n','')
           #print ExchangeDictVars[1:]
           self.ExchangeDict[key] = ExchangeDictVars[1:3]
         
      EuroExchangeconfigfile.close() 
         
      return DateUpdated
      
    def getDateUpdated(self):
        return self.LastUpdated
        
    def getExchangeDict(self):
        return self.ExchangeDict
      
      
       
        
        
    
class EuroExchangeRates(Currency):
      pass
      
      
      
    

