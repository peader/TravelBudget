from CurrencyScraper import *
from Budjet import *
from ReadWritePlotFile import *

LookOnline = False
PlotDict = {}

# Hardcode to Euros for now
ex_rates = EuroExchangeRates(LookOnline)

readPlotFile(PlotDict)

#print max(PlotDict.keys())

# Hard code Budget currency to Euros
BudgetCurrency = 'EUR'

# Have to read the plot database file for the default budget amount but for now
# hardcoding it to 15
BudgetAmount = PlotDict[max(PlotDict.keys())][0]
#print BudgetAmount

# Create the Budget object
Budget = Budjet(BudgetAmount, BudgetCurrency)
#print Budget.getCurrency()



#These next two variables need to be input by the user
ExpendAmount = 14
ExpendCurrency = 'THB'

Expend = Expenditure(ExpendAmount, ExpendCurrency, BudgetCurrency, ex_rates.getExchangeDict())

#This will be written to the plot file
#Budget 
BudgetAmount = Budget.getAmount()
BudgetDate = Budget.getDate()

# Expenditure
ExpendAmount = Expend.getConvertedCurrency()
ExpendDate = Expend.getDate()

PlotDict[BudgetDate] = [BudgetAmount, ExpendAmount]
#
Createplot(PlotDict)

#Update the plot file
writePlotFile(PlotDict)










