# Import Modules
import os
import csv

# Set path for the file
csv_path = os.path.join("Resources", "budget_data.csv")
                        
# Open the CSV
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Create 2 new lists that will contain the Month/Year and Profit/Losses information
    month_yr = []
    profit_loss = []
    
    # Read the header row first and store it to a variable
    csv_header = next(csv_reader)
        
    # Read each row of data after the header
    for row in csv_reader:
        
        # Populate the "month_yr" and "profit_loss" lists with the information from the file
        month_yr.append(row[0])
        profit_loss.append(int(row[1]))
        
    # Determine the total number of months included in the dataset   
    total_months = len(month_yr)
    
    # Calculate the net total amount of profit/losses over the entire period
    total_profits = round((sum(profit_loss)),2)

    # Create a new list that will contain the monthly changes in profit/losses
    change_profit_loss = []

    # Calculate the changes in profit/losses over the entire period and then update the "change_profit_loss" list
    for counter in range(1,total_months):
        data_current = profit_loss[counter]
        data_before = profit_loss[counter-1]
        delta = data_current - data_before
        change_profit_loss.append(delta)

    # Calculate the average of the monthly changes in profit/losses
    change_count = len(change_profit_loss)
    change_sum = sum(change_profit_loss)
    change_average = round((change_sum / change_count),2)

    # Determine the amount of the greatest decrease in profits
    greatest_decrease = min(change_profit_loss)

    # Determine the amount of the greatest increase in profits
    greatest_increase = max(change_profit_loss)

    # Determine the month/year of the greatest decrease in profits
    greatest_decrease_index = change_profit_loss.index(greatest_decrease)
    greatest_decrease_month = month_yr[greatest_decrease_index + 1]

    # Determine the month/year of the greatest increase in profits
    greatest_increase_index = change_profit_loss.index(greatest_increase)
    greatest_increase_month = month_yr[greatest_increase_index + 1]

    # Print the results to the terminal
    print("** Financial Analysis **")
    print("-----------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Net Total: ${total_profits}")
    print(f"Average  Change: ${change_average}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Export the results to a text file

# Specify the file to write to
output_path = os.path.join("analysis", "financial_analysis_results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as output_csv:

    # Initialize csv.writer
    csv_writer = csv.writer(output_csv, delimiter=',')

    # Write the first row
    csv_writer.writerow(["** Financial Analysis **"])

    # Write the second row
    csv_writer.writerow(["-----------------------------------------------"])
    
    # Write the third row
    csv_writer.writerow(["Total Months: " + str(total_months)])
    
     # Write the fourth row
    csv_writer.writerow(["Net Total: $"+ str(total_profits)])
    
    # Write the fifth row
    csv_writer.writerow(["Average  Change: $" + str(change_average)])
    
    # Write the sixth row
    csv_writer.writerow(["Greatest Increase in Profits: " + greatest_increase_month + " ($" + str(greatest_increase) + ")"])
    
      # Write the seventh row
    csv_writer.writerow(["Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(greatest_decrease) + ")"])