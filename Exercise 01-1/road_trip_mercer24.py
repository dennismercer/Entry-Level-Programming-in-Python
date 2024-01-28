"""
Author: Dennis Mercer, mercer24@purdue.edu
Assignment: 01.1 - Road Trip
Date: 01/15/2024

Description:
    Prompt User to input different variables (price, distance and MPG) for a formual to determine the cost of a road trip.

Contributors:
    None, I have several years of experience with coding in Python, C++, Java, Javascript and other languages.  I have also taught Python for Pentesters for the US Army.

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

# Main function to run the program. Prompt the user for input, calculates the fuel cost, and displays the result.
def main():
    print("Road trip fuel cost estimator:")

    distance = float(input("  How far away is your destination (miles)? "))
    price = float(input("  What is the average price of gas (dollars per gallon)? "))
    mpg = float(input("  What is the fuel efficiency of your vehicle (mpg)? "))

    # Calculate the total fuel cost for the round trip.
    cost = int((2 * distance) * (price / mpg))
    # Print a blank line to obtain the required "six lines" per gradescope
    print()
    # Display the calculated fuel cost to the user.
    print(f"The fuel cost for this trip is approximately ${cost}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
