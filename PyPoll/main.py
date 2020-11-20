# Correct path to the csv file on the scrip
# election_data.csv has three columns: `Voter ID`, `County`, and `Candidate`.
# Python script that analyzes nalyzes the votes and calculates:
  
#   The total number of votes cast

#   A complete list of candidates who received votes

#   The percentage of votes each candidate won

#   The total number of votes each candidate won

#   The winner of the election based on popular vote.


# Import the .csv file
import os
import csv

# csvpath - directory
# csv_path = os.path.join('C:\\Users\\\Owner\\Desktop\\Class_Material\\Homework to upload\\python-challenge\\PyPoll\\election_data.csv')
csvpath = os.path.join(r'PyPoll\Resources\election_data.csv')

# Creating variables
total_votes = 1
number_votes = []
candidates = []
percent_votes = []
percent_list = []
decimals_place = []

# Reading the cvs file
with open(csvpath) as csvfile:

#     # Opening CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader) #my content=mydata=csvsreader - this one gives me the iterator

    # Read the header row first (skip this step if there is now header)
    csvheader = next(csvreader)
    # print(f"CSV Header: {csvheader}")

 # Read each row of data after the header
    for row in csvreader:
        # print(row) 

        # Add to our total votes
        total_votes += 1 
        # print(total_votes) - not counting 3521002 or empty space 3521003 (last)

        # candidate is not in my list, add the name with the respective vote, else, if already in the list add the vote to her/his name.
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_votes[index] += 1
    
# print(candidates)
# print(total_votes)
# print(number_votes)
# print(index)


    # Add percentage of votes        
    
for votes in number_votes:
    percentage = (votes)/(total_votes) * 100
        # print(votes)
    percent_list.append(percentage)
        # print(percentage)
    # print(percent_list)

# 3 decimal places 
decimals_place = ['{:.3f}'.format(elem) for elem in percent_list]
# print(decimals_place)

# Getting the candidates and votes per each
zip_iterator = zip(candidates, number_votes)
candidates_votes = dict(zip_iterator)
# print(candidates_votes)

# winner_key = [keys for keys, values in candidates_votes.items() if values == max(candidates_votes.values())]
# print(winner_key)

# Find the winning candidate
winner = max(number_votes)
index = number_votes.index(winner)
winning_candidate = candidates[index]
# print(winning_candidate)

#Print the Analysis
print("-" * 25)
print("Election Results")
print("-" * 25)
print(f"Total Votes: {str(total_votes)}")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(decimals_place[i])}% ({str(number_votes[i])})")
print("-" * 25)
print(f"Winner: {winning_candidate}")
print("-" * 25)

# open a (new) file to write
# csv_path = os.path.join('C:\\Users\\\Owner\\Desktop\\Class_Material\\Homework to upload\\python-challenge\\PyPoll\\election_data_results.csv')
output_path = os.path.join(r'PyPoll\Analysis\election_data_results.txt')

# Write to the new txt file
with open(output_path, "w") as text_file:

    print(f"-------------------------", file = text_file)
    print(f"Election Results", file = text_file)
    print(f"-------------------------", file = text_file)
    print(f"Total Votes: {str(total_votes)}", file = text_file)
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {str(decimals_place[i])}% ({str(number_votes[i])})", file = text_file)
    print("-------------------------", file = text_file)
    print(f"Winner: {winning_candidate}", file = text_file)
    print("-" * 25, file = text_file)
    