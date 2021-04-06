import os
import csv
import pandas as pd
# Path to collect data from the Resources folder
PyBankCsv = os.path.join('Resources', 'election_data.csv')

# setting up arrays to store data
candidate = []


# pulling data into arrays from CSV file
averageRevenue = 0
with open(PyBankCsv) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in csvReader:
        candidate.append(row[2])

TotalVotes = len(candidate)

uniqueCandidates = []
for x in candidate:
    if x not in uniqueCandidates:
        uniqueCandidates.append(x)
    
print(uniqueCandidates)

khanVotesTotal=0
correyVotesTotal = 0
liVotesTotal = 0
oTooleyVotesTotal = 0
for x in candidate:
    if x == "Khan":
        khanVotesTotal += 1
    elif x == "Correy":
        correyVotesTotal += 1
    elif x == "Li":
        liVotesTotal += 1
    elif x == "O'Tooley":
        oTooleyVotesTotal += 1

khanVotesPercent = round(khanVotesTotal / TotalVotes *100)
correyVotesPercent = round(correyVotesTotal / TotalVotes * 100)
liVotesPercent =  round(liVotesTotal  / TotalVotes *100)
oTooleyVotesPercent =   round(oTooleyVotesTotal /TotalVotes * 100)


winner = 





print("Election Analysis")
print("----------------------------")
print(f"Total Votes: {TotalVotes}")
print("----------------------------")
print(f" Khan:     {khanVotesPercent}   ({khanVotesTotal}) ")   
print(f" Correy:   {correyVotesPercent}   ({correyVotesTotal}) ")   
print(f" Li:       {liVotesPercent}   ({liVotesTotal}) ")   
print(f" O'Tooley: {oTooleyVotesPercent}    ({oTooleyVotesTotal}) ")   
print("----------------------------")
print(f"Winner: {winner} " )




