# Komna Lamboni
# 11/17/2024
# P5LAB
# Rebuilding P3LAB Assignment, turning it into a function called disperse_change.The user should be prompted to enter the amount of money they will put into the self-checkout machine (as a float). The program should then display the amount of dollars, quarters, dimes, nickels, and pennies required to make the change.

import random

def disperse_change(change):
    """
    Takes a float value for change owed and displays the amount of dollars, quarters,
    dimes, nickels, and pennies required to make the change.
    """
    # Convert the amount to an integer to work with pennies
    pennies = int(round(change * 100))
    
    # Calculate the number of each denomination
    dollars = pennies // 100
    pennies %= 100
    
    quarters = pennies // 25
    pennies %= 25
    
    dimes = pennies // 10
    pennies %= 10
    
    nickels = pennies // 5
    pennies %= 5

    # Output the results with proper capitalization and formatting
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")

def main():
    # Generate a random float value as the total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed:.2f}")

    # Prompt user to enter the amount they are paying
    amount_paid = float(input("How much cash will you put in the self-checkout? "))

    # Calculate the change
    change_owed = round(amount_paid - total_owed, 2)
    print(f"Change is: ${change_owed:.2f}\n")
    
    # Call the disperse_change function to handle change
    disperse_change(change_owed)

# Ensure the program runs when executed
if __name__ == "__main__":
    main()
