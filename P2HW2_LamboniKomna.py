# Komna Lamboni
# 10/13/2024
# P2HW2
# Designing programs for students grades input.

# Initialize an empty list to store the grades
results = []
# Ask the user to enter grades for each module
for i in range(1, 7):
 grade = float(input(f'Enter grade for Module {i}: '))
 
results.append(grade)
# Calculate the required statistics
lowest_grade = min(results)
highest_grade = max(results)
sum_of_grades = sum(results)
average_grade = sum_of_grades / len(results)
# Display the results with formatted output
print('\n--------------Grade Summary---------------')
print(f'{"Lowest Grade:":<20} {lowest_grade:.2f}')
print(f'{"Highest Grade:":<20} {highest_grade:.2f}')
print(f'{"Sum of Grades:":<20} {sum_of_grades:.2f}')
print(f'{"Average:":<20} {average_grade:.2f}')
print('------------------------------------------')
