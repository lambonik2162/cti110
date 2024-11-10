# Komna Lamboni
# 10/20/2024
# P3HW2
# Writing code to calculate employees' salaries based on regular time worked and overtime.

# Function calculate_pay:
    # Prompt for employee details
    # Input employee_name as String
    # Input hours_worked as Float
    #Input pay_rate as Float

# Initialize variables for calculations
   # Set overtime_hours to 0
   # Set overtime_pay to 0.0
   # Set regular_pay to 0.0

# Determine if overtime was worked
   # If hours_worked > 40 Then
        # Set overtime_hours to hours_worked - 40
        # Set overtime_pay to overtime_hours * pay_rate * 1.5
        # Set regular_hours to 40
   # Else
        # Set regular_hours to hours_worked
   # End If

# Calculate regular pay
    # Set regular_pay to regular_hours * pay_rate

# Calculate gross pay
   # Set gross_pay to regular_pay + overtime_pay

# Display formatted results
    # Print "-----------------------------------------------"
    # Print "Employee name:", employee_name
    # Print "Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"
    # Print "-----------------------------------------------------------------------------------------------------------"
    # Print hours_worked, pay_rate, overtime_hours, overtime_pay, regular_pay, gross_pay

# End Function

# Call calculate_pay function to execute

def calculate_pay():
    # Get employee details
    employee_name = input("Enter employee's name: ")
    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    # Initialize variables
    overtime_hours = 0
    overtime_pay = 0.0
    regular_pay = 0.0

    # Check if the employee worked overtime (more than 40 hours)
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        regular_hours = 40
    else:
        regular_hours = hours_worked
    
    # Calculate regular pay
    regular_pay = regular_hours * pay_rate

    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay

    # Display the formatted results
    print("\n-----------------------------------------------")
    print(f"Employee name:\t{employee_name}")
    print(f"\n{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")
    print(f"-----------------------------------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.1f}{pay_rate:<10.1f}{overtime_hours:<10.1f}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:.2f}")

# Call the function
calculate_pay()
