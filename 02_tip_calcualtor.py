# Intro
print("Welcome to the tip calculator")

# Bill amount?
bill = float(input("What was the total bill?"))

# Tip %?
tip = float(input("What % of tip would you like to give?"))

# People to split between?
split = float(input("How many people to split the bill?"))

# convert tip to % add it to total and then split it
t = tip * .01
total = bill + (t * bill)
s = total/split

# Round it to nearest 2 decimal
pay = round(s,2)
print(pay)