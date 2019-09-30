#import dependecies
import os
#module for reading CSV files
import csv 


#find the file to load
budget_file = os.path.join('Desktop','Bootcamp Projects','Python-Challenge','PyBank','budget_data.csv')

#using csv module to read data
with open(budget_file, newline ='') as csvfile:
    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    #templates
    print("Financial Analysis")
    print("---------------------------")
    
    #to skip the header
    header = next(csvreader)
    
    #Empty list to append rows
    total_months = []
    total_profits = []
    x_profit_change = []
    
    #To loop through all the rows in the csvreaders.
    for row in csvreader:
        
        
        #looping and storing information to the list from the csv file
        total_months.append(row[0])
        total_profits.append(int(row[1]))
    
    #To find count the number of months
    print(f"Total Months: {len(total_months)}")
    
    
    #find the total of the profit/loss
    print(f"Total: ${sum(total_profits)}")
    
    #Looping throug the profits
    for i in range(len(total_profits)-1):
        
        #The average of the changes in "Profit/Losses" over the entire period
        x_profit_change.append(total_profits[i+1] - total_profits[i])
    print(f"Average Change: ${round(sum(x_profit_change)/len(x_profit_change),2)}")
    
    #The greatest increase in profits (date and amount) over the entire period
    increase_in_profits = max(x_profit_change)
    decrease_in_profits = min(x_profit_change)
    
    #The greatest decrease in losses (date and amount) over the entire period
    max_month = x_profit_change.index(max(x_profit_change)) + 1
    min_month = x_profit_change.index(min(x_profit_change)) + 1
    
    print(f"Greatest Increase in Profits: {total_months[max_month]} (${(str(increase_in_profits))})")
    print(f"Greatest Increase in Profits: {total_months[min_month]} (${(str(decrease_in_profits))})")
    
    #Finding a path to out put the file
    output_path = os.path.join('Desktop','Bootcamp Projects','Python-Challenge','PyBank','Bank_Output.txt')
    

    with open(output_path, 'w', newline='') as txtfile:
        #writing the data to the output
        txtfile.write("Financial Analysis")
        txtfile.write("\n")
        txtfile.write("---------------------------")
        txtfile.write("\n")
        txtfile.write(f"Total Months: {len(total_months)}")
        txtfile.write("\n")
        txtfile.write(f"Total: ${sum(total_profits)}")
        txtfile.write("\n")
        txtfile.write(f"Average Change: ${round(sum(x_profit_change)/len(x_profit_change),2)}")
        txtfile.write("\n")
        txtfile.write(f"Greatest Increase in Profits: {total_months[max_month]} (${(str(increase_in_profits))})")
        txtfile.write("\n")
        txtfile.write(f"Greatest Increase in Profits: {total_months[min_month]} (${(str(decrease_in_profits))})")
        txtfile.write("\n")
        
        
        
   
        
        
        
    
    
    
    

