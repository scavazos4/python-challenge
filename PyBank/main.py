import os
import csv

# Path to collect data from the Resources folder
PyBankCsv = os.path.join('Resources', 'budget_data')



# Define the function and have it accept the 'budget_data' as its sole parameter
def printData(BankData)
    date = str(BankData[0])
    profit = float(BankData[1])

    totalMonths = len(list(date))

    totalProfit = sum(list(profit))

    averageChange = totalProfit / totalMonths

    profitTracker1 = 0
    profitTracker2 = 0
    lossTracker1 = 0
    lossTracker2 = 0

    for row in csvReader:
        for i in profit:
                profitTracker1 = profit[i+1] - profit[i]
                if profitTracker1 >= profitTracker2:
                    profitTracker2 = profit[i+1] - profit[i]
                    dateTrackerProfit = date[i+1]


    for row in csvReader:
        for i in profit:
            lossTracker1 = profit[i+1]-profit[i]
            if losstracker1 <= lossTracker2
                lossTracker2 = profit[i+1] - profit[i]
                dateTrackerLoss = date[i+1]



    





