import math

# Ask the user to enter a percentage
percentage = float(input("Enter your percentage: "))

# Round up the percentage
rounded_percentage = math.ceil(percentage)

# Determine the grade based on the rounded percentage
if rounded_percentage >= 70:
    print(f"{rounded_percentage}% is a Distinction.")
elif rounded_percentage >= 60:
    print(f"{rounded_percentage}% is a Merit.")
elif rounded_percentage >= 50:
    print(f"{rounded_percentage}% is a Pass.")
else:
    print(f"{rounded_percentage}% is a Fail.")