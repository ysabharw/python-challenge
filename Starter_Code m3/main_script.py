import os
import csv

def run_pybank():
    print("Running PyBank Analysis...")
    # Dynamically construct the file paths for PyBank
    pybank_dir = os.path.join(os.getcwd(), "Starter_Code m3", "PyBank")
    file_to_load = os.path.join(pybank_dir, "Resources", "budget_data.csv")
    file_to_output = os.path.join(pybank_dir, "analysis", "budget_analysis.txt")

    # Ensure the input file exists
    if not os.path.exists(file_to_load):
        print(f"Error: The file '{file_to_load}' does not exist.")
        return

    # Ensure output directory exists
    os.makedirs(os.path.dirname(file_to_output), exist_ok=True)

    # Initialize variables
    total_months = 0
    total_net = 0
    net_change_list = []
    months_list = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", float("inf")]

    # Process the CSV
    with open(file_to_load) as financial_data:
        reader = csv.reader(financial_data)
        header = next(reader)  # Skip header

        first_row = next(reader)
        total_months += 1
        total_net += int(first_row[1])
        previous_net = int(first_row[1])

        for row in reader:
            total_months += 1
            total_net += int(row[1])
            net_change = int(row[1]) - previous_net
            net_change_list.append(net_change)
            months_list.append(row[0])
            previous_net = int(row[1])

            if net_change > greatest_increase[1]:
                greatest_increase = [row[0], net_change]
            if net_change < greatest_decrease[1]:
                greatest_decrease = [row[0], net_change]

    average_change = sum(net_change_list) / len(net_change_list)

    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Losses: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

    print(output)

    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)


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
