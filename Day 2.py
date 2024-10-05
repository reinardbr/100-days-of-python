#Tip calculator
print("Welcome to tip calculator!")
bill = float(input("What was the total bill?"))
tip = float(input("Whats the percentage tip you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
pay = round((bill * (1 + (tip / 100))) / people, 2)
print("Each person should pay: $" + str(pay))