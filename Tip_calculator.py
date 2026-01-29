#1 first we need to print the project name
print("Welcome To Tip Calculator")
#2 we need to ask the user what the total of the bill
bill = float(input("What is the total bill?\n"))
#3 we need to ask the user what the percent tip would you like to give and add the persent to the bill
tip = float(input("how much percent tip would you like to give?10,12,15\n"))
total_bill = bill * tip/100 + bill
#4we need to ask the user how many person to divide the total by people
people = int(input("How many people to split the bill?\n"))
#5  we need to show the result
total = float(total_bill) / people
print(f"Each person should pay: {total}")
