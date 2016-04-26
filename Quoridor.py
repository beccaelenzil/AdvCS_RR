from visual import *
from copy import *
import random
import time

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

    def getPlayerLocation(self,p):
        return self.players[p]

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
        """returns true if can place wall on row,col with orientation vh (0 for verticle 1 for horizontal)
        """
        if row < 0 or row >= self.height-1 or col < 0 or col >= self.width-1 or (vh == 0 and row == self.height-1) or (vh == 1 and col == self.width-1):
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
        if self.canMove(self.players[p][0],self.players[p][1],row,col) and self.players[p-1] != [row,col]:
            self.players[p] = [row,col]
            return True
        elif self.canMove(self.players[p][0],self.players[p][1],row,col) and self.players[p-1] == [row,col]\
                and self.canMove(row,col,row+(row-self.players[p][0]),col+(col-self.players[p][1])):
            self.players[p] = [row+(row-self.players[p][0]),col+(col-self.players[p][1])]
            return True
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
        """checks win
        :return:0 for no win 1 for player 0 win 2 for player 1 win
        """
        if self.players[0][0] == self.height-1:
            return 1
        elif self.players[1][0] == 0:
            return 2
        else:
            return 0
    def takeTurn(self,p):
        """takes turn for player p
        """
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
        """Does game in console
        """
        t = 0
        while self.checkWin() == 0:
            self.takeTurn(t)
            t = 1 if t == 0 else 0

        print 'Player ' + str(self.checkWin()) + ' Wins!'

class visualBoard:
    def __init__(self,width,height, playerOne, playerTwo):
        """makes the base board"""
        self.b = board(width,height)
        self.base = box(pos=(0,0,-.1),size=(2.5*width+.5,2.5*height+.5,.2),color=color.green)
        self.tiles = [[0 for i in range(width)] for i in range(height)]
        for j in range(height):
            for i in range(width):
                self.tiles[j][i] = box(pos=(i*2.5-1.25*(width-1),j*2.5-1.25*(height-1),.05),size=(2,2,.1),color=color.blue)
        self.vWalls = [[0]*(width-1) for i in range(height)]
        for j in range(height):
            for i in range(width-1):
                self.vWalls[j][i] = box(pos=(2.5+2.5*i-1.25*width,1.25+2.5*j-1.25*height,.025),size=(.5,2,.05),color=color.cyan)
        self.hWalls = [[0]*width for i in range(height-1)]
        for j in range(height-1):
            for i in range(width):
                self.hWalls[j][i] = box(pos=(1.25+2.5*i-1.25*width,2.5+2.5*j-1.25*height,.025),size=(2,.5,.05),color=color.cyan)
        self.players = [cylinder(pos=(1.25+2.5*self.b.players[0][1]-1.25*width,1.25+2.5*self.b.players[0][0]-1.25*height,.2),axis=(0,0,1),radius=.75,color=color.white),\
                        cylinder(pos=(1.25+2.5*self.b.players[1][1]-1.25*width,1.25+2.5*self.b.players[1][0]-1.25*height,.2),axis=(0,0,1),radius=.75,color=color.black)]
        self.playerType = ["AI" if playerOne == 'AI' else "Human", "AI" if playerTwo == "AI" else "Human"]
    def waitInput(self):
        """ waits for input from player then returns an array [type selected, x position, y position]
        """
        while True:
            rate(100)
            if scene.mouse.clicked:
                m = scene.mouse.getclick()
                obj = scene.mouse.pick
                if obj.__class__ == box:
                    if obj.size == (2,2,.1):
                        for y in range(len(q.tiles)):
                            for x in range(len(q.tiles[0])):
                                if q.tiles[y][x] == obj:
                                    return ["tile",x,y]
                    if obj.size == (.5,2,.05):
                        for y in range(len(q.vWalls)):
                            for x in range(len(q.vWalls[0])):
                                if q.vWalls[y][x] == obj:
                                    return ["vWalls",x,y]
                    if obj.size == (2,.5,.05):
                        for y in range(len(q.hWalls)):
                            for x in range(len(q.hWalls[0])):
                                if q.hWalls[y][x] == obj:
                                    return ["hWalls",x,y]

    def AIInput(self,p):
        """ makes move for AI player
        :param p: player being played for
        """
        time.sleep(1)
        a = random.randint(0,1) #0 for movement 1 for wall
        if a == 0: #tries to move towards opposite end, then randomly left or right then up
            if not self.b.movePlayer(self.b.players[p][0]+(1 if p == 0 else -1),\
                                 self.b.players[p][1], p):
                a = random.randrange(-1,2,2)
                if not self.b.movePlayer(self.b.players[p][0],\
                                 self.b.players[p][1]+a, p):
                    if not self.b.movePlayer(self.b.players[p][0],\
                                 self.b.players[p][1], p):
                        self.b.movePlayer(self.b.players[p][0]+(-1 if p == 0 else 1),\
                                 self.b.players[p][1], p)
        elif a == 1: #places a random wall
            vh = random.randint(0,1) #0 for vert 1 for hor
            row = random.randint(0,self.b.height-1)
            col = random.randint(0,self.b.width-1)
            while not self.b.playWall(row,col,vh):
                row = random.randint(0,self.b.height-1)
                col = random.randint(0,self.b.width-2)

    def updateBoard(self):
        """ update board to be same as text board
        """
        for row in range(len(self.vWalls)):
            for col in range(len(self.vWalls[0])):
                if self.b.vWalls[row][col] == 1  and self.vWalls[row][col].size != (.5,2,1):
                    self.vWalls[row][col].size = (.5,2,2)
                    self.vWalls[row][col].color = color.yellow
        for row in range(len(self.hWalls)):
            for col in range(len(self.hWalls[0])):
                if self.b.hWalls[row][col] == 1  and self.hWalls[row][col].size != (.5,2,1):
                    self.hWalls[row][col].size = (2,.5,2)
                    self.hWalls[row][col].color = color.yellow
        self.players[0].pos = (1.25+2.5*self.b.players[0][1]-1.25*self.b.width,1.25+2.5*self.b.players[0][0]-1.25*self.b.height,.2)
        self.players[1].pos = (1.25+2.5*self.b.players[1][1]-1.25*self.b.width,1.25+2.5*self.b.players[1][0]-1.25*self.b.height,.2)


    def humanInput(self,p):
        """takes turn for player p
        """
        while True:
            a = self.waitInput()
            if a[0] == "tile" and self.b.movePlayer(a[2],a[1],p):
                break
            elif a[0] == "hWalls" and self.b.playWall(a[2], a[1],1):
                break
            elif a[0] == "vWalls" and self.b.playWall(a[2], a[1],0):
                break

    def takeTurn(self,p):
        if self.playerType[p] == "AI":
            self.AIInput(p)
        elif self.playerType[p] == "Human":
            self.humanInput(p)


    def hostGame(self):
        """plays game
        """
        i = 0
        p = 0
        while self.b.checkWin() == 0:
            self.takeTurn(p)
            sleep(0.01) # becca added sleep
            self.updateBoard()
            p = 1 if p == 0 else 0
            i += 1
            print i
        text(text=('Player ' + str(self.b.checkWin()) + ' Wins!'), pos=(0,0,2), align='center', color=color.green)

#q = visualBoard(9,9,"Human","AI")


q = visualBoard(9,9,"Human","AI")

q.hostGame()

#print q.checkPaths()