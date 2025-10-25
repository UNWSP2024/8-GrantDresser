# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).

##
# Program 3: Capital Quiz
# Grant Dresser
# 10/24/2025
##

import random

def main():
    capitals = {
        "France" : "Paris",
        "Germany" : "Berlin",
        "Japan" : "Tokyo",
        "Italy" : "Rome",
        "Canada" : "Ottawa",
        "United States" : "Washington, D.C.",
        "Mexico" : "Mexico City",
        "Egypt" : "Cairo"
    }

    correct_count = 0
    incorrect_count = 0

    countries = list(capitals.keys())

    print ("Welcome to the Capitals of the World Quiz!")
    print ("Type 'exit' to finish the quiz at any time.")

    while True:
        country = random.choice(countries)
        answer = input(f"What is the capital of {country}? ")

        if answer.lower() == 'exit':
            break

        if answer.strip().lower() == capitals[country].lower():
            print("Correct!!!")
            correct_count += 1
        else:
            print(f"Incorrect. The capital of {country} is {capitals[country]}.")
            incorrect_count += 1

    print("Quiz finished!")
    print(f"Correct answers: {correct_count}")
    print(f"Incorrect answers: {incorrect_count}")
    print("Thanks for playing! Play again to improve your score!")

main()