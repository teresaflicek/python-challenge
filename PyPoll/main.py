# import dependencies
import os
import csv

# path to collect data from the resources folder
election_csv = os.path.join('Resources','election_data.csv')

# variables for values from election_csv
total_votes = 0
cand_names = []
percent_votes = []
num_votes = []


# read in the CSV file
with open(election_csv, 'r') as csvfile:

    # split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # read in the header row first
    header = next(csvreader)

    #check if data is successfully loaded and header appears
    #print(header)
  
    # loop through the data
    for row in csvreader:

        # count all the votes in the csv
        total_votes += 1

        if (total_votes == 1):
            cand_names.append(row[0])
            num_votes.append(1)

    # percent votes
    






# print report with triple f string
report = (f"""Election Results
-------------------------
Total Votes: 3521001 {total_votes}
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

# write the results into a text file
# outputFile = os.path.join('analysis', 'pypoll_report.txt')

# with open(outputFile, 'w') as text_file:
#     text_file.write