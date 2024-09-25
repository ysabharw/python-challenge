# python-challenge


## Overview

This repository contains Python scripts for analyzing financial data (PyBank) and election results (PyPoll). These scripts perform tasks that are typically done using Excel but have been implemented in Python for better efficiency and handling of large datasets.

## Project Structure

The project consists of two main directories:

1. **PyBank** - Python script to analyze a company's financial records.
2. **PyPoll** - Python script to analyze election results from a dataset of votes.

### Files

#### PyBank:

* `PyBank_starter.py`: The Python script that performs the financial analysis.
* `budget_data.csv`: The input dataset with Date and Profit/Losses columns.
* `pybank.txt`: The output file that contains the analysis results.

#### PyPoll:

* `PyPoll_starter.py`: The Python script that performs the election analysis.
* `election_data.csv`: The input dataset with Voter ID, County, and Candidate columns.
* `pypol.txt`: The output file that contains the election results.

## PyBank Analysis

The **PyBank** script analyzes financial records and provides:

* The total number of months included in the dataset.
* The net total amount of Profit/Losses.
* The average change in Profit/Losses.
* The greatest increase in profits (date and amount).
* The greatest decrease in losses (date and amount).



OUTPUT : Financial Analysis

Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Losses: Feb-14 ($-1825558)


## PyPoll Analysis

The **PyPoll** script processes the election dataset and calculates:

* The total number of votes cast.
* A complete list of candidates who received votes.
* The percentage of votes each candidate won.
* The total number of votes each candidate won.
* The winner of the election based on popular vote.

OUTPUT : Election Results

Total Votes: 369711

Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)

Winner: Diana DeGette
Winning Vote Count: 272892
Winning Percentage: 73.812%

## Resources Used

During the development of these scripts, the following resources were helpful:

1. **Python Documentation** : [https://docs.python.org/3/](https://docs.python.org/3/)
2. **Stack Overflow** :

* Issue: FileNotFoundError or CSV handling
  * Solution: [https://stackoverflow.com/questions/24282743/file-not-found-error](https://stackoverflow.com/questions/24282743/file-not-found-error)
* Issue: Calculating changes in lists
  * Solution: [https://stackoverflow.com/questions/18072760](https://stackoverflow.com/questions/18072760)

3. **Pandas Documentation** (optional): [https://pandas.pydata.org/]()

4. **Real Python Tutorials** :

* [Reading and Writing CSV Files in Python]()
