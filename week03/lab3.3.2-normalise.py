# This program reads in a string and strips
# any leading or trailing spaces.
# It then outputs the lengths of the original string
# and the normalised one
#
# Author: Nadyarini

rawString = input("please enter a string:") 
normalisedString = rawString.strip().lower()

lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)

print(f"That String normalised is :{normalisedString}")
print(f"we reduced the input string from {lenghtOfRawString} to {lenghtOfNormalised} characters")
