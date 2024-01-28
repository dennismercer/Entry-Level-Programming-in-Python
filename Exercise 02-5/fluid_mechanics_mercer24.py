"""
Author: Dennis Mercer, mercer24@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 01/27/2024

Description:
    Prompted user to enter user for:
    - the velocity of the water flowing through a pipe
    - the pipe's diameter
    - and the kinemastic viscosity of the fluid
    

Contributors:
    Your video and the textbook

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

import math

def main():
    # Define the Reynolds number function
    def reynolds_number(V, d, v):
        # Calculate the Reynolds number
        Reynum = (V * d) / v
        return Reynum

    # Prompt the user for input
    print("Enter the temperature in °C as 5, 20, or 50: ", end="")
    T = int(input())
    print("Enter the velocity of water in the pipe (m/s): ", end="")
    V = float(input())
    print("Enter the pipe's diameter (m): ", end="")
    d = float(input())
    # Set the kinematic viscosity based on the user's input.  First part of your Boolean Logic - Types.mp4
    if T == 5:
        v = 1.52e-6
    elif T == 20:
        v = 1.00e-6
    elif T == 50:
        v = 5.54e-7
    else:
        print("Invalid input")
        return
    # Calculate the Reynolds number and print the result
    Reynum = reynolds_number(V, d, v)
    print(f"At {T:.1f}°C, the Reynolds number for flow at {V} m/s in a {d} m diameter pipe is {Reynum:.2e}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
