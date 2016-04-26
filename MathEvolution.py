import random
class player:
    def __init__(self,plays):
        self.playList = plays
        self.fitness = 0

    def fitness(self, vs, game, rounds):
        for i in range(rounds):
            self.fitness += game[self.playList[i%len(self.playList)]][vs.playList[i%len(vs.playList)]]
        self.fitness /= rounds
        return self.fitness