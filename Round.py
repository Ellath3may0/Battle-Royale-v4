import random

from Config import Config
import time

from Location import Location
from Main import newConfig


class Round:

    name: str
    startTime: time
    players: list
    remaining: list
    lootItems: list
    map: list
    loopCounter: int
    config: Config





    def __init__(self, name: str, config: Config, players: list, items: list, locations: list):
        self.name = name
        self.startTime = time.time()
        self.config = config.copy()
        self.players = players.copy()
        self.remaining = players.copy()
        self.lootItems = items.copy()
        self.loopCounter = 0

        if self.config.locationsEnabled:
            # Map builder
            for i in range(5):
                self.map.append([])
                for j in range(5):
                    if random.randint(0, 2) == 0:
                        self.map[i].append(locations.pop(random.randint(0, len(locations) - 1)))
                        self.map[i][j].
                    else:
                        self.map[i].append(Location("No-Man's Land", [], 0, []))

        print("done")
