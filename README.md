# Python-challenge
Assignment 3

## Overview ##

This repository contains two Python scripts for data analysis:

1. **Budget Data Analysis** Analyzes financial records from a CSV file.
2. **Election Data Analysis** Analyzes election data from a CSV file.

## Budget Data Analysis ##

### Description ###

The budget_data analysis (main.py) script analyzes financial records from a CSV file (budget_data.csv). 
The dataset is composed of two columns: "Date" and "Profit/Losses". The script calculates the following values:

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

## Election Data Analysis ##

### Description ###

The election_data analysis (main2.py) script analyzes election data from a CSV file (election_data.csv). 
The dataset is composed of three columns: “Ballot ID", “County”, and “Candidate”. The script calculates the following values:

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote
