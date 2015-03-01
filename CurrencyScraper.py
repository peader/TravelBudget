import urllib 

#Set up classes
class Currency(object):
    def __init__(self, LookOnline ):
        """ LookOnline = boolean switch on whether to look online for exchange rates or not"""
        self.ExchangeDict = {}  
        if  LookOnline:
          self.ReadOnlineExchangeRates()     
        self.LastUpdated = self.ReadConfigFile()
        
        
        
     # Read config file
    def ReadConfigFile(self):
      if  isinstance(self,EuroExchangeRates):
        text = 'EUR' 
        filename = 'C:/Users/peter/Documents/GitHub/TravelBudget/' + text + 'config.txt'
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
      
    def ReadOnlineExchangeRates(self):
      if  isinstance(self,EuroExchangeRates):
        text = 'EUR'  
        url = 'www.themoneyconverter.com/rss-feed/' + text + '/rss.xml'
        configfilename = 'C:/Users/peter/Documents/GitHub/TravelBudget/' + text + 'config.txt'
        
        websitepath = 'http://' + url
      try:
        website = urllib.urlopen(websitepath)
        Exchangeconfigfile = open(configfilename,'w')
      except:
        print 'Cannot access online exchange rates. Using default values'
        return
        
      utext = website.readlines()
      
      firstdescrip = False
      firstitle = 0
      for line in utext:
        if '<lastBuildDate>' in line:
          string = ('LAST UPDATED: ' + line[line.index('<lastBuildDate>') + 15:line.rindex('</lastBuildDate>')] + '\n')
          Exchangeconfigfile.write(string)
      # Skip the first two '<title>' headings
        if '<title>' in line:
          if  firstitle < 2:
              firstitle += 1
          else:
            string = ('TITLE: ' + line[line.index('<title>') + 7:line.rindex('</title>')]  + '\n' )
            Exchangeconfigfile.write(string)
        #Skip the first <description>
        if '<description>' in line:
          if not firstdescrip:
              firstdescrip = True
          else:
            string = ('DESCRIPTION: ' +line[line.index('<description>') + 13:line.rindex('</description>')]  + '\n')
            Exchangeconfigfile.write(string)
        if '<category>' in line:
          string = ('CATEGORY: ' +line[line.index('<category>') + 10:line.rindex('</category>')] + '\n' + '\n' )
          Exchangeconfigfile.write(string)
    
    

      website.close()
      Exchangeconfigfile.close()
      
    def getDateUpdated(self):
        return self.LastUpdated
        
    def getExchangeDict(self):
        return self.ExchangeDict
      
      
       
        
        
    
class EuroExchangeRates(Currency):
      pass
      
      
      
    

