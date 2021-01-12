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

# average change of profit and losses over the entire period
    avg_pandl = round(sum(pandl_changes)/len(pandl_changes), 2)

# greatest increase in profits (date and amount)
    
    # greatest amount increase in profits
    great_increase = max(pandl_changes)

    # greatest increase in profits date pulled using .index
    great_inc_index = pandl_changes.index(great_increase)
    great_inc_month = months[great_inc_index]

# greatest decrease in profits (date and amount)
    
    # greatest amount decrease in profits
    great_decrease = min(pandl_changes)

    # greatest decrease in profits date pulled using .index
    great_dec_index = pandl_changes.index(great_decrease)
    great_dec_month = months[great_dec_index]


# print report with triple f string
report = (f"""Financial Analysis
----------------------------
Total Months: {monthcount}
Total: ${net_pandl}
Average  Change: ${avg_pandl}
Greatest Increase in Profits: {great_inc_month} (${great_increase});
Greatest Decrease in Profits: {great_dec_month} (${great_decrease});""")

print(report)

# write the results into a text file
outputFile = os.path.join('analysis', 'pybank_report.txt')

with open(outputFile, 'w') as text_file:
    text_file.write(f"""
    Financial Analysis
    ----------------------------
    Total Months: {monthcount}
    Total: ${net_pandl}
    Average  Change: ${avg_pandl}
    Greatest Increase in Profits: {great_inc_month} (${great_increase});
    Greatest Decrease in Profits: {great_dec_month} (${great_decrease});""")

