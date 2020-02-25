#Dependencies
import os
import csv

#Variables
candidates = []
votes = 0
total_votes = []

#CSV path
csvpath = os.path.join('election_data.csv')

#Open the file
with open(csvpath, newline='') as election_results:
    csvreader = csv.reader(election_results, delimiter=",")

    #skip the header
    line = next(csvreader, None)

    #Adding up the votes
    for line in csvreader:
        votes = votes + 1

        #Candidate voted for
        candidate = line[2]

        #If candidate has other votes, tally them
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            total_votes[candidate_index] = total_votes[candidate_index] + 1
        else:
            candidates.append(candidate)
            total_votes.append(1)

     #Percentages of votes for each candidate and the winner
    percentages = []
    max_votes = total_votes[0]
    max_index = 0

    for count in range(len(candidates)):
        vote_percentage = total_votes[count]/votes*100
        percentages.append(total_votes)
    if total_votes[count] > max_votes:
        max_votes = total_votes[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

#Show output
print()
print()
print()
print("Election Results")
print("By: Jamie Chamberlain")
print("---------------------------------")
print(f"Total Votes: {votes}")
print("---------------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]} % ({total_votes[count]})")
print("---------------------------------")
print(f"Winner: {winner}")
print("---------------------------------")

