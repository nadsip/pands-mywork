# lab3.2.4-convert.py
#
# Author: Nadyarini
# Take input from the user
amount = float(input("Please enter an amount: "))

# Convert the amount to cents (absolute value)
amount_in_cents = int(abs(amount) * 100)

# Output the result
print(f"That amount in cents is: {amount_in_cents}")