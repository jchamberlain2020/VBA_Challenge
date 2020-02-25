#Dependencies
import os
import csv

#CSV path
csvpath = os.path.join('budget_data.csv')

#Variables to track
total_months = 0
net_profit_loss = 0
orig_profit_loss = 0
net_change_list = []
month_change_list = []

greatest_increase = ["",0]
greatest_decrease = ["", 99999999999999999999]

#Open/Reading data with delimiter
with open(csvpath, newline='') as budgetdata:
    csvreader = csv.reader(budgetdata, delimiter=",")

    print(csvreader) 
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Setting up data
    firstrow = next(csvreader)
    total_months = total_months + 1
    net_profit_loss = net_profit_loss + int(firstrow[1])
    orig_profit_loss = int(firstrow[1])

    #After the header
    for row in csvreader:
        #Total number of months
        total_months = total_months + 1

        #Net Profit/Losses
        net_profit_loss = net_profit_loss + int(row[1])

        #Average Change Profit Losses
        net_change = int(row[1]) - orig_profit_loss

        net_change_list = net_change_list + [net_change]
        month_change_list = month_change_list + [row[0]]

        #Greatest increase and greatest increase in profits       
        if net_change > greatest_increase[1]:
                greatest_increase[0] = row[0]

                greatest_increase[1] = net_change
            
        #Greatest decreases in losses
        if net_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]

                greatest_decrease[1] = net_change
            
        orig_profit_loss = int(row[1]) 

average_monthly_net_change = sum(net_change_list) / len(month_change_list)

# Show output
print()
print()
print()
print("Financial Analysis")
print("By: Jamie Chamberlain")
print("-------------------------")
print ( "Total Months: " + str(total_months))
print ("Total: $" + str(net_profit_loss))
print ("Avgerage Change: $" + str(average_monthly_net_change ))
print ("Greatest Increase in Profit: " + str(greatest_increase[0]) + " / " + "$" + str(greatest_increase[1])) 
print ("Greatest Decrease in Profit: " + str(greatest_decrease[0]) + " / " + "$" + str(greatest_decrease[1])) 