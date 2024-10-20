# Komna Lamboni
# 10/20/2024
# P3LAB
# Writing code that displays information to users.

def calculate_change(amount):
    # Remove the dollar sign if present and convert the amount to a float
    amount = float(amount.replace('$', ''))
    # Convert the amount to an integer to work with pennies
    pennies = int(round(amount * 100))
    
    # Calculate the number of each denomination
    dollars = pennies // 100
    pennies %= 100
    
    quarters = pennies // 25
    pennies %= 25
    
    dimes = pennies // 10
    pennies %= 10
    
    nickels = pennies // 5
    pennies %= 5
    
    # Output the results
    if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
        print("No change")
    else:
        if dollars > 0:
            print(f"{dollars} {'dollar' if dollars == 1 else 'dollars'}")
        if quarters > 0:
            print(f"{quarters} {'quarter' if quarters == 1 else 'quarters'}")
        if dimes > 0:
            print(f"{dimes} {'dime' if dimes == 1 else 'dimes'}")
        if nickels > 0:
            print(f"{nickels} {'nickel' if nickels == 1 else 'nickels'}")
        if pennies > 0:
            print(f"{pennies} {'penny' if pennies == 1 else 'pennies'}")

# Example usage:
amount = input("Enter the amount of money as a float: ")
calculate_change(amount)

