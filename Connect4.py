# python 2
#
# Problem Set 2, Problem 1
# Name:
#

import os

class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """

    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [0]*W for row in range(H) ]

        # we do not need to return inside a constructor!


    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        ref = [' ', 'X', 'O']
        for row in range(0,H):
            s += '|'
            for col in range(0,W):
                s += ref[int(self.data[row][col])]
                s += '|'
            s += '\n'

        s += (2*W+1) * '-' + '\n'  # bottom of the board

        for i in range(W): # and the numbers underneath here
            s += ' ' + str(i%10)
        return s       # the board is complete, return it

    def addMove(self, col, ox):
        if col >= self.width or col < 0 or self.data[0][col] != 0:
            return False
        for row in range(self.height-1, -1,-1):
            if self.data[row][col] == 0:
                self.data[row][col] = ox
                return True
        return False

    def setBoard(self,moveString):
        next = 1
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, next)
            next = -next

    def allowsMove(self, col):
        if col >= self.width or col < 0 or self.data[0][col] != 0:
            return False
        else:
            return True

    def clear(self):
        for row in range(0,self.height):
            for col in range(0,self.width):
                self.data[row][col] = 0

    def isFull(self):
        for col in range(0,self.width):
            if self.data[0][col] == 0:
                return False
        return True

    def delMove(self, c):
        for row in range(0, self.height):
            if self.data[row][c] != 0:
                self.data[row][c] = 0
                return True
        return False

    def checkHor(self):
        for row in range(3,self.height):
            for col in range(3,self.width):
                if self.data[row][col]+self.data[row][col-1]+self.data[row][col-2]+self.data[row][col-3] == 4:
                    return 1
                elif self.data[row][col]+self.data[row][col-1]+self.data[row][col-2]+self.data[row][col-3] == -4:
                    return -1
        return 0

    def checkVert(self):
        for row in range(3,self.height):
            for col in range(0,self.width):
                if self.data[row][col]+self.data[row-1][col]+self.data[row-2][col]+self.data[row-3][col] == 4:
                    return 1
                elif self.data[row][col]+self.data[row-1][col]+self.data[row-2][col]+self.data[row-3][col] == -4:
                    return -1
        return 0

    def checkSlant(self):
        for row in range(3,self.height):
            for col in range(3,self.width):
                if self.data[row][col]+self.data[row-1][col-1]+self.data[row-2][col-2]+self.data[row-3][col-3] == 4:
                    return 1
                elif self.data[row][col]+self.data[row-1][col-1]+self.data[row-2][col-2]+self.data[row-3][col-3] == -4:
                    return -1
        for row in range(0,self.height-3):
            for col in range(3,self.width):
                if self.data[row][col]+self.data[row+1][col-1]+self.data[row+2][col-2]+self.data[row+3][col-3] == 4:
                    return 1
                elif self.data[row][col]+self.data[row+1][col-1]+self.data[row+2][col-2]+self.data[row+3][col-3] == -4:
                    return -1
        return 0

    def checkWin(self):
        """returns 1 for X win and -1 for O win
        """
        if self.checkHor() != 0:
            return self.checkHor()
        elif self.checkVert() != 0:
            return self.checkVert()
        elif self.checkSlant() != 0:
            return self.checkSlant()
        else:
            return 0

    def filterInput(self):
        a = -1
        while a not in [str(x) for x in range(self.width)]:
            a = raw_input()
        return int(a)

    def hostGame(self):
        move = -1
        player = 1
        while self.checkWin() == 0 and not self.isFull():
            print self
            if player == 1:
                print "X: Choose Column..."
                move = self.filterInput()
                while not self.addMove(move,player):
                    move = self.filterInput()
            else:
                print "O: Choose Column..."
                move = self.filterInput()
                while not self.addMove(move,player):
                    move = self.filterInput()
            player = -player
        print self
        a = ["*O WINS!*", "*X WINS!*"]
        print a[self.checkWin()]

b = Board(7,6)

b.hostGame()