from Player import Player

'''
Items can be collected by players during their turns. Items can affect a
player's speed, strength, and intellect modifiers
'''

class Item:
    name        = ""
    speed       = 0
    strength    = 0
    intellect   = 0
    isHealing   = False
    health      = 0
    usefulness  = 0


    # Constructor
    def __init__(self, name: str, SpdHlth: int, strength: int, intellect: int, isHealing: bool):
        if isHealing:
            self.name = name
            self.health = SpdHlth
            self.isHealing = True

            self.usefulness = SpdHlth

        else:
            self.name = name
            self.speed = SpdHlth
            self.strength = strength
            self.intellect = intellect

            self.usefulness = SpdHlth * 3 + strength * 4 + intellect * 3


        print('Item ' + name + ' has been initialised')


    # Update a character's modifiers
    def apply(self, player: Player):
        player.speedMod     += self.speed
        player.strengthMod  += self.strength
        player.intelMod     += self.intellect


    # discard this item from a characters inventory and remove effects (if not consumable)
    def discard(self, player: Player):
        if self.isHealing:
            player.consumables.pop(player.consumables.index(self))

        else:
            player.speedMod     -= self.speed
            player.strengthMod  -= self.strength
            player.intelMod     -= self.intellect

            player.backpack.pop(player.backpack.index(self))


    # Consume a healing item and apply its effects
    def consume(self, player: Player):
        if self.health > player.maxHealth - player.gameHealth:
            player.gameHealth = player.maxHealth
        else:
            player.gameHealth += self.health

        player.consumables.pop(player.consumables.index(self))