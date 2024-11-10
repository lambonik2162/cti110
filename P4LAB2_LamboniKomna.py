# Lamboni, Komna
# 11/03/2024
# P4LAB2
# Writing codes that display information to users using loops.

run_program = "yes"

while run_program == "yes":
    # Ask the user to enter an integer
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue
    
    # Check if the integer is negative
    if number < 0:
        print("This program does not handle negative numbers.")
    else:
        # Display the multiplication table from 1 to 12
        for i in range(1, 13):
            print(f"{number} * {i} = {number * i}")
    
    # Ask the user if they want to run the program again
    run_program = input("\nWould you like to run the program again? ").strip().lower()
    if run_program != "yes":
        print("Exiting program...")

