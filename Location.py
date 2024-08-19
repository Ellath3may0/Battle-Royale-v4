import Player
from random import choice

class Location:

    def __init__(self, name: str, lootItems: list, lootTableSize: int, players: list):

        self.name = name
        self.players = players
        self.lootTable = []

        for i in range(lootTableSize):
            self.lootTable.append(lootItems.choice(self.lootTable))

        self.inStorm = False

        print("Location " + name + " has been successfully initialised")

    def lootSearch(self, player: Player) -> list:
        loot = []

        for i in range(3):
            if player.intelCall():
                loot.append(self.lootTable.pop(self.lootTable.index(choice(self.lootTable))))

        return loot