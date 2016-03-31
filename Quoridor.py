from visual import *
from copy import *

class board:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.hWalls = [[0]*(width) for i in range(height-1)]
        self.vWalls = [[0]*(width-1) for i in range(height)]
        self.players = [[0,int(self.width/2)],[self.height-1, int(self.width/2)]]

    def __repr__(self):
        s = 'Quoridor\n----------\n'
        for col in range(self.width):
            s += '+-'
        s += '+\n'
        for row in range(self.height-1):
            s += '|'
            for col in range(self.width-1):
                s += '$'if self.players[0] == [row,col] else('%'if self.players[1] == [row,col] else' ')
                s += '|' if self.vWalls[row][col] == 1 else ' '
            s += '$'if self.players[0] == [row,col] else('%'if self.players[1] == [row,col] else' ')
            s += '|\n+'
            for col in range(self.width):
                s += '-' if self.hWalls[row][col] == 1 else ' '
                s += '+'
            s += '\n'
        s += '|'
        for col in range(self.width-1):
            s += '$'if self.players[0] == [self.height-1,col] else('%'if self.players[1] == [self.height-1,col] else' ')
            s += '|' if self.vWalls[self.height-1][col] == 1 else ' '
        s += '$'if self.players[0] == [self.height-1,col] else('%'if self.players[1] == [self.height-1,col] else' ')
        s += '|\n+'
        for col in range(self.width):
            s += '-'
            s += '+'
        s += '\n'
        return s

    def addWall(self,row,col,vh):
        """
        :param row: row
        :param col: column
        :param vh: 0 for vertical 1 for horizontal
        """
        if vh == 0:
            self.vWalls[row][col] = 1
        elif vh == 1:
            self.hWalls[row][col] = 1

    def canWall(self,row,col,vh):
        if row < 0 or row >= self.height-1 or col < 0 or col >= self.width-1 or (vh == 0 and row == self.height-2) or (vh == 1 and col == self.width-2):
            return False
        if vh == 0 and self.vWalls[row][col] == 0 and self.vWalls[row+1][col] == 0:
            return True
        elif vh == 1 and self.hWalls[row][col] == 0 and self.hWalls[row][col+1] == 0:
            return True
        return False

    def playWall(self,row,col,vh):
        """
        play a 2 length wall defined from upper left position
        :param vh: 0 for vertical 1 for horizontal
        :return: true if it works false if it doesn't
        """
        if vh == 0 and self.canWall(row,col,vh):
            self.vWalls[row][col] = 1
            self.vWalls[row+1][col] = 1
            if not self.checkPaths():
                self.vWalls[row][col] = 0
                self.vWalls[row+1][col] = 0
                return False
            return True
        elif vh == 1 and self.canWall(row,col,vh):
            self.hWalls[row][col] = 1
            self.hWalls[row][col+1] = 1
            if not self.checkPaths():
                self.vWalls[row][col] = 0
                self.vWalls[row][col+1] = 0
                return False
            return True
        return False

    def canMove(self,srow, scol, row,col):
        """
        row and col are possition p is player returns true if player p can move to position row col else false
        """
        if scol < 0 or srow < 0 or row < 0 or col < 0 or scol >= self.width or srow >= self.height or col >= self.width or row >= self.height:
            return False
        if scol == 0 and srow == 0:
            if [srow+1,scol] == [row,col] and self.hWalls[row][col] == 0:
                return True
            elif [srow,scol+1] == [row,col] and self.vWalls[row][col] == 0:
                return True
            else:
                return False
        elif scol == 0 and srow == self.height-1:
            if [srow-1,scol] == [row,col] and self.hWalls[row-1][col] == 0:
                return True
            elif [srow,scol+1] == [row,col] and self.vWalls[row][col] == 0:
                return True
            else:
                return False
        elif scol == self.width-1 and srow == 0:
            if [srow+1,scol] == [row,col] and self.hWalls[row][col] == 0:
                return True
            elif [srow,scol-1] == [row,col] and self.vWalls[row][col-1] == 0:
                return True
            else:
                return False
        elif scol == self.width -1 and scol == self.width:
            if [srow-1,scol] == [row,col] and self.hWalls[row][col] == 0:
                return True
            elif [srow,scol-1] == [row,col] and self.vWalls[row][col] == 0:
                return True
            else:
                return False
        elif scol == 0:
            if [srow+1,scol] == [row,col] and self.hWalls[row-1][col] == 0:
                return True
            elif [srow-1,scol] == [row,col] and self.hWalls[row][col] == 0:
                return True
            elif [srow,scol-1] == [row,col] and self.vWalls[row][col] == 0:
                return True
            else:
                return False
        elif scol == self.width - 1:
            if [srow+1,scol] == [row,col] and self.hWalls[row-1][col] == 0:
                return True
            elif [srow-1,scol] == [row,col] and self.hWalls[row][col] == 0:
                return True
            elif [srow,scol+1] == [row,col] and self.vWalls[row][col-1] == 0:
                return True
            else:
                return False
        elif srow == 0:
            if [srow+1,scol] == [row,col] and self.hWalls[row-1][col] == 0:
                return True
            elif [srow,scol+1] == [row,col] and self.vWalls[row][col-1] == 0:
                return True
            elif [srow,scol-1] == [row,col] and self.vWalls[row][col] == 0:
                return True
            else:
                return False
        elif srow == self.height -1:
            if [srow-1,scol] == [row,col] and self.hWalls[row-1][col] == 0:
                return True
            elif [srow,scol+1] == [row,col] and self.vWalls[row][col-1] == 0:
                return True
            elif [srow,scol-1] == [row,col] and self.vWalls[row][col] == 0:
                return True
            else:
                return False
        else:
            if [srow+1,scol] == [row,col] and self.hWalls[row-1][col] == 0:
                return True
            elif [srow-1,scol] == [row,col] and self.hWalls[row][col] == 0:
                return True
            elif [srow,scol+1] == [row,col] and self.vWalls[row][col-1] == 0:
                return True
            elif [srow,scol-1] == [row,col] and self.vWalls[row][col] == 0:
                return True
            else:
                return False

    def movePlayer(self,row,col,p):
        """
        tries to move player p(0 or 1) to row, col
        :return: true if worked false otherwise
        """
        if self.canMove(self.players[p][0],self.players[p][1],row,col) and self.players[p-1] != [row,col]:#need to implement if other pawn is in way
            self.players[p] = [row,col]
            return True
        elif self.canMove(self.players[p][0],self.players[p][1],row,col) and self.players[p-1] == [row,col]\
                and self.canMove(row,col,row+(row-self.players[p][0]),col+(col-self.players[p][1])):
            self.players[p] = [row+(row-self.players[p][0]),col+(col-self.players[p][1])]
        else:
            return False

    def pathAvailable(self,p):
        """ runs a pathfinder algorithm to see if it is possible for both players to get from their point to the other side
        :param p: which player you are searching for
        :return:
        """
        openNodes = [self.players[p]]
        #print 'open-start' + str(openNodes)
        closedNodes = []
        while openNodes != []:
            tempNodes = openNodes
            openNodes = []
            for i in range(len(tempNodes)):
                closedNodes.append(tempNodes[i])
                if (tempNodes[i][0] == self.height-1 and p == 0) or (tempNodes[i][0] == 0 and p == 1):
                    return True
                if self.canMove(tempNodes[i][0],tempNodes[i][1],tempNodes[i][0]+1,tempNodes[i][1]) and [tempNodes[i][0]+1,tempNodes[i][1]] not in closedNodes:
                    openNodes.append([tempNodes[i][0]+1,tempNodes[i][1]])
                if self.canMove(tempNodes[i][0],tempNodes[i][1],tempNodes[i][0]-1,tempNodes[i][1]) and [tempNodes[i][0]-1,tempNodes[i][1]] not in closedNodes:
                    openNodes.append([tempNodes[i][0]-1,tempNodes[i][1]])
                if self.canMove(tempNodes[i][0],tempNodes[i][1],tempNodes[i][0],tempNodes[i][1]+1) and [tempNodes[i][0],tempNodes[i][1]+1] not in closedNodes:
                    openNodes.append([tempNodes[i][0],tempNodes[i][1]+1])
                if self.canMove(tempNodes[i][0],tempNodes[i][1],tempNodes[i][0],tempNodes[i][1]-1) and [tempNodes[i][0],tempNodes[i][1]-1] not in closedNodes:
                    openNodes.append([tempNodes[i][0],tempNodes[i][1]-1])
            #print 'open' + str(openNodes)
            #print 'closed' + str(closedNodes)
        return False

    def checkPaths(self):
        """ checks both players to see if they can path to the opposite side
        """
        return True if self.pathAvailable(0) and self.pathAvailable(1) else False

    def checkWin(self):
        if self.players[0][0] == self.height-1:
            return 1
        elif self.players[1][0] == 0:
            return 2
        else:
            return 0
    def takeTurn(self,p):
        print self
        a = -1
        while a not in [1,2,3]:
            a = input('1 for move player 2 for horizontal wall 3 for vertical wall')
        if a == 1:
            while not self.movePlayer(input('row:'), input('column:'),p):
                True
        elif a == 2:
            while not self.playWall(input('row:'), input('column:'),1):
                True
        elif a == 3:
            while not self.playWall(input('row:'), input('column:'),0):
                True

    def hostGame(self):
        t = 0
        while self.checkWin() == 0:
            self.takeTurn(t)
            t = 1 if t == 0 else 0

        print 'Player ' + str(self.checkWin()) + 'Wins!'



q = board(9,9)
q.players[0] = [6,4]
q.players[1] = [6,3]
q.hostGame()
#print q.checkPaths()