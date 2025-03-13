# Use a while loop to keep prompting the user
while True:
    # Ask the user to enter a number
    number = int(input("Enter a number: "))
    
    # Check if the user entered -1 to exit
    if number == -1:
        print("Exiting the program.")
        break  # Exit the loop
    
    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")