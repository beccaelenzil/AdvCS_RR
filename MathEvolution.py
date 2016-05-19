import random
class player:
    def __init__(self, plays = [], len = 10, strtnum = 2):
        self.strtNum = strtnum
        if plays == []:
            self.playList = [random.randrange(0,strtnum) for x in range(len)]
        else:
            self.playList = plays
        self.fitness = 0.0

    def __repr__(self):
        return str(self.playList) + ' fitness:' +str(self.fitness)

    def __gt__(self, other):
        if isinstance(other, player):
            return self.fitness > other.fitness
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, player):
            return self.fitness < other.fitness
        return NotImplemented

    def fight(self, vs, game, rounds):
        fit = 0.0
        for i in range(rounds):
            fit += game[self.playList[i%len(self.playList)]][vs.playList[i%len(vs.playList)]]
        fit /= rounds
        self.fitness += fit
        return self.fitness

    def mutate(self):
        switch = random.randrange(self.strtNum)
        plays = self.playList


class evolution:
    def __init__(self, number, gOne, gTwo):
        self.gameOne = gOne
        self.gameTwo = gTwo
        self.num = number
        self.genepool = [[player(strtnum = len(gOne)) for i in range(number)],[player(strtnum = len(gTwo)) for i in range(number)]]

    def __repr__(self):
        prnt = "Group 1:\n"
        for i in range(self.num):
            prnt += str(i) + ": " + self.genepool[0][i].__repr__() + "\n"
        prnt += "Group 2:\n"
        for i in range(self.num):
            prnt += str(i) + ": " + self.genepool[1][i].__repr__() + "\n"
        return prnt



    def fight(self,rounds):
        for j in range(self.num):
            for i in range(self.num):
                self.genepool[0][j].fight(self.genepool[1][i],self.gameOne,rounds)
                self.genepool[1][j].fight(self.genepool[0][i],self.gameTwo,rounds)

    def sort(self):
        for i in range(self.num):
            for j in range(i,0,-1):
                if self.genepool[0][j] < self.genepool[0][j-1]:
                    self.genepool[0][j], self.genepool[0][j-1] = self.genepool[0][j-1], self.genepool[0][j]
                else:
                    break
        for i in range(self.num):
            for j in range(i,0,-1):
                if self.genepool[1][j] < self.genepool[1][j-1]:
                    self.genepool[1][j], self.genepool[1][j-1] = self.genepool[1][j-1], self.genepool[1][j]
                else:
                    break

e = evolution(10,[[1,2,3],[4,5,6],[7,8,9]], [[1,2,3],[4,5,6],[7,8,9]])
e.fight(100)
print e
e.sort()
print e