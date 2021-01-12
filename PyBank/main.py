# import dependencies
import os
import csv

# path to collect data from the resources folder
budget_csv = os.path.join('Resources','budget_data.csv')

# variables for values from budget_csv (pandl is Profit and Losses)
months = []
pandl_changes = []
monthcount = 0
net_pandl = 0
current_month_pandl = 0
prev_month_pandl = 0
pandl_change = 0

# read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # read in the header row first
    header = next(csvreader)

    #check if data is successfully loaded and header appears
    #print(header)
  
    # Loop through the data
    for row in csvreader:

        # count all the months in the csv
        monthcount += 1

        # net profit and losses for total in report
        current_month_pandl = int(row[1])
        net_pandl += current_month_pandl

        # if statement to append the variables for months and pandl change each time the for loop runs
        if  (monthcount == 1):
            prev_month_pandl = current_month_pandl

        else:

            # calculate the change in profits and losses from the previous month
            pandl_change = current_month_pandl - prev_month_pandl

            # append months to the month counter
            months.append(row[0])

            # append the pandl change from the previous month to the pandl changes counter
            pandl_changes.append(pandl_change)

            # set equal for the next run of the loop
            prev_month_pandl = current_month_pandl

    #check if successfully runs
    print(current_month_pandl)




















# print report with triple f string
report = (f"""Financial Analysis
----------------------------
Total Months: 86{monthcount}
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)""")

print(report)


