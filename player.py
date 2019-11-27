class player:

    def __init__ (self, name, cannons, coins, isalive):
        self.name = name
        self.cannons = cannons
        self.coins = coins
        self.isalive = isalive

    def playerDeath(self):
        player.isalive = False

    def calculateScore(self):
        self.score = self.cannons + self.munten

    def loseCannon(self):
        player.cannons -= 1

    def loseCoin(self):
        player.coins -= 1
print()