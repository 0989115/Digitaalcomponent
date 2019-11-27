class player:

    def __init__ (self, name, cannons, coins, isalive):
        self.name = name
        self.cannons = cannons
        self.coins = coins
        self.isalive = isalive

    def playerDeath(self):
        self.isalive = False

    def calculateScore(self):
        self.score = self.cannons + self.coins

    def loseCannon(self):
        self.cannons -= 1

    def loseCoin(self):
        self.coins -= 1

    def addCannon(self):
        self.cannons += 1

    def addCoins(self):
        self.coins += 1
