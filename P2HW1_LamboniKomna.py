# Komna Lamboni
# 10/13/2024
# P2HW1
# Creating a program that does some basic math on numbers that are entered.
# Ask the user to enter their budget
budget = float(input('Enter Budget: $'))
# Ask the user to enter their travel destination
destination = input('Enter your travel destination: ')
# Ask the user for the amount they will spend on gas
gas_expense = float(input('How much do you think you will spend on gas? $'))
# Ask the user for the amount they will spend on accommodation
accommodation_expense = float(input('Approximately, how much will you need for accommodation/hotel? $'))
# Ask the user for the amount they will spend on food
food_expense = float(input('Last, how much do you need for food? $'))
print('\n--------------Travel Expenses---------------')
# Calculate the total expenses
total_expenses = gas_expense + accommodation_expense + food_expense
# Calculate the remaining budget
remaining_budget = budget - total_expenses
# Display the results with formatted output
print(f'{"Location:":<25} {destination}')
print(f'{"Initial Budget:":<25} ${budget:,.2f}')
print(f'{"Fuel:":<25} ${gas_expense:,.2f}')
print(f'{"Accommodation:":<25} ${accommodation_expense:,.2f}')
print(f'{"Food:":<25} ${food_expense:,.2f}')
print('-----------------------------------------')
print(f'\n{"Remaining Balance:":<25} ${remaining_budget:,.2f}')
