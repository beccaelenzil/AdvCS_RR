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
        """moves in a column col for a player ox
        """
        if ox == 'X':
            ox = 1
        elif ox == 'O':
            ox = -1
        if col >= self.width or col < 0 or self.data[0][col] != 0:
            return False
        for row in range(self.height-1, -1,-1):
            if self.data[row][col] == 0:
                self.data[row][col] = ox
                return True
        return False

    def setBoard(self,moveString):
        """sets board according to a string
        """
        next = 1
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, next)
            next = -next

    def allowsMove(self, col):
        """checks if can move in column
        """
        if col >= self.width or col < 0 or self.data[0][col] != 0:
            return False
        else:
            return True

    def clear(self):
        """clears board
        """
        for row in range(0,self.height):
            for col in range(0,self.width):
                self.data[row][col] = 0

    def isFull(self):
        """returns true if its full false otherwise
        """
        for col in range(0,self.width):
            if self.data[0][col] == 0:
                return False
        return True

    def delMove(self, c):
        """removes the top chip and returns true, false if it cant
        """
        for row in range(0, self.height):
            if self.data[row][c] != 0:
                self.data[row][c] = 0
                return True
        return False

    def checkHor(self):
        """returns 1 for O win and -1 for X win 0 for no win. checks horizontally
        """
        for row in range(3,self.height):
            for col in range(3,self.width):
                if self.data[row][col]+self.data[row][col-1]+self.data[row][col-2]+self.data[row][col-3] == 4:
                    return 1
                elif self.data[row][col]+self.data[row][col-1]+self.data[row][col-2]+self.data[row][col-3] == -4:
                    return -1
        return 0

    def checkVert(self):
        """returns 1 for O win and -1 for X win 0 for no win. checks vertically
        """
        for row in range(3,self.height):
            for col in range(0,self.width):
                if self.data[row][col]+self.data[row-1][col]+self.data[row-2][col]+self.data[row-3][col] == 4:
                    return 1
                elif self.data[row][col]+self.data[row-1][col]+self.data[row-2][col]+self.data[row-3][col] == -4:
                    return -1
        return 0

    def checkSlant(self):
        """returns 1 for O win and -1 for X win 0 for no win. checks slants
        """
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
        """returns 1 for O win and -1 for X win 0 for no win
        """
        if self.checkHor() != 0:
            return self.checkHor()
        elif self.checkVert() != 0:
            return self.checkVert()
        elif self.checkSlant() != 0:
            return self.checkSlant()
        else:
            return 0
    def winsFor(self, ox):
        if ox == 'X':
            for row in range(3,self.height):
                for col in range(3,self.width):
                    if self.data[row][col]+self.data[row-1][col-1]+self.data[row-2][col-2]+self.data[row-3][col-3] == 4:
                        return True
            for row in range(0,self.height-3):
                for col in range(3,self.width):
                    if self.data[row][col]+self.data[row+1][col-1]+self.data[row+2][col-2]+self.data[row+3][col-3] == 4:
                        return True
            for row in range(3,self.height):
                for col in range(0,self.width):
                    if self.data[row][col]+self.data[row-1][col]+self.data[row-2][col]+self.data[row-3][col] == 4:
                        return True
            for row in range(3,self.height):
                for col in range(3,self.width):
                    if self.data[row][col]+self.data[row][col-1]+self.data[row][col-2]+self.data[row][col-3] == 4:
                        return True
            return False
        elif ox == 'O':
            for row in range(3,self.height):
                for col in range(3,self.width):
                    if self.data[row][col]+self.data[row-1][col-1]+self.data[row-2][col-2]+self.data[row-3][col-3] == -4:
                        return True
            for row in range(0,self.height-3):
                for col in range(3,self.width):
                    if self.data[row][col]+self.data[row+1][col-1]+self.data[row+2][col-2]+self.data[row+3][col-3] == -4:
                        return True
            for row in range(3,self.height):
                for col in range(0,self.width):
                    if self.data[row][col]+self.data[row-1][col]+self.data[row-2][col]+self.data[row-3][col] == -4:
                        return True
            for row in range(3,self.height):
                for col in range(3,self.width):
                    if self.data[row][col]+self.data[row][col-1]+self.data[row][col-2]+self.data[row][col-3] == -4:
                        return True
            return False
        return False

        print self.checkWin()
        return test == self.checkWin()
    def filterInput(self):
        """waits until valid input is entered
        """
        a = -1
        while a not in [str(x) for x in range(self.width)]:
            a = raw_input()
        return int(a)

    def hostGame(self):
        """plays game
        """
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
        a = ["*You Both Lose!*","*X WINS!*", "*O WINS!*"]
        print a[self.checkWin()]

b = Board(7,6)
#b.hostGame()

# Connect Four Tests

print "---------------------------------------------"
print "print a 7 x 6 board with the columns numbered"
print "---------------------------------------------\n"
b = Board(7,6)
print b

print " "
print "---------------------------------------------"
print "test addMove"
print "---------------------------------------------\n"
print "| | | | | | | |"
print "| | | | | | | |"
print "| | | | | | | |"
print "|X| | | | | | |"
print "|O| | | | | | |"
print "|X| | |O|O|O|O|"
print "---------------"
print " 0 1 2 3 4 5 6\n"
print "==\n"
b.addMove(0, 'X')
b.addMove(0, 'O')
b.addMove(0, 'X')
b.addMove(3, 'O')
b.addMove(4, 'O')  # cheating by letting O go again!
b.addMove(5, 'O')
b.addMove(6, 'O')
print b

print " "
print "---------------------------------------------"
print "test clear"
print "---------------------------------------------\n"
print "print an empty board"
b.clear()
print b

print " "
print "---------------------------------------------"
print "test allowsMove"
print "---------------------------------------------\n"
b = Board(2,2)
b.addMove(0, 'X')
b.addMove(0, 'O')
print b
print " "
print "b.allowsMove(-1) should be False == ",b.allowsMove(-1)
print "b.allowsMove(0) should be False == ",b.allowsMove(0)
print "b.allowsMove(1) should be True == ",b.allowsMove(1)
print "b.allowsMove(2) should be False == ",b.allowsMove(2)

print " "
print "---------------------------------------------"
print "test isFull"
print "---------------------------------------------\n"
b = Board(2,2)
print b
print " "
print "b.isFull() should be False == ", b.isFull()
print " "
b.setBoard( '0011' )
print b
print " "
print "b.isFull() should be True == ", b.isFull()


print " "
print "---------------------------------------------"
print "test delMove"
print "---------------------------------------------\n"

b = Board(2,2)
b.setBoard( '0011' )
print b
print "after the following commands: \n \
b.delMove(1) \n \
b.delMove(1) \n \
b.delMove(1) \n \
b.delMove(0) \n \
The board should look like: \n \
| | | \n \
|X| | \n \
-----\n \
 0 1 \n \
 == "
b.delMove(1)
b.delMove(1)
b.delMove(1)
b.delMove(0)
print b

print " "
print "---------------------------------------------"
print "test winsFor"
print "---------------------------------------------\n"


b = Board(7,6)
b.setBoard( '00102030' )
print "if b.setBoard( '00102030' ), then b.winsFor('X') should be True == ",b.winsFor('X')
print "if b.setBoard( '00102030' ), then b.winsFor('O') should be True == ",b.winsFor('O')

b = Board(7,6)
b.setBoard( '23344545515'  )
print "if b.setBoard( '23344545515'  ), then b.winsFor('X') should be True == ",b.winsFor('X')
print "if b.setBoard( '23344545515'  ), then b.winsFor('O') should be False == ",b.winsFor('O')

print " "
print "---------------------------------------------"
print "host game"
print "---------------------------------------------\n"

# play your game with a friend, tell me who you played with, and confirm that everything works

print "I played with Ben"
print "Everything works!"

