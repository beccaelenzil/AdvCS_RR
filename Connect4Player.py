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
            col = random.randrange(b.width)
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
                            b.delMove(col.Opp,self.oppCh())
                b.delMove(col)
        return scores

    def nextMove(self,b):
        scores = self.scoresFor(b)
        max_index = [x for x in range(len(scores)) if scores[x] == max(scores)]
        



p = smartPlayer('X')
print p

p = smartPlayer('O')
print p