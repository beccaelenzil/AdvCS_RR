from Connect4 import Board as Board
from random import *

class basicPlayer():
    """a basic player class that selects the next move"""
    def __init__(self, ox):
        """the constructor"""
        self.ox = ox

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Basic player for " + self.ox + "\n"
        return s

    def nextMove(self,b):
        """selects an allowable next move at random"""
        col = -1
        while b.allowsMove(col) == False:
            col = randrange(b.width)
        return col

class smartPlayer(basicPlayer):
    """ an AI player for Connect Four """
    def __init__(self, ox):
        """ the constructor inherits from from the basicPlayer class"""
        basicPlayer.__init__(self, ox)

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Smart player for " + self.ox + "\n"
        return s

    def oppCh(self):
        return 'X' if self.ox == 'O' else 'O'

    def scoresFor(self,b):
        scores = [50] * b.width
        for col in range(b.width):
            if not b.allowsMove(col):
                scores[col] = -1
            else:
                b.addMove(col,self.ox)
                if b.winsFor(self.ox):
                    scores[col] = 100
                else:
                    for colOpp in range(b.width):
                        if b.allowsMove(colOpp):
                            b.addMove(colOpp,self.oppCh())
                            if b.winsFor(self.oppCh()):
                                scores[col] = 0
                            b.delMove(colOpp)
                b.delMove(col)
        return scores

    def nextMove(self,b):
        scores = self.scoresFor(b)
        max_index = [x for x in range(len(scores)) if scores[x] == max(scores)]
        return max_index[randrange(len(max_index))]

class humanPlayer(basicPlayer):
    def __init__(self,ox):
        basicPlayer.__init__(self,ox)
    def nextMove(self,b):
        print self.ox + ": Choose Column..."
        move = self.filterInput(b)
        while not b.allowsMove(move):
            move = self.filterInput(b)
        return move
    def filterInput(self,b):
        """waits until valid input is entered
        """
        a = -1
        while a not in [str(x) for x in range(b.width)]:
            a = raw_input()
        return int(a)

def playGame(p1,p2):
    b = Board(7,6)
    if p1 == 'smart':
        playerX = smartPlayer('X')
    elif p1 == 'basic':
        playerX = basicPlayer('X')
    elif p1 == 'human':
        playerX = humanPlayer('X')
    if p2 == 'smart':
        playerO = smartPlayer('O')
    elif p2 == 'basic':
        playerO = basicPlayer('O')
    elif p2 == 'human':
        playerO = humanPlayer('O')
    move = -1
    player = 1
    while b.checkWin() == 0 and not b.isFull():
        print b
        if player == 1:
            b.addMove(playerX.nextMove(b),'X')
        else:
            b.addMove(playerO.nextMove(b),'O')
        player = -player
    print b
    a = ["*You Both Lose!*","*X WINS!*", "*O WINS!*"]
    print a[b.checkWin()]
    return b.checkWin()

def BasicVSmart():
    truce_x_o = [0,0,0]
    for i in range(100):
        truce_x_o[playGame('smart','smart')] += 1
        print truce_x_o
    return truce_x_o
BasicVSmart()
#playGame('smart','human')