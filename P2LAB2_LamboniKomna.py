# Komna Lamboni
# 10/06/2024
# P2LAB2
# How to write code that uses a dictionary to store user input and displays output to the user.

# Create the dictionary with key-value pairs
vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Create a variable that holds all the keys in the dictionary
keys = vehicle_mpg.keys()

# Print the variable that holds the keys
print("vehicle_mpg:", list(keys))

# Prompt the user to enter one of the vehicles from the dictionary
vehicle = input("Enter a vehicle to see its mpg: ")

# Display the mpg for the vehicle that the user entered
if vehicle in vehicle_mpg:
    mpg = vehicle_mpg[vehicle]
    print(f"The {vehicle} gets {mpg} mpg.")
    
    # Prompt the user to enter the number of miles they will drive the vehicle
    miles = float(input(f"How many miles will you drive the {vehicle}? "))
    
    # Calculate the gallons of gas needed
    gallons_needed = miles / mpg
    
    # Display the gallons of gas needed, rounded to two decimal places
    print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")
else:
    print("The vehicle you entered is not in the list.")
