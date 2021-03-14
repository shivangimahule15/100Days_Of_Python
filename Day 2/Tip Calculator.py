#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# print("Welcome to the Tip Calculator")
# bill=input("What was the total bill? $")
# tip=input("What percentage of tip you would like to give? 10, 12 or 15?")
# split=input("How many people to split the bill?")
# bill_float=float(bill)
# tip_float=float(tip)
# split_float=float(split)
# per_tip=(bill_float*(tip_float/100))
# main_bill=(bill_float+per_tip)
# result=round(main_bill/split_float,2)

# print(f"Each person should pay: ${result}")

print("Welcome to Tip Calculator")
total_bill = float( input("What was the total bill? $") )
tip_percentage = int( input("What percentage of tip would you like to give? 10, 12, or 15? ") )
number_of_people = int( input("How many people to split the bill? ") )

total_bill += total_bill * ( tip_percentage / 100 )

individual_bill_amount = round( total_bill / number_of_people , 2 )

print(f"Each person should pay: ${ individual_bill_amount }")



