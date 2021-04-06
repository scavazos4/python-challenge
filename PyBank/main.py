import os
import csv

# Path to collect data from the Resources folder
PyBankCsv = os.path.join('Resources', 'budget_data.csv')

# setting up arrays to store data
dates = []
revenues = []

# pulling data into arrays from CSV file
averageRevenue = 0
with open(PyBankCsv) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in csvReader:
        dates.append(row[0])
        revenues.append(int(row[1]))

# creating variables to store values       
totalMonths = len(dates)
totalProfit = sum(revenues)

# creating variables to store initial data
changeTotal = 0
profitTracker = (revenues[1]) - (revenues[0])
lossTracker = (revenues[1]) - (revenues[0])

# for loop for calculating average change 
# and tracking greates and least changes
for i in range(0,totalMonths-1):
    change = (revenues[i+1]) - (revenues[i])
    if change >= profitTracker:
        profitTracker = change
        dateTrackerProfit = dates[i+1]
    elif change <= lossTracker:
        lossTracker = change
        dateTrackerLoss = dates[i+1]
    changeTotal += change


# calculating average revenue change
averageRevenueChange = changeTotal / totalMonths

#outputing analysis to console
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total Revenue: {totalProfit}")
print(f"Average Revenue Change: {averageRevenueChange}")
print(f"Greatest Increase in Profit: {dateTrackerProfit} $ {profitTracker}" )
print(f"Greatest Decrease in Profit: {dateTrackerLoss} $ {lossTracker}" )

#outputing analysis to file
textoutput = os.path.join("Analysis", 'Financial_summary.txt')
with open (textoutput, 'w', newline='') as summary:
    write = csv.writer(summary)
    write.writerows([
["Financial Analysis"],
["----------------------------"],
["Total Months: " + str(totalMonths)],
["Total Revenue: $" + str(totalProfit)],
["Average Revenue Change: $" + str(averageRevenueChange)],
["Greatest Increase in Profit: " + str(dateTrackerProfit) + " $" + str(profitTracker) ],
["Greatest Decrease in Profit: " + str(dateTrackerLoss) + " $" + str(lossTracker) ]
    ])





    





