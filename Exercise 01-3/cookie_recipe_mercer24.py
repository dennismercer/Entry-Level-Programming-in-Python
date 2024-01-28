"""
Author: Dennis Mercer, mercer24@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 01/15/2024

Description:
    Prompt user to enter the number of cookies that they want to make and then displays the ammount of each ingredient is needed to make that number of cookies.

Contributors:
   I used the python offical documation site at https://docs.python.org/3/library/string.html  
   This time I was confused on the format of the output string.  I was very confused based on the test fail message.
   At first I tried to adjust the spaces inside the output and that did not work.  I checked the assignment and noticed that the output requirement was for a width of 10
   and the float set to 2 for precision.  This one got me for a bit.  

My contributor(s) helped me:
    [X] understand the assignment expectations without
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
    # Ask user to input the number of cookies they want to make
    cookies = int(input("How many cookies do you want to make? "))

    # Ingredients needed to produce 48 cookies and this will be used to adjust based on the user's input for a different number of cookies
    butter_per_cookie = 1.25 / 48
    sugar_per_cookie = 1.5 / 48
    flour_per_cookie = 2.5 / 48

    # Calculate the amount needed for the number of cookies the user inputted 
    butter_needed = butter_per_cookie * cookies
    sugar_needed = sugar_per_cookie * cookies
    flour_needed = flour_per_cookie * cookies

    # Display the results with proper indenting found at https://docs.python.org/3/library/string.html
    print(f"To make {cookies:,} cookies, you will need:")
    print(f"{butter_needed:10,.2f} cups of butter")
    print(f"{sugar_needed:10,.2f} cups of sugar")
    print(f"{flour_needed:10,.2f} cups of flour")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
