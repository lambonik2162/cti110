# Komna Lamboni
# 11/10/2024
# P4HW1
# Rebuilding P2HW2 Assignment using loops to display score average with its corresponding grade letter.

# Pseudocode:
# 1. Define a function `get_score_count` to prompt the user for the number of scores to be entered:
#    - Loop until a valid integer greater than 0 is entered.
#    - If the input is invalid, display an error message and re-prompt.
#    - Return the valid count.

# 2. Define a function `get_valid_score` that takes `score_number` as an argument to prompt for an individual score:
#    - Loop until a valid score between 0 and 100 is entered.
#    - Prompt user to enter the score with format "Enter score #N:".
#    - If the score is outside the range 0-100, display an error message and re-prompt with "Enter score #N again:".
#    - Return the valid score.

# 3. Define a function `calculate_average` that takes a list of scores as an argument:
#    - Identify the lowest score in the list.
#    - Create a modified list that is a copy of the original scores list with the lowest score removed.
#    - Calculate the average of the scores in the modified list.
#    - Return the lowest score, modified list, and calculated average.

# 4. Define a function `determine_grade` that takes the average score as an argument:
#    - Determine the letter grade based on the average score:
#        - 'A' for 90 or above
#        - 'B' for 80 to 89
#        - 'C' for 70 to 79
#        - 'D' for 60 to 69
#        - 'F' for below 60
#    - Return the letter grade.

# 5. Define the main function `main` to execute the program:
#    - Call `get_score_count` to get the number of scores.
#    - Initialize an empty list to store the scores.
#    - Loop to collect the scores based on the count:
#        - Call `get_valid_score` with the current score number to get a valid score and add it to the list.
#    - Call `calculate_average` with the scores list to get:
#        - The lowest score, modified list (with the lowest score removed), and the average.
#    - Call `determine_grade` with the average to obtain the letter grade.
#    - Display results formatted as follows:
#        - Lowest Score, Modified List, Scores Average, and Grade.

# 6. Run the `main` function if the script is executed directly.


def get_score_count():
    while True:
        try:
            count = int(input("How many scores do you want to enter? "))
            if count > 0:
                return count
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_valid_score(score_number):
    while True:
        try:
            score = float(input(f"Enter score #{score_number}: "))
            if 0 <= score <= 100:
                return score
            else:
                print("\nINVALID Score entered!!!!")
                print("Score should be between 0 and 100")
                # Displaying only "Enter score #N again:" without additional input prompt
                print(f"Enter score #{score_number} again:", end=" ")
        except ValueError:
            print("\nInvalid input. Please enter a numeric score.")

def calculate_average(scores):
    lowest_score = min(scores)
    modified_scores = scores.copy()
    modified_scores.remove(lowest_score)
    average_score = sum(modified_scores) / len(modified_scores)
    return lowest_score, modified_scores, average_score

def determine_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    score_count = get_score_count()
    scores = []
    
    for i in range(1, score_count + 1):
        score = get_valid_score(i)
        scores.append(score)
    
    lowest_score, modified_scores, average_score = calculate_average(scores)
    grade = determine_grade(average_score)
    
    # Displaying the results in the requested format
    print("\n----------------Results----------------")
    print("Lowest Score   :", f"{lowest_score:.1f}")
    print("Modified List  :", modified_scores)
    print("Scores Average :", f"{average_score:.2f}")
    print("Grade          :", grade)
    print("--------------------------------------")

if __name__ == "__main__":
    main()
