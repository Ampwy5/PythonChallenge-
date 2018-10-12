#import dependencies 
import os 
import csv 

#set file path 
electioncsv = os.path.join('election_data.csv')

#declare variables
totalVotes = 0 

#reading in CSV
with open(electioncsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #for loop that is iterating over all rows in csvreader 
    for row in csvreader: 
#calculate Total Votes by adding to 0 all rows iterated over 
        totalVotes += 1










#defining Analysis and printing 
electionResults = (
f"Election Results \n"
f"-------------------------- \n"
f"Total Votes: {totalMonths} \n"
f"Total Revenue: ${totalRevenue} \n"
f"Average Revenue Change: ${avgRevChange} \n"
f"Greatest Increase in Revenue: {greatestIncDate} (${greatestInc}) \n"
f"Greatest Decrease in Revenue: {greatestDecDate} (${greatestDec}) \n"
)
print(electionResults)

#this function writes text file to the PyBank folder 
file = open('Results From PyPoll Terminal.txt', 'w')
file.write(f"Financial Analysis \n"
f"-------------------------- \n"
f"Total Months: {totalMonths} \n"
f"Total Revenue: ${totalRevenue} \n"
f"Average Revenue Change: ${avgRevChange} \n"
f"Greatest Increase in Revenue: {greatestIncDate} (${greatestInc}) \n"
f"Greatest Decrease in Revenue: {greatestDecDate} (${greatestDec}) \n")

file.close()