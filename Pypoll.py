# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import the datetime class from the datetime module
# import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# Print the present time.
# print("The time right now is ", now)

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to save the file to a path.
file_to_save = os.path.join ("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
    # txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")    

# 1. Initialize a total vote counter
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary
candidate_votes = {}
# Winning Cnadidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here.
    # Read the file with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read and print the header row
    headers = next(file_reader)
    # print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # print(row)
        # 2. Add to the total vote count
        # total_votes = total_votes + 1
        total_votes += 1
    
    # 3. Print the total votes.
    #  print(total_votes)

        # Print the candidate name from each row
        candidate_name = row[2]
        
        # Add the candidate name to the candidate list.
        # candidate_options.append(candidate_name)
    
    # Print the candidate list.
    # print(candidate_options)

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

        # Print the candidate list.
        # print(candidate_options)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Print the candidate vote dictionary
    # print(candidate_votes)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

        # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count =  votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # To do: print out the winning candidate, vote count and percentage to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winnning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    #Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)





