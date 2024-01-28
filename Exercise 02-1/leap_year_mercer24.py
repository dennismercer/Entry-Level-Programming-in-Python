"""
Author: Dennis Mercer, mercer24@purdue.edu
Assignment: 02.1 - Leap Year
Date: 01/09/2024

Description:
    Prompt user to enter a year, then checks to see if the year is a leap year and output as request.

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
# Function, passing in the year to determin if it is a leapyear.
    def is_leap_year(year):
        if year % 100 == 0:
              return year % 400 == 0
        return year % 4 == 0

    # User is prompted to enter the year
    year = int(input("Enter a year: "))

    # Check if the year is a leap year
    if is_leap_year(year):
        print(f"The year {year} is a leap year.")
        print(f"February of {year} has 29 days.")
    else:
        print(f"The year {year} is not a leap year.")
        print(f"February of {year} has 28 days.")
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
