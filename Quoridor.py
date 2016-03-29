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

    def playWall(self,row,col,vh):
        """
        play a 2 length wall defined from upper left position
        :param vh: 0 for vertical 1 for horizontal
        :return: true if it works false if it doesn't
        """
        if vh == 0 and self.vWalls[row][col] == 0 and self.vWalls[row+1][col] == 0:
            self.vWalls[row][col] = 1
            self.vWalls[row+1][col] = 1
            return True
        elif vh == 1 and self.hWalls[row][col] == 0 and self.hWalls[row][col+1] == 0:
            self.hWalls[row][col] = 1
            self.hWalls[row][col+1] = 1
            return True
        return False

    def canMove(self,srow, scol, row,col):
        """
        row and col are possition p is player returns true if player p can move to position row col else false
        """
        if scol == 0 and srow == 0:
            if [srow,scol] == [row+1,col] and self.hWalls[row][col] == 0:
                return True
            elif [srow,scol] == [row,col+1] and self.vWalls[row][col] == 0:
                return True
            else:
                return False
        elif scol == 0 and srow == self.height-1:
            if [srow,scol] == [row-1,col] and self.hWalls[row-1][col] == 0:
                return True
            elif [srow,scol] == [row,col+1] and self.vWalls[row][col] == 0:
                return True
            else:
                return False
        elif scol == self.width-1 and srow == 0:
            if [srow,scol] == [row+1,col] and self.hWalls[row][col] == 0:
                return True
            elif [srow,scol] == [row,col-1] and self.vWalls[row][col-1] == 0:
                return True
            else:
                return False
        elif scol == self.width -1 and scol == self.width:
            if [srow,scol] == [row+1,col] and self.hWalls[row][col] == 0:
                return True
            elif [srow,scol] == [row,col+1] and self.vWalls[row][col] == 0:
                return True
            else:
                return False
        elif scol == 0:
            if [srow,scol] == [row-1,col] and self.hWalls[row-1][col] == 0:
                return True
            elif [srow,scol] == [row+1,col] and self.hWalls[row][col] == 0:
                return True
            elif [srow,scol] == [row,col+1] and self.vWalls[row][col] == 0:
                return True
            else:
                return False
        elif scol == self.width - 1:
            if [srow,scol] == [row-1,col] and self.hWalls[row-1][col] == 0:
                return True
            elif [srow,scol] == [row+1,col] and self.hWalls[row][col] == 0:
                return True
            elif [srow,scol] == [row,col-1] and self.vWalls[row][col-1] == 0:
                return True
            else:
                return False
        elif srow == 0:
            if [srow,scol] == [row+1,col] and self.hWalls[row][col] == 0:
                return True
            elif [srow,scol] == [row,col-1] and self.vWalls[row][col-1] == 0:
                return True
            elif [srow,scol] == [row,col+1] and self.vWalls[row][col] == 0:
                return True
            else:
                return False
        elif srow == self.height -1:
            if [srow,scol] == [row-1,col] and self.hWalls[row-1][col] == 0:
                return True
            elif [srow,scol] == [row,col-1] and self.vWalls[row][col-1] == 0:
                return True
            elif [srow,scol] == [row,col+1] and self.vWalls[row][col] == 0:
                return True
            else:
                return False
        else:
            if [srow,scol] == [row-1,col] and self.hWalls[row-1][col] == 0:
                return True
            elif [srow,scol] == [row+1,col] and self.hWalls[row][col] == 0:
                return True
            elif [srow,scol] == [row,col-1] and self.vWalls[row][col-1] == 0:
                return True
            elif [srow,scol] == [row,col+1] and self.vWalls[row][col] == 0:
                return True
            else:
                return False

    def movePlayer(self,row,col,p):
        """
        tries to move player p(0 or 1) to row, col
        :return: true if worked false otherwise
        """
        if self.canMove(self.players[p][0],self.players[p][1],row,col):#need to implement if other pawn is in way
            self.players[p] = [row,col]
            return True
        else:
            return False

    def pathAvailable(self):
        openNodes = [self.players[0]]
        print 'open-start' + str(openNodes)
        closedNodes = []
        while openNodes != []:
            tempNodes = openNodes
            openNodes = [] # issues with pointers
            for i in range(len(tempNodes)):
                closedNodes.append(tempNodes[i])
                if tempNodes[i][0] == self.height-1:
                    return True
                if self.canMove(tempNodes[i][0],tempNodes[i][1],tempNodes[i][0]+1,tempNodes[i][1]) and [tempNodes[i][0]+1,tempNodes[i][1]] not in closedNodes:
                    openNodes.append([tempNodes[i][0]+1,tempNodes[i][1]])
                if self.canMove(tempNodes[i][0],tempNodes[i][1],tempNodes[i][0]-1,tempNodes[i][1]) and [tempNodes[i][0]-1,tempNodes[i][1]] not in closedNodes:
                    openNodes.append([tempNodes[i][0]-1,tempNodes[i][1]])
                if self.canMove(tempNodes[i][0],tempNodes[i][1],tempNodes[i][0],tempNodes[i][1]+1) and [tempNodes[i][0],tempNodes[i][1]+1] not in closedNodes:
                    openNodes.append([tempNodes[i][0],tempNodes[i][1]+1])
                if self.canMove(tempNodes[i][0],tempNodes[i][1],tempNodes[i][0],tempNodes[i][1]-1) and [tempNodes[i][0],tempNodes[i][1]-1] not in closedNodes:
                    openNodes.append([tempNodes[i][0],tempNodes[i][1]-1])
            print 'open' + str(openNodes)
            print 'closed' + str(closedNodes)
        return False




q = board(7,7)
q.playWall(0,0,1)
q.playWall(0,0,0)
q.playWall(0,3,1)
print q
print q.pathAvailable()