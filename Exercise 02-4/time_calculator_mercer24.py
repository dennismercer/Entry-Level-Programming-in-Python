"""
Author: Dennis Mercer, mercer24@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 01/27/2024

Description:
    Prompted user to enter a number of seconds and then display the total time entered in days, hours,minutes, and seconds.

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

def main():
    # Function that will take the seconds variable that is a user input and will calculate the data
    def convert_seconds_to_time(seconds):
        # If the input is less than 60 seconds, return less than one minute. If not the output is funky
        if seconds < 60:
            return f"{seconds} second(s) is less than one minute."
        else:
            # Calculate the number of days, hours, minutes, and seconds based on your video
            days = seconds // (24 * 3600)
            seconds = seconds % (24 * 3600)
            hours = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60

            # Create a list to store the time components - major ideas taken from your video and then using list as discussed in the textbook
            time = []
            if days > 0:
                time.append(f"{days} day(s)")
            if hours > 0:
                time.append(f"{hours} hour(s)")
            if minutes > 0:
                time.append(f"{minutes} minute(s)")
            if seconds > 0:
                time.append(f"{seconds} second(s)")

            # Format the time components into a string - examples taken from the textbook
        # Format the time components into a string
        if len(time) == 0:
            return "0 second(s)"
        elif len(time) == 1:
            return time[0]
        else:
            # Add a comma before 'and' if there are more than two components
            if len(time) > 2:
                return ", ".join(time[:-1]) + ", and " + time[-1]
            else:
                return " and ".join(time)

    # Prompt the user to enter a number of seconds
    seconds = int(input("Please enter a time in seconds: "))

    # Output the results for a screenshot
    print(f"  {seconds} seconds is less than one minute." if seconds < 60 else f"  {seconds:,} seconds equals {convert_seconds_to_time(seconds)}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
