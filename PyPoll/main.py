import os
import csv

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

# create list to identify unique candidates
uniqueCandidates = []
for x in candidate:
    if x not in uniqueCandidates:
        uniqueCandidates.append(x)
    
# print(uniqueCandidates)

# counting votes
khanVotesTotal=0
correyVotesTotal = 0
liVotesTotal = 0
oTooleyVotesTotal = 0
for x in candidate:
    if x == uniqueCandidates[0]:
        khanVotesTotal += 1
    elif x == uniqueCandidates[1]:
        correyVotesTotal += 1
    elif x == uniqueCandidates[2]:
        liVotesTotal += 1
    elif x == uniqueCandidates[3]:
        oTooleyVotesTotal += 1

# 
khanVotesPercent = round(khanVotesTotal / TotalVotes *100)
correyVotesPercent = round(correyVotesTotal / TotalVotes * 100)
liVotesPercent =  round(liVotesTotal  / TotalVotes *100)
oTooleyVotesPercent =   round(oTooleyVotesTotal /TotalVotes * 100)

# decide winner votes. 
winnerVotes = max(khanVotesTotal, correyVotesTotal, liVotesTotal, oTooleyVotesTotal )

# decide winner
if khanVotesTotal > (correyVotesTotal and liVotesTotal and oTooleyVotesTotal):
    winnerName = "Khan"
elif correyVotesTotal > ( liVotesTotal and oTooleyVotesTotal):
    winnerName = "Correy"
elif liVotesTotal > (oTooleyVotesTotal):
    winnerName = "Li"
else:
    winnerName = "O'Tooley"


#outputing analysis to console
print("Election Analysis")
print("----------------------------")
print(f"Total Votes: {TotalVotes}")
print("----------------------------")
print(f" Khan:     {khanVotesPercent}   ({khanVotesTotal}) ")   
print(f" Correy:   {correyVotesPercent}   ({correyVotesTotal}) ")   
print(f" Li:       {liVotesPercent}   ({liVotesTotal}) ")   
print(f" O'Tooley: {oTooleyVotesPercent}    ({oTooleyVotesTotal}) ")   
print("----------------------------")
print(f"Winner: {winnerName} with {winnerVotes} Votes" )



#outputing analysis to file
textoutput = os.path.join("Analysis", 'Poll_summary.txt')
with open (textoutput, 'w', newline='') as summary:
    write = csv.writer(summary)
    write.writerows([
["Election Analysis"],
["----------------------------"],
[f"Total Votes:  {TotalVotes}"],
["----------------------------",],
[f"Khan:   {khanVotesPercent}   ({khanVotesTotal})"],
[f"Correy:  + {correyVotesPercent}   ({correyVotesTotal}) "],
[f"Li: + {liVotesPercent}   ({liVotesTotal}) " ],
[f"O'Tooley  {oTooleyVotesPercent}    ({oTooleyVotesTotal}) "],
["----------------------------"],
[f"Winner:  {winnerName} with {winnerVotes} Votes"]
    ])
