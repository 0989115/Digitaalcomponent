class player:

    def __init__ (self, name, cannons, coins, isalive):
        self.name = name
        self.cannons = cannons
        self.coins = coins
        self.isalive = isalive

    def playerDeath(self):
        player.isalive = False

    def calculateScore(self):
        self.score = self.cannons + self.coins

    def loseCannon(self):
        self.cannons -= 1

    def loseCoin(self):
        self.coins -= 1
