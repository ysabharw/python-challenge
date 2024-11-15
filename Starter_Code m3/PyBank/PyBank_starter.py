# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

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

