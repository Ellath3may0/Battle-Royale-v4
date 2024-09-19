from Config import Config
from Round import Round
from Player import Player
from Item import Item
from Location import Location
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
        print(str(num) + " - " + rnd) # TODO: make a to-string method for Round class
        num += 1

def newConfig():
    global config
    config = Config()

def importSheet():
    sheet = csv.reader(input("Please enter the file location of your data sheet: "))
    print("Importing data...")
    for row in sheet:
        if row[0] == "Players" or row[0] == "name":
            continue
        elif row[0] != "":
            try:
                player = Player(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]))
                players.append(player)
            except ValueError:
                print("Data sheet formatting invalid.\nError with player in row " + str(sheet.line_num))
                exit(1)

        if row[6] != "":
            try:
                location = Location(row[6], int(row[7]))
                locations.append(location)
            except ValueError:
                print("Data sheet formatting invalid.\nError with location in row " + str(sheet.line_num))
                exit(1)

        if row[9] != "":
            try:
                item = Item(row[9], int(row[11]), int(row[12]), int(row[13]), int(row[10]) == 1)
                items.append(item)
            except ValueError:
                print("Data sheet formatting invalid.\nError with item in row " + str(sheet.line_num))



def newRound():

    rounds.append(Round(input("Please enter a name for this new round:\n"), config, players, items, locations))

print("Welcome to Battle Royale version 4!\nFor detailed instructions, please refer to READ_ME.md in the root of this "
      "repository")

while True:
    print("Please enter the number corresponding to the action you would like to make.")
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