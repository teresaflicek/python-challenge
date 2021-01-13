# import dependencies
import os
import csv

# path to collect data from the resources folder
election_csv = os.path.join('Resources','election_data.csv')

# variables for values from election_csv
total_votes = 0
cand_names = []
vote_percents = []
cand_votes = []


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

        #if statement to add the number of votes to candidates vote totals
        if (total_votes == 1):
            cand_names.append(row[2])
            cand_votes.append(1)

    # percent of votes comparable to total for each candidate
    for votes in cand_votes:
        percent = (votes / total_votes)*100
        percent = round((percent))
        vote_percents.append(percent)

# winner of the election

# variable containing the most votes
winner_votes = max(cand_votes)

# variables containing the winner name 
winner_index = cand_votes.index(winner_votes)
winner_cand = cand_names[winner_index]

#printing the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
for i in range(len(cand_names)):
    print(f"{cand_names[i]}: {vote_percents[i]} {cand_votes[i]}")
print(f"Winners: {winner_cand}")





# print report with triple f string
# report = (f"""

# Election Results
# -------------------------
# Total Votes: 3521001 {total_votes}
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
# """)

# write the results into a text file
outputFile = os.path.join('analysis', 'pypoll_report.txt')

with open(outputFile, 'w') as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    for i in range(len(cand_names)):
        text_file.write(f"{cand_names[i]}: {vote_percents[i]} {cand_votes[i]}\n")
    text_file.write(f"Winners: {winner_cand}\n")