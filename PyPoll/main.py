# import dependencies
import os
import csv

# path to collect data from the resources folder
election_csv = os.path.join('Resources','election_data.csv')

# variables for values from election_csv
total_votes = 0
cand_names = []



# read in the CSV file
# with open(election_csv, 'r') as csvfile:

#     # split the data on commas
#     csvreader = csv.reader(csvfile, delimiter=',')

#     # read in the header row first
#     header = next(csvreader)

#     #check if data is successfully loaded and header appears
#     #print(header)
  
#     # loop through the data
#     for row in csvreader:









# print report with triple f string
report = (f"""
    Election Results
    -------------------------
    Total Votes: 3521001
    -------------------------
    Khan: 63.000% (2218231)
    Correy: 20.000% (704200)
    Li: 14.000% (492940)
    O'Tooley: 3.000% (105630)
    -------------------------
    Winner: Khan
    -------------------------
""")

print(report)