from Config import Config
from Round import Round
import csv

# List of rounds
rounds = []

# Current configuration
config = Config("default")

# List of players
players = []

# List of unique items
items = []

# List of locations
locations = []


def showRounds():
    num = 1
    for rnd in rounds:
        print(num + " - " + rnd) # TODO: make a to-string method for Round class
        num += 1

def newConfig():
    global config
    config = Config()

def importSheet():
    print('placeholder')

def newRound():

    rounds.append(Round(input("Please enter a name for this new round:\n"), config, players, items, locations))

print("Welcome to Battle Royale version 4!\nFor detailed instructions, please refer to READ_ME.md in the root of this "
      "repository")

while True:
    print("Please enter the number corresponding to the action you would like to make.")

    while True:
        answer = input("1 - View previous rounds\n"
                       "2 - Edit round configuration\n"
                       "3 - Import a CSV data sheet\n"
                       "4 - Execute new round simulation\n"
                       "5 - Exit program ! ALL UNSAVED DATA WILL BE LOST !\n")

        if answer   == '1': showRounds()
        elif answer == '2': newConfig()
        elif answer == '3': importSheet()
        elif answer == '4': newRound()
        elif answer == '5': print("Exiting program..."); exit(0)
        elif answer == '7': config = Config(":3")
        else:
            print("!== Input invalid. Please try again. ==!")
            continue