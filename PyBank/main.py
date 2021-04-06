import os
import csv

# Path to collect data from the Resources folder
PyBankCsv = os.path.join('Resources', 'budget_data.csv')

dates = []
revenues = []

averageRevenue = 0
with open(PyBankCsv) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in csvReader:
        dates.append(row[0])
        revenues.append(int(row[1]))
       
totalMonths = len(dates)
totalProfit = sum(revenues)

changeTotal = 0
profitTracker = (revenues[1]) - (revenues[0])
lossTracker = (revenues[1]) - (revenues[0])

for i in range(0,totalMonths-1):
    change = (revenues[i+1]) - (revenues[i])
    if change >= profitTracker:
        profitTracker = change
        dateTrackerProfit = dates[i+1]
    elif change <= lossTracker:
        lossTracker = change
        dateTrackerLoss = dates[i+1]
    changeTotal += change



averageRevenueChange = changeTotal / totalMonths

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total Revenue: {totalProfit}")
print(f"Average Revenue Change: {averageRevenueChange}")
print(f"Greatest Increase in Profit: {dateTrackerProfit} $ {profitTracker}" )
print(f"Greatest Decrease in Profit: {dateTrackerLoss} $ {lossTracker}" )






    





