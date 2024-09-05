import csv

def print_and_write(output, file):
    print(output)
    file.write(output + '\n')

# My variables
total_months = 0
net_total = 0
previous_profit_losses = 0
changes = []
dates = []

# Pathing my CSV file
with open('C:/Users/Cloud/LearnPython/Python-Challenge/Python-challenge/PyBank/Resources/budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    for row in reader:
        date = row[0]
        profit_losses = int(row[1])
        
        
        total_months += 1
        
        # Calculate the net total amount of "Profit and Losses"
        net_total += profit_losses
        
        # Calculate the changes in "Profit and Losses"
        if total_months > 1:
            change = profit_losses - previous_profit_losses
            changes.append(change)
            dates.append(date)
        
        # Update the previous "Profit and Losses"
        previous_profit_losses = profit_losses

# Calculate the average change
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# txt file of result
with open('budget_analysis.txt', 'w') as txt_file:
    print_and_write("Financial Analysis", txt_file)
    print_and_write("----------------------------", txt_file)
    print_and_write(f"Total Months: {total_months}", txt_file)
    print_and_write(f"Total: ${net_total}", txt_file)
    print_and_write(f"Average Change: ${average_change:.2f}", txt_file)
    print_and_write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})", txt_file)
    print_and_write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})", txt_file)
