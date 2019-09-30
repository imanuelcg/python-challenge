#import dependecies
import os
#module for reading CSV files
import csv 

# load the file to the program
election_file = os.path.join('Desktop','Bootcamp Projects','Python-Challenge','PyPoll','election_data.csv')

#using csv module to read data
with open(election_file, newline ='') as csvfile:
    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    #Declaring variable
    number_of_votes = 0
    khanV = 0
    correyV = 0
    liV = 0
    otooleyV = 0
    
    #templates
    print("Election Results")
    print("---------------------------")
    
    #to skip the header
    header = next(csvreader)
    
    #To loop through the rows
    for row in csvreader:
        
        #Counting the voter ID and store in a variable.
        number_of_votes += 1
        
        #Looping through the name, whenever the name is a match, it will add to the counter
        if row[2] == "Khan":
            khanV += 1
        elif row[2] == "Correy":
            correyV += 1
        elif row[2] == "Li":
            liV += 1
        elif row[2] == "O'Tooley":
            otooleyV += 1
            
#Making a dictionary from the list 
voters = ["Khan",'Correy","Li", "O'"Tooley"]
votes = ["khanV","CorreyV","liV","otooleyV"]


#zip candidate together
voters_and_votes = dict(zip(voters,votes))
key = max(voters_and_votes, key = voters_and_votes.get)

#calculating the percentage
khan_percentage = (khanV/number_of_votes) * 100
print(f"Khan: ({khan_percentage:.3f}%)({khanV})")

correy_percentage = (correyV/number_of_votes) * 100
print(f"Correy: ({correy_percentage:.3f}%)({correyV})")

li_percentage = (liV/number_of_votes) * 100
print(f"Li: ({li_percentage:.3f}%)({liV})")

otooley_percentage = (otooleyV/number_of_votes) * 100
print(f"O'Tooley: ({otooley_percentage:.3f}%)({otooleyV})")

print("---------------------------")
print(f"Winner: {key}")
                  

#Finding a path to out put the file
output_path = os.path.join('Desktop','Bootcamp Projects','Python-Challenge','PyPoll','Election_Output.txt')
    

with open(output_path, 'w', newline='') as txtfile:

    txtfile.write("Election Results")
    txtfile.write("\n")
    txtfile.write("---------------------------")
    txtfile.write("\n")
    txtfile.write(f"Khan: ({khan_percentage:.3f}%)({khanV})")
    txtfile.write("\n")
    txtfile.write(f"Correy: ({correy_percentage:.3f}%)({correyV})")  
    txtfile.write("\n")  
    txtfile.write(f"Li: ({li_percentage:.3f}%)({liV})")            
    txtfile.write("\n")      
    txtfile.write(f"O'Tooley: ({otooley_percentage:.3f}%)({otooleyV})")
    txtfile.write("\n")
    txtfile.write("---------------------------")
    txtfile.write("\n")
    txtfile.write(f"Winner: {key}")   
        
        
    
    
    
    

