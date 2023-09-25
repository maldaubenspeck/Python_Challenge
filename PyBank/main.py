import csv
from pathlib import Path

total_months = 0
total_profit_loss = 0
changed_profit_loss = []
previous_profit_loss = 0
dates = []
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ''
greatest_decrease_date = ''

#Open CSV Budget File
csvpath = Path("Resources/budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


 # Read the header row
    header = next(csvreader)
   
    for row in csvreader:
        # Extract the date and profit/loss
        date,profit_loss = row
        profit_loss = int(profit_loss)
        total_months += 1
       
        # Calculate the net total amount of profit/losses
        total_profit_loss += profit_loss
       
        # Calculate the change in profit/loss compared to the previous month
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changed_profit_loss.append(change)
            dates.append(date)
       
        # Update the previous profit/loss for the next iteration
        previous_profit_loss = profit_loss


# Calculate the average change in profit/losses
average_change = sum(changed_profit_loss) / len(changed_profit_loss)

# Find the greatest increase and decrease in profits
greatest_increase = max(changed_profit_loss)
greatest_decrease = min(changed_profit_loss)

# Find the corresponding dates for the greatest increase and decrease
greatest_increase_date = dates[changed_profit_loss.index(greatest_increase)]
greatest_decrease_date = dates[changed_profit_loss.index(greatest_decrease)]


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

output_file = 'Pybank_analysis.txt'

with open(output_file, 'w') as f:

    f.write("Financial Analysis\n")

    f.write("------------------\n")

    f.write(f"Total Months: {total_months}\n")

    f.write(f"Total Profit/Loss: ${total_profit_loss}\n")

    f.write(f"Average Change: ${average_change:.2f}\n")

    f.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")

    f.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

