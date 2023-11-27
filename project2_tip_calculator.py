print("Welcome to the tip calculator \n")


amount = input("What was the total bill? ")
tip = input("what percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

new_amount = int(amount)
new_tip = int(tip)
new_split = int(split)

Amount_2B_paid = (new_amount + (new_amount*(new_tip/100)))/new_split
# new_amount_2B = float(Amount_2B_paid)
print(f"Each person should pay: {Amount_2B_paid}")