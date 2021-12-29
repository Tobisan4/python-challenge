# Import Modules
import os
import csv

# Set path for the file
csv_path = os.path.join("Resources", "election_data.csv")
                        
# Open the CSV
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Create a list that contains the voted names
    names = []
    
    # Skip the data header line
    next(csv_reader)
        
    # Read each row of data after the header
    for row in csv_reader:
        
        # Populate the "names" list with the information from the file
        names.append(row[2])

    # Calculate the total number of votes
    total_votes = len(names)

    #Create a candidate's list

    # Create a list that will contain the names of all the candidates
    candidate_list = []

    #Read all the elements in the "names" list
    for entree in names:
    
        # Check if the name already exists on the candidate list or not
        if entree not in candidate_list:
        
            # If name doesn't exist, add it to the candidate list
            candidate_list.append(entree)

    # Count the number of votes each candidate received

    # Create a list that will hold the number of votes for each candidate
    vote_count = []

    # Count the votes and record them to the "vote_count" list
    for candidate1 in candidate_list:
    
        # Initialize vote counter
        count = 0
    
        for vote in names:
            if vote == candidate1:
                count = count + 1
        vote_count.append(count)

    # Calculate the percentage of votes for each candidate

    # Create a list that will hold the percentage of votes for each candidate
    vote_percent=[]

    # Calculate the vote percentage then record it in the "vote_percent" list
    for candidate2 in candidate_list:
        position = candidate_list.index(candidate2)
        percentage = format((vote_count[position] / total_votes), '.3%')
        vote_percent.append(percentage)

    # Determine election winner
    winner_count = max(vote_count)
    winner_index = vote_count.index(winner_count)
    winner_name = candidate_list[winner_index]

    #Print the results to the terminal
    count = len(candidate_list)
    print("** Election Results **")
    print("=============================")
    print(f"Total Votes Counted: {total_votes}")
    print("=============================")
    print("Name  Vote_Count  Vote_%")
    for x in range(count):
        print(f"{candidate_list[x]}  {vote_count[x]}  {vote_percent[x]}")
    print("=============================")
    print("Election Winner: " + winner_name)

# Export the results to a text file

# Combined the 3 separate lists via zip
election_results = zip(candidate_list, vote_count, vote_percent)

# Specify the file to write to
output_path = os.path.join("analysis", "election_results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as output_csv:

    # Initialize csv.writer
    csv_writer = csv.writer(output_csv, delimiter=',')

    # Write the first row
    csv_writer.writerow(["** Election Results **"])

    # Write the second row
    csv_writer.writerow(["============================="])
    
    # Write the third row
    csv_writer.writerow(["Total Votes Counted: " + str(total_votes)])
    
     # Write the fourth row
    csv_writer.writerow(["============================="])
    
    # Write the fifth row
    csv_writer.writerow(["Name", "Vote_Count", "Vote_%"])
    
    # Write the sixth row
    csv_writer.writerows(election_results)
    
    # Write the seventh row
    csv_writer.writerow(["============================="])
    
    # Write the eighth row
    csv_writer.writerow(["Election Winner: " + winner_name])

