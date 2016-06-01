import random
import math
import copy
import matplotlib.pyplot as plt

class player:
    def __init__(self, plays = [], len = 10, strtnum = 2):
        """
        :param plays: override the playlist (leave empty to autofill)
        :param len: length of playlist
        :param strtnum: the number of different strategies
        """
        self.strtNum = strtnum
        if plays == []:
            self.playList = [random.randrange(0,strtnum) for x in range(len)]
        else:
            self.playList = plays
        self.fitness = 0.0

    def __repr__(self):
        """
        :return: string with both the playlist and the fitness
        """
        return str(self.playList) + ' fitness:' +str(self.fitness)

    def __gt__(self, other):
        """
        :return: compares the fitness of two players
        """
        if isinstance(other, player):
            return self.fitness > other.fitness
        return NotImplemented

    def __lt__(self, other):
        """
        :return: compares fitness of two players
        """
        if isinstance(other, player):
            return self.fitness < other.fitness
        return NotImplemented

    def fight(self, vs, game):
        """
        :param vs: the opposing player
        :param game: the game matrix that the two players are playing
        :param rounds: how many times they play the game (if this is longer than the playlist then it will wrap around again)
        :return: player's fitness
        """
        fit = 0.0
        for i in range(len(self.playList)):
            fit += game[self.playList[i]][vs.playList[i]]
        fit /= len(self.playList)
        self.fitness += fit
        return self.fitness

    def mutate(self):
        """
        :return: a player with randomly mutated plays (can mutate from 1 to playlist length of indexes)
        """
        plays = copy.copy(self.playList)
        for i in range(int(float(len(self.playList))/(random.random()*float(len(self.playList)-1)+1.0))):
            switch = random.randrange(self.strtNum-1)
            index = random.randrange(len(self.playList))
            if self.playList[index] != switch:
                plays[index] = switch
            else:
                plays[index] = self.strtNum-1

        return player(plays = plays, len = len(plays), strtnum = self.strtNum)

class evolution:
    def __init__(self, playLen, number, gOne, gTwo):
        """
        :param playLen: length of playlist
        :param number: number of players in each genepool
        :param gOne: the game that the first genepool plays
        :param gTwo: the game that the second genepool plays
        """
        self.gameOne = gOne
        self.gameTwo = gTwo
        self.num = number
        self.len = playLen
        self.genepool = [[player(strtnum = len(gOne),len=playLen) for i in range(number)],[player(strtnum = len(gTwo),len=playLen) for i in range(number)]]

    def __repr__(self):
        """
        :return: string of every player in both genepools
        """
        prnt = "Group 1:\n"
        for i in range(self.num):
            prnt += str(i) + ": " + self.genepool[0][i].__repr__() + "\n"
        prnt += str(self.avgFitness()[0]) + "\nGroup 2:\n"
        for i in range(self.num):
            prnt += str(i) + ": " + self.genepool[1][i].__repr__() + "\n"
        prnt += str(self.avgFitness()[1])
        return prnt

    def avgFitness(self):
        """
        :return: average fitness of both genepools in a list [genepool1, genepool2]
        """
        a = [0,0]
        for i in range(self.num):
            a[0] += self.genepool[0][i].fitness
            a[1] += self.genepool[1][i].fitness
        return [round(a[0]/self.num,3), round(a[1]/self.num,3)]

    def isFull(self):
        """
        :return: true if none of the players are None type, false otherwise
        """
        for i in range(self.num):
            if self.genepool[0][i] == None:
                return False
        return True

    def fight(self):
        """ makes every player fight against every player in the opposing genepool
        """
        for j in range(self.num):
            for i in range(self.num):
                self.genepool[0][j].fight(self.genepool[1][i],self.gameOne)
                self.genepool[1][j].fight(self.genepool[0][i],self.gameTwo)
        for i in range(self.num):
            self.genepool[0][i].fitness /= self.num
            self.genepool[1][i].fitness /= self.num

    def sort(self):
        """ sorts the genepools by fitness
        """
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

    def cull(self):
        """ kills 50% of the population based off of a distribution
        """
        num = 0
        stat = 1
        i = 0
        while num < self.num // 2:
            if random.random() < stat and self.genepool[0][i%self.num] != None:
                num += 1
                self.genepool[0][i%self.num] = None
                self.genepool[1][i%self.num] = None
                stat -= 1.5*stat/self.num
            i += 1

    def rePop(self):
        """ repopulates the genepool by mutating the surviving players (chooses the best to mutate first)(can work on any number of culled players)
        """
        nScan = 0
        pScan = self.num-1
        while not self.isFull():
            while self.genepool[0][pScan] == None:
                pScan = (pScan-1)%self.num
            while self.genepool[0][nScan] != None:
                nScan = (nScan+1)%self.num
            self.genepool[0][nScan] = self.genepool[0][pScan].mutate()
            self.genepool[1][nScan] = self.genepool[1][pScan].mutate()
            nScan = (nScan+1)%self.num
            pScan = (pScan-1)%self.num

    def refresh(self):
        """ resets fitness
        """
        for i in range(self.num):
            self.genepool[0][i].fitness = 0
            self.genepool[1][i].fitness = 0

    def generation(self,rounds):
        """ executes rounds number of generations
        """
        a = []
        b = []
        for i in range(rounds):
            self.fight()
            c = self.avgFitness()
            a.append(c[0])
            b.append(c[1])
            self.sort()
            self.cull()
            self.rePop()
            self.refresh()
        self.fight()
        self.sort()
        print self
        plt.scatter([x for x in range(len(a))],a,color = "red")
        plt.scatter([x for x in range(len(b))],b,color = "green")
        plt.show()

class statPlayer:
    def __init__(self, plays = [], strtnum = 2):
        self.strtnum = strtnum
        self.plays = plays
        if plays == []:
            plays = [random.random() for i in range(strtnum)]
            tot = sum(plays)
            self.plays = [plays[x]/tot for x in range(strtnum)]
        self.fitness = 0.0

    def __repr__(self):
        prnt = str(self.plays) + "fitness: " + str(self.fitness)
        return prnt

    def __gt__(self, other):
        """
        :return: compares the fitness of two players
        """
        if isinstance(other, player):
            return self.fitness > other.fitness
        return NotImplemented

    def __lt__(self, other):
        """
        :return: compares fitness of two players
        """
        if isinstance(other, player):
            return self.fitness < other.fitness
        return NotImplemented

    def play(self):
        rnd = random.random()
        for i in range(self.strtnum):
            rnd -= self.plays[i]
            if rnd <= 0:
                return i
        return self.strtnum-1

    def fight(self, vs, game, rounds):
        """
        :param vs: the opposing player
        :param game: the game matrix that the two players are playing
        :param rounds: how many times they play the game (if this is longer than the playlist then it will wrap around again)
        :return: player's fitness
        """
        fit = 0.0
        for i in range(rounds):
            fit += game[self.play()][vs.play()]
        fit /= rounds
        self.fitness += fit
        return self.fitness

    def mutate(self):
        """
        :return: a player with randomly mutated plays (can mutate from 1 to playlist length of indexes)
        """
        plays = copy.copy(self.plays)
        a = [.01/random.random() for i in range(self.strtnum)]
        tot = sum(a) + sum(plays)
        plays = [(a[i]+plays[i])/(tot) for i in range(self.strtnum)]
        return statPlayer(plays = plays, strtnum = self.strtnum)

class statEvolution:
    def __init__(self, playLen, number, gOne, gTwo):
        """
        :param playLen: length of playlist
        :param number: number of players in each genepool
        :param gOne: the game that the first genepool plays
        :param gTwo: the game that the second genepool plays
        """
        self.gameOne = gOne
        self.gameTwo = gTwo
        self.num = number
        self.len = playLen
        self.genepool = [[statPlayer(strtnum = len(gOne)) for i in range(number)],[statPlayer(strtnum = len(gTwo)) for i in range(number)]]

    def __repr__(self):
        """
        :return: string of every player in both genepools
        """
        prnt = "Group 1:\n"
        for i in range(self.num):
            prnt += str(i) + ": " + self.genepool[0][i].__repr__() + "\n"
        prnt += str(self.avgFitness()[0]) + "\nGroup 2:\n"
        for i in range(self.num):
            prnt += str(i) + ": " + self.genepool[1][i].__repr__() + "\n"
        prnt += str(self.avgFitness()[1])
        return prnt

    def avgFitness(self):
        """
        :return: average fitness of both genepools in a list [genepool1, genepool2]
        """
        if None in self.genepool[0]:
            return [0,0]
        a = [0,0]
        for i in range(self.num):
            a[0] += self.genepool[0][i].fitness
            a[1] += self.genepool[1][i].fitness
        return [round(a[0]/self.num,3), round(a[1]/self.num,3)]

    def isFull(self):
        """
        :return: true if none of the players are None type, false otherwise
        """
        for i in range(self.num):
            if self.genepool[0][i] == None:
                return False
        return True

    def fight(self):
        """ makes every player fight against every player in the opposing genepool
        """
        for j in range(self.num):
            for i in range(self.num):
                self.genepool[0][j].fight(self.genepool[1][i],self.gameOne,self.len)
                self.genepool[1][j].fight(self.genepool[0][i],self.gameTwo,self.len)
        for i in range(self.num):
            self.genepool[0][i].fitness /= self.num
            self.genepool[1][i].fitness /= self.num

    def sort(self):
        """ sorts the genepools by fitness
        """
        for i in range(self.num):
            for j in range(i,0,-1):
                if self.genepool[0][j].fitness < self.genepool[0][j-1].fitness:
                    self.genepool[0][j], self.genepool[0][j-1] = self.genepool[0][j-1], self.genepool[0][j]
                else:
                    break
        for i in range(self.num):
            for j in range(i,0,-1):
                if self.genepool[1][j].fitness < self.genepool[1][j-1].fitness:
                    self.genepool[1][j], self.genepool[1][j-1] = self.genepool[1][j-1], self.genepool[1][j]
                else:
                    break

    def cull(self):
        """ kills 50% of the population based off of a distribution
        """
        num = 0
        stat = 1
        i = 0
        while num < self.num // 2:
            if random.random() < stat and self.genepool[0][i%self.num] != None:
                num += 1
                self.genepool[0][i%self.num] = None
                self.genepool[1][i%self.num] = None
                stat -= 1.5*stat/self.num
            i += 1

    def rePop(self):
        """ repopulates the genepool by mutating the surviving players (chooses the best to mutate first)(can work on any number of culled players)
        """
        nScan = 0
        pScan = self.num-1
        while not self.isFull():
            while self.genepool[0][pScan] == None:
                pScan = (pScan-1)%self.num
            while self.genepool[0][nScan] != None:
                nScan = (nScan+1)%self.num
            self.genepool[0][nScan] = self.genepool[0][pScan].mutate()
            self.genepool[1][nScan] = self.genepool[1][pScan].mutate()
            nScan = (nScan+1)%self.num
            pScan = (pScan-1)%self.num

    def refresh(self):
        """ resets fitness
        """
        for i in range(self.num):
            self.genepool[0][i].fitness = 0
            self.genepool[1][i].fitness = 0

    def generation(self,rounds):
        """ executes rounds number of generations
        """
        a = []
        b = []
        for i in range(rounds):
            self.fight()
            c = self.avgFitness()
            a.append(c[0])
            b.append(c[1])
            self.sort()
            self.cull()
            self.rePop()
            self.refresh()
        self.fight()
        self.sort()
        print self
        plt.scatter([x for x in range(len(a))],a,color = "red")
        plt.scatter([x for x in range(len(b))],b,color = "green")
        plt.show()
"""
#No Dom Zero Sum
a = [[1,0,2],
    [-1,4,1],
    [3,2,-4]]

b = [[-1,1,-3],
     [0,-4,-2],
     [-2,-1,4]]
#Prisoner's
a = [[-8,11],
     [-10,10]]
#No Dom
a = [[4,2,2],
     [3,0,5],
     [1,4,6]]
b = [[2,6,4],
     [4,1,3],
     [5,3,1]]
#ESS
a = [[-25,50,50,-25,12.5],
     [0,15,0,15,7.5],
     [0,50,25,0,25],
     [-25,15,50,15,-5],
     [-12.5,32.5,25,-5,25]]
"""

#ESS maybe?
a = [[4,5,2],
    [2,3,6],
    [1,3,8]]

b = [[5,4,1],
    [4,0,3],
    [2,2,10]]

#e = evolution(50,25,a,b) #Red is p1 Green p2
#e.generation(500)
#e = statEvolution(50,25,a,b)
# e.generation(500)
e = statEvolution(10,10,a,b)
print e
e.fight()
print e
e.sort()
print e
e.cull()
print e
e.rePop()
e.refresh()
print e

"""
a = [[-25,50,50,-25,12.5],
     [0,15,0,15,7.5],
     [0,50,25,0,25],
     [-25,15,50,15,-5],
     [-12.5,32.5,25,-5,25]]
"""
"""
a = [[-25,30,30,-25],
    [0,50,0,15],
    [0,30,50,0],
    [-25,15,30,15]]
"""
