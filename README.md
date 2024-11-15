

# Python Challenge

## Overview

This repository contains Python scripts for analyzing financial data (**PyBank**) and election results (**PyPoll**). These scripts perform tasks typically done using Excel but have been implemented in Python for improved efficiency and scalability with large datasets. Additionally, a collective script has been added to simplify running both analyses.

---

## Project Structure

The project consists of two main directories:

1. **PyBank** - Python script to analyze a company's financial records.
2. **PyPoll** - Python script to analyze election results from a dataset of votes.

---

## Files

### **PyBank**

- **`PyBank_starter.py`**: Python script that performs the financial analysis.
- **`Resources/budget_data.csv`**: Input dataset containing `Date` and `Profit/Losses` columns.
- **`analysis/budget_analysis.txt`**: Output file with the analysis results.

### **PyPoll**

- **`PyPoll_starter.py`**: Python script that performs the election analysis.
- **`Resources/election_data.csv`**: Input dataset containing `Voter ID`, `County`, and `Candidate` columns.
- **`analysis/election_analysis.txt`**: Output file with the election results.

### **Collective Script**

- **`main_script.py`**: A unified script that runs both the PyBank and PyPoll analyses. It dynamically handles paths, checks for missing files, and ensures output directories exist.

---

## PyBank Analysis

The **PyBank** script analyzes financial records and provides:

1. The total number of months included in the dataset.
2. The net total amount of Profit/Losses.
3. The average change in Profit/Losses.
4. The greatest increase in profits (date and amount).
5. The greatest decrease in losses (date and amount).

**Sample Output**:

```
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: -$8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Losses: Feb-14 ($-1825558)
```

---

## PyPoll Analysis

The **PyPoll** script processes the election dataset and calculates:

1. The total number of votes cast.
2. A complete list of candidates who received votes.
3. The percentage of votes each candidate won.
4. The total number of votes each candidate won.
5. The winner of the election based on the popular vote.

**Sample Output**:

```
Election Results
-------------------------
Total Votes: 369711
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272892
Winning Percentage: 73.812%
```

---

## Enhancements

### **Dynamic Path Handling**

- Both scripts now use `os.path` to dynamically handle file paths. This makes the project more portable and ensures compatibility across different operating systems.

### **Error Handling**

- Added checks to ensure the input files exist before attempting to read them. If a file is missing, an appropriate error message is displayed.

### **Output Directory Management**

- The scripts ensure the `analysis` directory exists before writing the output files.

### **Unified Script**

- The `main_script.py` script allows users to run both PyBank and PyPoll analyses in a single execution, simplifying workflow management.

---

## Resources Used

The following resources were helpful during development:

1. **Python Documentation**: [https://docs.python.org/3/](https://docs.python.org/3/)
2. **Stack Overflow**:
   - **Issue**: FileNotFoundError or CSV handling**Solution**: [File Not Found Error](https://stackoverflow.com/questions/24282743/file-not-found-error)
   - **Issue**: Calculating changes in lists
     **Solution**: [Calculating List Changes](https://stackoverflow.com/questions/18072760)
3. **Pandas Documentation (optional)**: [https://pandas.pydata.org/](https://pandas.pydata.org/)
4. **Real Python Tutorials**:
   - **[Reading and Writing CSV Files in Python](https://realpython.com/python-csv/)**

---

## How to Run the Scripts

### **Running Individual Scripts**

1. **PyBank**:
   ```bash
   cd Starter_Code\ m3/PyBank
   python PyBank_starter.py
   ```
2. **PyPoll**:
   ```bash
   cd Starter_Code\ m3/PyPoll
   python PyPoll_starter.py
   ```

### **Running the Unified Script**

1. Navigate to the project’s root directory:
   ```bash
   cd /path/to/python-challenge
   ```
2. Run the unified script:
   ```bash
   python main_script.py
   ```

The results will be printed to the terminal and saved to the respective `analysis` directories.

---
