#Set up classes
class Money(Object):
    def __init__(self):
        pass
    
class Euro(Money):
  def __init__(self):
      pass

  def ReadEuroConfigFile():
   EuroExchangeconfigfile = open('C:/Users/peter/Documents/GitHub/TravelBudget/config.txt','r')
   lines =  EuroExchangeconfigfile.readlines()

   
   for line in lines:
       
    

EuroExchangeconfigfile.close()      
    
        
        

    


