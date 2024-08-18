import Player

'''
Items can be collected by players during their turns. Items can affect a
player's speed, strength, and intellect modifiers
'''

class Item:
    name        = ""
    speed       = 0
    strength    = 0
    intellect   = 0

    def __init__(self, name: str, speed: int, strength: int, intellect: int):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.intellect = intellect

        print('Item ' + name + ' has been initialised')

    # Update a character's modifiers
    def apply(self, player: Player):
        player.speedMod     += self.speed
        player.strengthMod  += self.strength
        player.intelMod     += self.intellect

    def discard(self, player: Player):
        player.speedMod     -= self.speed
        player.strengthMod  -= self.strength
        player.intelMod     -= self.intellect