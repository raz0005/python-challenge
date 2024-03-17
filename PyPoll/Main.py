import csv

# Function to analyze election data
def analyze_election_data(file_path):
    # Initialize variables to store election analysis results
    total_votes = 0
    candidates_votes = {}
    winner = {"name": "", "votes": 0}

    # Read the CSV file
    with open(file_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)  # Skip header row

        # Iterate through each row in the CSV file
        for row in csvreader:
            # Extract candidate name from the row
            candidate_name = row[2]

            # Count total votes
            total_votes += 1

            # Update candidate's vote count
            if candidate_name in candidates_votes:
                candidates_votes[candidate_name] += 1
            else:
                candidates_votes[candidate_name] = 1

    # Calculate the percentage of votes each candidate won
    for candidate, votes in candidates_votes.items():
        percentage = (votes / total_votes) * 100
        candidates_votes[candidate] = {"votes": votes, "percentage": percentage}

        # Update the winner
        if votes > winner["votes"]:
            winner["name"] = candidate
            winner["votes"] = votes

    return total_votes, candidates_votes, winner

# Main function
def main():
    file_path = "PyPoll/Resources/election_data.csv"
    total_votes, candidates_votes, winner = analyze_election_data(file_path)

    # Print the election analysis results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, data in candidates_votes.items():
        print(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})")
    print("-------------------------")
    print(f"Winner: {winner['name']}")
    print("-------------------------")

    # Write the election analysis results to a text file
    with open("election_results.txt", "w") as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Total Votes: {total_votes}\n")
        txtfile.write("-------------------------\n")
        for candidate, data in candidates_votes.items():
            txtfile.write(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Winner: {winner['name']}\n")
        txtfile.write("-------------------------\n")

    print("Election results have been written to election_results.txt")

if __name__ == "__main__":
    main()
