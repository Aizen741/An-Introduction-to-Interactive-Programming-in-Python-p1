'''import random
def number_to_fortune(number):
    if number == 0:
        return "Yes, for sure!"
    elif number == 1:
        return "Probably yes."
    elif number == 2:
        return "Seems like yes..."
    elif number == 3:
        return "Definitely not!"
    elif number == 4:
        return "Probably not."
    elif number == 5:
        return "I really doubt it..."
    elif number == 6:
        return "Not sure, check back later!"
    elif number == 7:
        return "I really can't tell."
    else:
        return "Something was wrong with my input."

def mystical_octosphere(question):

    print("Your question was... " + question)
    print("You shake the mystical octosphere.")
    answer_number = random.randrange(0, 8)
    answer_fortune = number_to_fortune(answer_number)
    print("The cloudy liquid swirls, and a reply comes into view...")
    print("The mystical octosphere says... " + answer_fortune)
    print()
mystical_octosphere("Will I get rich?")
mystical_octosphere("Are the Cubs going to win the World Series?")
'''


# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper' :
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):

    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    # convert number to a name using if/elif/else
    # don't forget to return the result!


def rpsls(player_choice):

    # print a blank line to separate consecutive games
    print()
    # print out the message for the player's choice
    print('Enter your choice: ')
    print('Player chooses', player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,4)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)

    # print out the message for computer's choice
    print('Computer chooses', comp_choice)

    # compute difference of comp_number and player_number modulo five
    judgement = comp_number - player_number % 5

    # use if/elif/else to determine winner, print winner message
    if(judgement > 0):
        print('Computer wins')
    elif(judgement < 0):
        print('Player wins')
    else:
        print("it's a Tie")

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


































