"""
Author: Dennis Mercer, mercer24@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 01/27/2024

Description:
    Prompt user to enter a color which should be only red, green or black.  Then return if the color is red, green or black based on the number
    entered by the user. If the number is not between 0-36, return "Invalid Input!"

Contributors:
    None

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""


def main():
    # Prompt the user to enter a number.  In this case we should have also specified to the user to enter the number between 0-36
    pocket_number = int(input("Please choose a pocket number: "))

    # Now to check if the number is between 0-36, if not print Invalid Input, else check the number and print the pocket color.
    if pocket_number < 0 or pocket_number > 36:
        print("  Invalid Input!")
    elif pocket_number == 0:
        print("  Pocket number 0 is green.")
    elif 1 <= pocket_number <= 10:
        color = "red" if pocket_number % 2 == 1 else "black"
        print(f"  Pocket number {pocket_number} is {color}.")
    elif 11 <= pocket_number <= 18:
        color = "red" if pocket_number % 2 == 0 else "black"
        print(f"  Pocket number {pocket_number} is {color}.")
    elif 19 <= pocket_number <= 28:
        color = "red" if pocket_number % 2 == 1 else "black"
        print(f"  Pocket number {pocket_number} is {color}.")
    elif 29 <= pocket_number <= 36:
        color = "red" if pocket_number % 2 == 0 else "black"
        print(f"  Pocket number {pocket_number} is {color}.")
    else:
        print("Invalid Input!")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
