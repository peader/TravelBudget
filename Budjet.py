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
    """ ExchangeRate is an instance of an object of class 'EuroExchangeRates'"""
    def __init__(self,amount,currency,BudjetCurrency,ExchangeRates):
        Money.__init__(self,amount)
        self.currency = currency
        self.BudjetCurrency = BudjetCurrency
        self.ExchangeRates = ExchangeRates
        
    def ConvertCurrency(self):
        key = self.currency + '/' + self.BudjetCurrency
        print key
        Rate = self.ExchangeRates[key][0]
        converted = (self.amount/float(Rate))
        return converted
        
class Budjet(Money):
    def __init__(self,amount,currency):
        Money.__init__(self,amount)
        self.currency = currency
        
    def getCurrency(self):
        return self.currency
        