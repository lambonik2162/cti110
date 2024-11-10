# Komna Lamboni
# 11/10/2024
# P4HW2
# Rebuilding P3HW2 Assignment using loops to calculate gross pay for multiple employees, determined by the user, and the total amount paid for overtime, the total amount paid for regular pay, and the total amount paid for all employees.
# Pseudocode

    # - Calculate overtime_hours as the maximum of 0 or (hours_worked - 40)
    # - Calculate regular_hours as the minimum of hours_worked or 40
    # - Calculate regular_pay as regular_hours * pay_rate
    # - Calculate overtime_pay as overtime_hours * (pay_rate * 1.5)
    # - Calculate gross_pay as regular_pay + overtime_pay
    # Return regular_pay, overtime_pay, gross_pay, and overtime_hours
    # - Initialize total_employees to 0
    # - Initialize total_overtime_pay to 0.0
    # - Initialize total_regular_pay to 0.0
    # - Initialize total_gross_pay to 0.0
    # - Display prompt for employee name or "Done" to terminate
    # - While employee name is NOT "Done":
    #     - Ask for hours worked and pay rate
    #     - Call calculate_pay function to get regular, overtime pay, and gross pay
    #     - Display employee pay details in formatted output
    #     - Update totals (total_employees, total_overtime_pay, total_regular_pay, total_gross_pay)
    #     - Prompt for next employee name
    # - After exiting loop, display summary of totals (total number of employees, overtime pay, regular pay, and gross pay)

def calculate_pay(hours_worked, pay_rate):
    overtime_hours = max(0, hours_worked - 40)
    regular_hours = min(hours_worked, 40)
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
    return regular_pay, overtime_pay, gross_pay, overtime_hours

def main():
    total_employees = 0
    total_overtime_pay = 0.0
    total_regular_pay = 0.0
    total_gross_pay = 0.0

    # Initial prompt to enter employee name
    employee_name = input("Enter employee's name or \"Done\" to terminate: ")

    while employee_name.lower() != "done":
        # Gather hours worked and pay rate
        hours_worked = float(input(f"How many hours did {employee_name} work? "))
        pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

        # Calculate pay details using the calculate_pay function
        regular_pay, overtime_pay, gross_pay, overtime_hours = calculate_pay(hours_worked, pay_rate)

        # Display formatted pay details for the current employee
        print(f"\nEmployee name: {employee_name}")
        print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
        print("-" * 78)
        print(f"{hours_worked:<14.1f}{pay_rate:<12.2f}{overtime_hours:<11.1f}${overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:<10.2f}\n")

        # Update totals
        total_employees += 1
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay

        # Prompt for the next employee name
        employee_name = input("Enter employee's name or \"Done\" to terminate: ")

    # Display summary totals
    print(f"\nTotal number of employees entered: {total_employees}")
    print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
    print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
    print(f"Total gross pay for all employees: ${total_gross_pay:.2f}")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()

