#import dependencies 
import os 
import csv 

#set file path 
budgetcsv = os.path.join('budget_data.csv')

#declare variables
totalMonths = 0 
totalRevenue = 0
pastRevenue = 0  
greatestInc = 0 
greatestDec = 0 
#list which will store the month to month changes in revenue 
revenueChange = []

#reading in CSV
with open(budgetcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #for loop that is iterating over all rows in csvreader 
    for row in csvreader: 
        #calulate Total Months by simply adding to 0 all rows iterated over 
        totalMonths += 1 
        #calculate Total Revenue by adding all integers from revenue column
        totalRevenue = totalRevenue + int(row[1])
        monthChange = int(row[1]) - pastRevenue
        pastRevenue = int(row[1])
        revenueChange.append(monthChange)
        avgRevChange = round(sum(revenueChange)/totalMonths)
        #this if block compares monthChange to the greatestInc/greatestDec as it updates
        if (monthChange > greatestInc): 
            greatestIncDate = row[0]
            greatestInc = monthChange
        if (monthChange < greatestDec):
            greatestDecDate = row[0]
            greatestDec = monthChange

pastRevenue = 0 

#defining Analysis and printing 
Analysis = (
f"Financial Analysis \n"
f"-------------------------- \n"
f"Total Months: {totalMonths} \n"
f"Total Revenue: ${totalRevenue} \n"
f"Average Revenue Change: ${avgRevChange} \n"
f"Greatest Increase in Revenue: {greatestIncDate} (${greatestInc}) \n"
f"Greatest Decrease in Revenue: {greatestDecDate} (${greatestDec}) \n"
)
print(Analysis)

#this function writes text file to the PyBank folder 
file = open('Results From PyBank Terminal.txt', 'w')
file.write(f"Financial Analysis \n"
f"-------------------------- \n"
f"Total Months: {totalMonths} \n"
f"Total Revenue: ${totalRevenue} \n"
f"Average Revenue Change: ${avgRevChange} \n"
f"Greatest Increase in Revenue: {greatestIncDate} (${greatestInc}) \n"
f"Greatest Decrease in Revenue: {greatestDecDate} (${greatestDec}) \n")

file.close()
