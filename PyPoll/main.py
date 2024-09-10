import csv

def print_and_write(output, file):
    print(output)
    file.write(output + '\n')

# My variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Pathing my CSV file 
with open('C:/Users/Cloud/LearnPython/Python-Challenge/Python-challenge/PyPoll/Resources/election_data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    for row in reader:
        candidate = row[2]
        total_votes += 1
        
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculating the percentage for the candidates that won
for candidate in candidates:
    votes = candidates[candidate]
    percentage = (votes / total_votes) * 100
    candidates[candidate] = (votes, percentage)
    
    # The real MVP :)
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

# Create a txt file (notepad) with the results
with open('election_analysis.txt', 'w') as txt_file:
    print_and_write("Election Results", txt_file)
    print_and_write("-------------------------", txt_file)
    print_and_write(f"Total Votes: {total_votes}", txt_file)
    print_and_write("-------------------------", txt_file)
    for candidate, (votes, percentage) in candidates.items():
        print_and_write(f"{candidate}: {percentage:.3f}% ({votes})", txt_file)
    print_and_write("-------------------------", txt_file)
    print_and_write(f"Winner: {winner}", txt_file)
    print_and_write("-------------------------", txt_file)
