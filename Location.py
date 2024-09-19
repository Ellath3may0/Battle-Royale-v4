import Player
from random import choice

class Location:

    name: str           = ""
    lootTableSize: int  = 0
    inStorm: bool       = False
    players: list       = []
    lootTable: list     = []

    def __init__(self, name: str, lootTableSize: int):

        self.name = name
        self.lootTableSize = lootTableSize
        self.inStorm = False

        print("Location " + name + " has been successfully initialised")

    def lootAndPlayers(self, lootItems: list, players: list):
        self.players = players

        for i in range(0, self.lootTableSize):
            self.lootTable.append(choice(lootItems))

    def lootSearch(self, player: Player) -> list:
        loot = []

        for i in range(3):
            if player.intelCall():
                loot.append(self.lootTable.pop(self.lootTable.index(choice(self.lootTable))))

        return loot