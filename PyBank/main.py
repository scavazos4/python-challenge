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
for i in revenues:
    change = (i) - (i+1)
    changeTotal += change

AverageRevenueChange = changeTotal / totalMonths

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total Revenue: {totalProfit}")
print(f"Average Revenue Change: {averageRevenue}")
#    print(f"Greatest Increase in Profit: {dateTrackerProfit} $ {profitTracker2}" )
#    print(f"Greatest Decrease in Profit: {dateTrackerLoss} $ {lossTracker2}" )






    





