# Komna Lamboni
# 09/28/2024
# P1HW1
# Writing code that collects information from user, processes information collected and displays results to user.

print('--------Calculating Exponents--------\n')

# Get base value from the user
base = int(input('Enter an integer as the base value:'))

# Get exponent value from the user
exponent = int(input('Enter an integer as the exponent:'))

# Calculate the result
result = base ** exponent

# Print the result
print(base, 'raised to the power of', exponent, 'is', result, '!!!\n')


print('--------Addition and Subtraction-------\n')


# Get the starting integer from the user
start = int(input('Enter a starting integer:'))

# Get the integer to add from the user
to_add = int(input('Enter an integer to add:'))

# Get the integer to subtract from the user
to_subtract = int(input('Enter an integer to subtract:'))

# Perform the addition and subtraction
result = start + to_add - to_subtract

# Print the result
print(start, '+', to_add, '-', to_subtract, 'is equal to', result,)
