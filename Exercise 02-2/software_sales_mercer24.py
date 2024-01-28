"""
Author: Dennis Mercer, mercer24@purdue.edu
Assignment: 02.2 - Software Sales
Date: 02/27/2024

Description:
    Prompt user to enter the number of packages purchased and then display the amount of the discount and the total amount of the purchase after the discount

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
    
    PACKAGE_PRICE = 880

    # This is a Function to calculate the discount, passing in quantity
    def calculate_discount(quantity):
        if 4 <= quantity <= 39:
            return 0.10  # 10% discount
        elif 40 <= quantity <= 199:
            return 0.15  # 15% discount
        elif 200 <= quantity <= 999:
            return 0.30  # 30% discount
        elif quantity >= 1000:
            return 0.42  # 42% discount
        else:
            return 0  # No discount

    # Prompt the user for the number of packages to be purchased
    quantity = int(input("How many packages will be purchased: "))

    # Check for invalid input
    if quantity < 0:
        print("  Invalid Input!")
    else:
        discount_rate = calculate_discount(quantity)
        discount_amount = PACKAGE_PRICE * quantity * discount_rate
        total_price = PACKAGE_PRICE * quantity - discount_amount

        # Display the results
        if discount_rate > 0:
            print(f"  {discount_rate * 100:.0f}% discount applied.")
        else:
            print("  No discount applied.")

        print(f"  The total price to purchase {quantity} packages is ${total_price:,.2f}.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
