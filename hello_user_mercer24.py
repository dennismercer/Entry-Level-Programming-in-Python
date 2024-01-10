"""
Author: Dennis Mercer, mercer24@purdue.edu
Assignment: 00.1 - Hello User
Date: 01/09/2024

Description: This program will ask the user for their name and store it in the variable {name}. In this case, it displays "What is your name? " and waits for the user to type something. 
Once the Enter key is pressed, the input text is assigned to the variable {name}. variable. This way, we can greet the user with their own name, making the greeting feel 
more personal.  Finally, the program will print a greeting using the user's name, using an f-string (formatted string literal) is used here to embed the variable “name” 
directly into the string.


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
    # prompt user for name
    name = input("What is your name? ")
    # print name with !
    print(f"Hello {name}!")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
