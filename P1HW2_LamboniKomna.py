# Komna Lamboni
# 09/28/2024
# P1HW2
# Creating a program that does some basic math on numbers that are entered. 

print('This program calculates and displays travel expenses\n')

# Ask the user to enter their budget
budget = float(input('Enter Budget: '))

# Ask the user to enter their travel destination
destination = input('Enter your travel destination: ')

# Ask the user for the amount they will spend on gas
gas_expense = int(input('How much do you think you will spend on gas? '))

# Ask the user for the amount they will spend on accommodation
accommodation_expense = float(input('Approximatively, how much will you need for accommodation/hotel? '))

# Ask the user for the amount they will spend on food
food_expense = float(input('Last, how much do you need for food? '))

print('\n--------------Travel Expenses---------------')

# Calculate the total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Calculate the remaining budget
remaining_budget = budget - total_expenses

# Display the results
print('Location:', destination)
print('Initial Budget:', budget)
print('\nFuel:', gas_expense)
print('Accomodation:', accommodation_expense)
print('Food:', food_expense)
print('\nRemaining Balance:', remaining_budget)

