"""
Simple lottery number generator terminal app by Matthew Woods for Dubber Programming Challenge

non-standard module requirements:
colorama>=0.4.3

To Expand to 7+ balls, simply initiate a new intance of the LotteryBall class after line 73
and append to the list named 'balls', this can be in theory done up to 49 balls before there
are no more to chose from.
"""
# Imports
import operator
import os
import secrets
from colorama import init, Fore, Back, Style
init() # Used to display colored background on console with Colorama

class LotteryBall:
    """
    Class to store results and formatting from number generator
    """
    def __init__(self, number):
        self.number = number

    def set_colour(self):
        """
        Sets colour based on input number
        """
        if self.number in range(1,10):
            self.colour = Colours.grey
        elif self.number in range(10,20):
            self.colour = Colours.blue
        elif self.number in range(20,30):
            self.colour = Colours.pink
        elif self.number in range(30,40):
            self.colour = Colours.green
        elif self.number in range(40,50):
            self.colour = Colours.yellow

    @property
    def result(self):
        """
        Returns a string containing a result formatted with colorama
        """
        self.set_colour()
        return self.colour + f"{self.number:02}"

class Colours:
    """
    Simple class to store colorama display formatting
    """
    grey = Back.WHITE + Fore.BLACK
    blue = Back.BLUE + Fore.BLACK
    pink = Back.MAGENTA + Fore.BLACK
    green = Back.GREEN + Fore.BLACK
    yellow = Back.YELLOW + Fore.BLACK


def pick_random_from_list(valid_choices):
    """
    Chooses result from list of valid options and then drops 
    the result from the list
    """
    result = secrets.choice(valid_choices)
    valid_choices.remove(result)
    return result

def sort_and_display(balls):
    """
    Sorts list of LotteryBall classes based on 'number' 
    attribute and appends to formatted string for display
    """
    balls.sort(key=operator.attrgetter('number'))
    results = ''
    for ball in range(len(balls)):
        results = results +balls[ball].result + ' '
    return results

def welcome():
    """
    Clears the terminal screen, and displays a title bar.
    """
    os.system('cls')           
    print("**************************************************")
    print("*** Dubber Programming challenge - Lottery App ***")
    print("**************************************************")


if __name__ == "__main__":

    welcome()
    valid_choices = list(range(1,50)) # selection of numbers available to choose from

    while True:
        # initialise ball classes and generate result
        ball_1 = LotteryBall(pick_random_from_list(valid_choices))
        ball_2 = LotteryBall(pick_random_from_list(valid_choices))
        ball_3 = LotteryBall(pick_random_from_list(valid_choices))
        ball_4 = LotteryBall(pick_random_from_list(valid_choices))
        ball_5 = LotteryBall(pick_random_from_list(valid_choices))
        ball_6 = LotteryBall(pick_random_from_list(valid_choices))

        balls = [ball_1, ball_2, ball_3, ball_4, ball_5, ball_6]

        # display results
        print("Generated numbers:")
        print(sort_and_display(balls))
        print(Style.RESET_ALL) # reset stlye to remove background colour

        # query user to regenerate numbers of end program
        while True:
            retry_condition = str(input("Generate new numbers? (y/n) "))
            if (retry_condition == 'y') or (retry_condition == 'Y'):
                valid_choices = list(range(1,50)) # reinitialise fresh list of valid numbers
                break
            elif (retry_condition == 'n') or (retry_condition == 'N'):
                print("Goodbye!")
                quit()
            else:
                print("Invalid Input!")