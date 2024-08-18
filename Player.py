import random


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
    # Strenth modifier
    strengthMod = 0

    # Intellect stat that determines the character's decision-making proficiency
    # Used with speed and strength to determine the character's combat proficiency
    # Improves search efficiency
    # Recommended 10 for Omnitient, 1 for idiot
    intellect   = -1
    # Intellect modifier
    intelMod    = 0

    # Gameplay variables
    location    = 00
    gameHealth  = -1

    # Backpack
    # This list stores all the items the character collects along their journey
    # Maximum items in backpack is 10
    backpack = []

    # Character initialisation
    def __init__(self, name: str, maxHealth: int, speed: int, strength: int, intellect: int):
        # Apply character information
        self.name       = name
        self.maxHealth  = maxHealth
        self.speed      = speed
        self.strength   = strength
        self.intellect  = intellect

        # Initialise game health
        self.gameHealth = maxHealth

        # User feedback
        print(name + ' has been successfully initialised.')

    # Update modifiers based on backpack contents
    def backpackCheck(self):
        self.speedMod, self.strengthMod, self.intelMod = 0

        for item in self.backpack:
            item.apply(self)

    def intelCall(self) -> bool:
        return random.random() * 100 + 1 < self.intellect + self.intelMod