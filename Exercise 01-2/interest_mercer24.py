"""
Author: Dennis Mercer, mercer24@purdue.edu
Assignment: 01.2 - Interest
Date: 01/15/2024

Description:
    Prompts the user to enter an inital deposit, annual interest rate, years that the account will earn interest, and number of times the interest is compounded annually.

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


# Main function to run the program.  
# Prompt the user for input, calculates the future value, and displays the result.
def main():
    print("Enter the following parameters.")

    # User inputs with specific prompt text to enter data to be used in the calculation
    principal = float(input("  The initial deposit? "))
    annual_rate = float(input("  The annual interest rate in percent? "))
    years = float(input("  The number of years the account earn interest? "))
    compounds_per_year = float(input("  The number of times interest is compounded each year: "))

    # Calculates the Compound interest
    rate = annual_rate / 100
    compounded_interest = (1 + rate / compounds_per_year)
    total_compounds = compounds_per_year * years
    future_value = principal * (compounded_interest ** total_compounds)

    # Format and display the result
    formatted_future_value = "${:,.2f}".format(future_value)
    print(f"The balance of this account will be {formatted_future_value} after {years} years.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
