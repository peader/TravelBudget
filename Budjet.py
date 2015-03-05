import time
class Money(object):
    def __init__(self,amount):
        self.Date = (time.strftime("%d/%m/%Y"))
        self.amount = amount
        
    def getDate(self):
        return self.Date
        
    def getAmount(self):
        return self.amount
        
class Expenditure(Money):
    """ 'ExchangeRates' is the exhange dictionary from an instance of an object of class 'EuroExchangeRates'"""
    def __init__(self,amount,currency,BudgetCurrency,ExchangeRates):
        Money.__init__(self,amount)
        self.currency = currency
        self.BudgetCurrency = BudgetCurrency
        self.ExchangeRates = ExchangeRates
        
    def getConvertedCurrency(self):
        key = self.currency + '/' + self.BudgetCurrency
        Rate = self.ExchangeRates[key][0]
        #print 'Converted to ' + self.ExchangeRates[key][1]
        converted = (self.amount/float(Rate))
        return converted
        
class Budjet(Money):
    def __init__(self,amount,currency):
        Money.__init__(self,amount)
        self.currency = currency
        
        
    def getCurrency(self):
        return self.currency
        