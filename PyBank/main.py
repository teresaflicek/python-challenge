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

    header = next(csvreader)

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if name_to_check == row[0]:
            print_percentages(row)


















# print report with triple f string
report = (f"""Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)""")

print(report)


