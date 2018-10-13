#import dependencies 
import os 
import csv 

#set file path 
electioncsv = os.path.join('election_data.csv')

#declare variables
totalVotes = 0
liTotal = 0 
khanTotal = 0 
correyTotal = 0 
otooleyTotal = 0
winningVoteCount = 0 

#create list of candidates
candidateList = ["Li", "Khan", "Correy", "O'Tooley"]

#reading in CSV
with open(electioncsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #for loop that is iterating over all rows in csvreader 
    for row in csvreader: 
#calculate Total Votes by adding to 0 all rows iterated over 
        totalVotes += 1
        #calculate total for candidate Li and percent 
        if (row[2]) == 'Li':
            liTotal += 1
            liPercent = liTotal/totalVotes * 100
        if (row[2]) == 'Khan':
            khanTotal += 1 
            khanPercent = khanTotal/totalVotes * 100 
        if (row[2]) == 'Correy':
            correyTotal += 1 
            correyPercent = correyTotal/totalVotes * 100 
        if (row[2]) == "O'Tooley": 
            otooleyTotal += 1 
            otooleyPercent = otooleyTotal/totalVotes * 100 
        #calculate winner  
        if otooleyTotal > correyTotal and otooleyTotal > liTotal and otooleyTotal > khanTotal:
            electionWinner = "O'Tooley"
        if khanTotal > correyTotal and khanTotal > liTotal and khanTotal > otooleyTotal:
            electionWinner = "Khan"
        if liTotal > correyTotal and liTotal > otooleyTotal and liTotal > khanTotal:
            electionWinner = "Li"
        if correyTotal > otooleyTotal and correyTotal > khanTotal and correyTotal > liTotal: 
            electionWinner = "Correy" 
        


#defining Analysis and printing 
electionResults = (
f"Election Results \n"
f"-------------------------- \n"
f"Total Votes: {totalVotes} \n"
f"-------------------------- \n"
f"Khan: {khanTotal} (%{khanPercent}) \n"
f"Correy: {correyTotal} (%{correyPercent}) \n"
f"Li: {liTotal} (%{liPercent}) \n"
f"O'Tooley: {otooleyTotal} (%{otooleyPercent}) \n"
f"-------------------------- \n"
f"WINNER: {electionWinner} \n"
f"-------------------------- \n"
)
print(electionResults)

#this function writes text file to the PyBank folder 
file = open('Results From PyPoll Terminal.txt', 'w')
file.write(f"Election Results \n"
f"-------------------------- \n"
f"Total Votes: {totalVotes} \n"
f"-------------------------- \n"
f"Khan: {khanTotal} (%{khanPercent}) \n"
f"Correy: {correyTotal} (%{correyPercent}) \n"
f"Li: {liTotal} (%{liPercent}) \n"
f"O'Tooley: {otooleyTotal} (%{otooleyPercent}) \n"
f"-------------------------- \n"
f"WINNER: {electionWinner} \n"
f"-------------------------- \n"
)

file.close()