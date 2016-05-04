import random
class player:
    def __init__(self,plays = []):
        if plays == []:
            self.playList = [random.randrange(0,2) for x in range(random.randint(1,10))]
        else:
            self.playList = plays
        self.fitness = 0
        self.rounds = 0

    def __repr__(self):
        return str(self.playList) + ' fitness:' +str(self.fitness)

    def fitness(self, vs, game, rounds):
        fit = 0
        for i in range(rounds):
            fit += game[self.playList[i%len(self.playList)]][vs.playList[i%len(vs.playList)]]
        fit /= rounds
        self.fitness += fit
        return self.fitness

    def mutate(self):
        plays = self.playList
        plays.insert(random.randint(0,len(self.playList)), random.randint(0,2))
        return plays


class evolution:
    def __init__(self, number, gOne, gTwo):
        self.gameOne = [[3,3],[1,1]]
        self.gameTwo = [[4,4],[2,2]]
        self.num = number
        self.genepool = [[player(),player()] for i in range(number)]

    def fight(self,rounds):
        for j in range(self.num):
            for i in range(self.num):
                self.genepool[j][0].fitness(self.genepool[i][1],self.gameOne,rounds)
                self.genepool[j][1].fitness(self.genepool[i][0],self.gameTwo,rounds)
        for i in range(self.num):
            print self.genepool[i][0]
            print self.genepool[i][1]


fit = evolution(2,[[4,4],[2,2]],[[2,2],[4,4]])
fit.fight(20)
print
print p

