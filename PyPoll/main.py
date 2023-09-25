import csv
from pathlib import Path

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
greatest_votes = 0

# Read the CSV file
csvpath = Path("Resources/election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader)

    # Loop for all rows in the CSV file
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        # If candidate is not found, include them with a vote
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1

# Print the total amount of votes
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

#Variable for percentage votes
Percentage_votes = ""

# This code creates a result for each candidate and prints
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Check if othe candidate has more votes than the winner
    if votes > greatest_votes:
        greatest_votes = votes
        winner = candidate

    Percentage_votes += f"{candidate}: {percentage:.3f}% ({votes})\n"

print("-------------------------")

# Print winner of popular vote
print(f"Winner: {winner}")
print("-------------------------")

#Create a textfile
output_file = 'Pypoll_analysis.txt'

with open(output_file, 'w') as f:

    f.write("Election Results\n")

    f.write("------------------\n")

    f.write(f"Total Votes: {total_votes}\n")

    f.write("------------------\n")

    f.write(str(Percentage_votes))
            
    f.write("------------------\n")

    f.write(f"Winner: {winner}\n")

    f.write("------------------\n")