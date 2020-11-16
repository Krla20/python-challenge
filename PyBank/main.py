# Correct path to the csv file on the scrip
# Budget_data.csv has two columns: 'Date' and "Profit/Losses"
# Python script that analyzes the records to calculate:
    # * The total number of months included in the dataset

    # * The net total amount of "Profit/Losses" over the entire period

    # * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

    # * The greatest increase in profits (date and amount) over the entire period

    # * The greatest decrease in losses (date and amount) over the entire period



# Import the .csv file
import os
import csv

# csvpath - directory
# csvpath = os.path.join("C:\\Users\\Owner\\Desktop\\Class_Material\\Homework to upload\\python_challenge\\PyBank\\Resources\\budget_data.csv")
csvpath = os.path.join('', 'PyBank','Resources', 'budget_data.csv')

# Creating variables
total_months = 0
total_net_amount_prof_los = 0
value = 0
change = 0
dates = []
profits = []

# Reading the cvs file
with open(csvpath) as csvfile:

    # Opening CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader) #my content=mydata=csvsreader - this one gives me the iterator

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    # for row in csvreader:
    #     print(row)

    #Reading the first row to track changes properly
    first_row = next(csvreader)
    total_months += 1
    total_net_amount_prof_los = int(first_row[1])
    value = int(first_row[1])

    #For loop to each row of data except after header and first row
    for row in csvreader:
        dates.append(row[0]) #keep track of the dates

        #calculate the change and add it to a list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

        #total of months
        total_months += 1
        #print(total_months)

        #total net amount "Profit/Losses" over the entire period
        total_net_amount_prof_los = total_net_amount_prof_los + int(row[1])
        #print(total_net_amount_prof_los)

        #greatest increase in profits (date and amount) over the entire period
        greatest_increase_profit = max(profits)
        #print(greatest_increase_profit)
        greatest_increase_index = profits.index(greatest_increase_profit)
        #print(greatest_index)
        greatest_increase_date = dates[greatest_increase_index]
        #print(greatest_increase_date)

        #greatest decrease in profits (date and amount) over the entire period
        greatest_decrease_profit = min(profits)
        #print(greatest_decrease_profit)
        greatest_decrease_index = profits.index(greatest_decrease_profit)
        #print(greatest_decrease_index)
        greatest_decrease_date = dates[greatest_decrease_index]

        #Average change in "Profit/Losses" over the entire period
        average_change = sum(profits) / len(profits)

#Print the Analysis
print("-" * 50)
print("Financial Analysis" )
print("-" * 50)
print(f"Total Months: {str(total_months)}")
print(f"Total Amount: ${str(total_net_amount_prof_los)}")
print(f"Average Change: ${str(round(average_change,2))}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${str(greatest_increase_profit)})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${str(greatest_decrease_profit)})")
print("-" * 50)

# # Set variable for output file
# output_file = os.path.join("","Analysis", "budget_data_final.csv")

# # Open the output file
# with open(output_file, "w", newline= "") as csvfile:

# # Exporting the file to a .csv file
# # output_file = open("budget_data_final.txt")

#     #Initialize csv writer
#     csvwriter = csv.writer(csvfile, delimiter=,",")

#     #Write rows in the file
#     csvwirter.writerow(["Total Months: "])

# open a (new) file to write
# output_path = os.path.join("C:\\Users\\Owner\\Desktop\\Class_Material\\Homework to upload\\python_challenge\\PyBank\\Analysis\\budget_data_output.txt")
output_path = os.path.join('', 'PyBank', 'Analysis', 'budget_data_output.txt')

# Write to the new txt file
with open(output_path, "w") as text_file:

    print(f'--------------------------------------------------', file = text_file)
    print(f'Financial Analysis', file = text_file)
    print(f'--------------------------------------------------', file = text_file)
    print(f'Total Months: {str(total_months)}', file = text_file)
    print(f'Total Amount: ${str(total_net_amount_prof_los)}', file = text_file)
    print(f'Average Change: ${str(round(average_change,2))}', file = text_file)
    print(f'Greatest Increase in Profits: {greatest_increase_date} (${str(greatest_increase_profit)})', file = text_file)
    print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${str(greatest_decrease_profit)})', file = text_file)
    print(f'--------------------------------------------------', file = text_file)