from visual import *

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

    def movePlayer(self,row,col,p):
        """
        tries to move player p(0 or 1) to row, col
        :return: true if worked false otherwise
        """
        if self.players[p] == [row+1,col+1]

q = board(7,7)
q.playWall(0,0,1)
q.playWall(0,0,0)
q.playWall(0,1,1)
print q