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
  
    # loop through the data
    for row in csvreader:

        # count all the votes in the csv
        total_votes += 1

        #if statement to add the number of votes to candidates vote totals
        if cand_names.count(row[2]) == 0:
            cand_names.append(row[2])
            cand_votes.append(1)

        else:
            cand_votes[cand_names.index(row[2])] += 1

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
print("-------------------------")
for i in range(len(cand_names)):
    print(f"{cand_names[i]}: {(vote_percents[i]):.3f}% {cand_votes[i]}")
print("-------------------------")
print(f"Winners: {winner_cand}")
print("-------------------------")

# write the results into a text file
outputFile = os.path.join('analysis', 'pypoll_report.txt')

with open(outputFile, 'w') as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")
    for i in range(len(cand_names)):
        text_file.write(f"{cand_names[i]}: {(vote_percents[i]):.3f}% {cand_votes[i]}\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winners: {winner_cand}\n")
    text_file.write("-------------------------\n")