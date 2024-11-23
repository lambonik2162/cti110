# Komna Lamboni
# 11/22/2024
# P5HW
#  Creating a menu-driven program that allows users to play a math quiz by setting up functions that subtract and generate random numbers as the user keeps input incorrect values till the correct input is received. 

import random

def math_quiz():
    print("Welcome to Math Quiz")
    
    menu_option = ""
    while menu_option != "3":  # Main menu loop
        print("\nMAIN MENU")
        print("---------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        
        menu_option = input("Please choose one of the menu options: ").strip()
        
        if menu_option == "1" or menu_option == "2":  
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
            
            if menu_option == "1":  # Adding Random Numbers
                print(f"\n  {num1}")
                print(f"+ {num2}")
                correct_answer = num1 + num2
            elif menu_option == "2":  # Subtracting Random Numbers
                print(f"\n  {num1}")
                print(f"- {num2}")
                correct_answer = num1 - num2

            # Start the guessing game
            guesses = 0
            first_attempt = True
            user_guess = None
            
            while user_guess != correct_answer:
                try:
                    if first_attempt:
                        user_guess = int(input("Enter answer: "))
                        first_attempt = False
                    else:
                        user_guess = int(input("Try again: "))
                    guesses += 1
                    if user_guess < correct_answer:
                        print("Sorry, guess is too low.")
                    elif user_guess > correct_answer:
                        print("Sorry, guess is too high.")
                except ValueError:
                    print("Please enter a valid number.")
            
            print("Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {guesses}")
        
        elif menu_option == "3":  # Exit
            print("Thank you for playing...")
            print("Bye!!")
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    math_quiz()
