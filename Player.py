from random import randint
import Item


class Player:
    # String to be used as the player's name
    name        = ""

    # Starting health of the character, and it's maximum health level
    # recommended 100 for heavy-weight, and 1 for ant-weight
    maxHealth   = -1

    # Character's speed stat
    # Used with intellect and strength to determine the character's combat proficiency
    # Determines movement and speed
    # Recommended 10 for speed of light, 1 for snail's pace
    speed       = -1
    # speed modifier
    speedMod    = 0

    # This is the player's strength stat
    # This will be used in tandem with speed and intellect to determine the character's combat proficiency
    # Recommended 10 for god killers, and 1 for nitwits
    strength    = -1
    # Strength modifier
    strengthMod = 0

    # Intellect stat that determines the character's decision-making proficiency
    # Used with speed and strength to determine the character's combat proficiency
    # Improves search efficiency
    # Recommended 10 for omniscient, 1 for idiot
    intellect   = -1
    # Intellect modifier
    intelMod    = 0

    # Current in-game health
    gameHealth  = -1

    # Backpack
    # This list stores all the items the character collects along their journey
    # Maximum items in backpack is 10
    backpack    = []
    # a part of the backpack specifically for consumables. Does not increase backpack capacity
    consumables = []

    # Character initialisation
    def __init__(self, name: str, maxHealth: int, speed: int, strength: int, intellect: int):

        # Check for invalid character data
        if (
            name == "" or
            maxHealth   < 1 or maxHealth    > 100 or
            speed       < 1 or maxHealth    > 10 or
            strength    < 1 or strength     > 10 or
            intellect   < 1 or intellect    > 10
        ):
            print("There was an issue interpreting character data. Please ensure you have properly formatted your data"
                  "sheet.")

            exit(0)

        # Apply character information
        self.name       = name
        self.maxHealth  = maxHealth
        self.speed      = speed
        self.strength   = strength
        self.intellect  = intellect

        # Initialise game health
        self.gameHealth = maxHealth

        # User feedback
        print('Player ' + name + ' has been successfully initialised')

    # Update modifiers based on backpack contents
    # TODO: Implement this functionality when picking up or discarding an item
    def backpackCheck(self):
        self.speedMod, self.strengthMod, self.intelMod = 0, 0, 0

        for item in self.backpack:
            item.apply(self)


    # Add an item to the backpack, and apply its effects to the character's modifiers
    def addItem(self, item: Item):
        self.backpack.append(item)
        item.apply(self)


    # Remove an item from the backpack, and its effects on the character's modifiers
    def removeItem(self, item: int):
        self.backpack.pop(item).discard()


    # Randomised intel call used for decision-making
    def intelCall(self) -> bool:
        return randint(1, 10) < self.intellect + self.intelMod


    # Calculate the character's combat proficiency
    def combatProficiency(self) -> int:
        return ((self.intellect + self.intelMod)    * 3 +
                (self.speed     + self.speedMod)    * 3 +
                (self.strength  + self.strengthMod) * 4)