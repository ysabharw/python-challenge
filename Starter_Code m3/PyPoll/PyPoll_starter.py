# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

def run_pypoll():
    print("Running PyPoll Analysis...")
    # Dynamically construct the file paths for PyPoll
    pypoll_dir = os.path.join(os.getcwd(), "Starter_Code m3", "PyPoll")
    file_to_load = os.path.join(pypoll_dir, "Resources", "election_data.csv")
    file_to_output = os.path.join(pypoll_dir, "analysis", "election_analysis.txt")

    # Ensure the input file exists
    if not os.path.exists(file_to_load):
        print(f"Error: The file '{file_to_load}' does not exist.")
        return

    # Ensure output directory exists
    os.makedirs(os.path.dirname(file_to_output), exist_ok=True)

    # Initialize variables
    total_votes = 0
    candidate_options = []
    candidate_votes = {}
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    # Process the CSV
    with open(file_to_load) as election_data:
        reader = csv.reader(election_data)
        header = next(reader)  # Skip header

        for row in reader:
            total_votes += 1
            candidate_name = row[2]
            if candidate_name not in candidate_options:
                candidate_options.append(candidate_name)
                candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] += 1

    # Generate output
    with open(file_to_output, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes}\n"
            f"-------------------------\n"
        )
        print(election_results, end="")
        txt_file.write(election_results)

        for candidate in candidate_votes:
            votes = candidate_votes[candidate]
            vote_percentage = (votes / total_votes) * 100
            if votes > winning_count:
                winning_candidate = candidate
                winning_count = votes
                winning_percentage = vote_percentage
            candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
            print(candidate_results, end="")
            txt_file.write(candidate_results)

        winning_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count}\n"
            f"Winning Percentage: {winning_percentage:.3f}%\n"
            f"-------------------------\n"
        )
        print(winning_summary)
        txt_file.write(winning_summary)


# Run both PyBank and PyPoll
if __name__ == "__main__":
    run_pybank()
    print("\n")
    run_pypoll()
