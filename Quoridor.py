
class board:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.hWalls = [[0]*(width) for i in range(height-1)]
        self.vWalls = [[0]*(width-1) for i in range(height)]
        self.spaces = [[' ']*width for i in range(height)]
        self.spaces[0][int(self.width/2)] = '$'
        self.spaces[self.height-1][int(self.width/2)] = '%'
    def __repr__(self):
        s = 'Quoridor\n----------\n'
        for col in range(self.width):
            s += '+-'
        s += '+\n'
        for row in range(self.height-1):
            s += '|'
            for col in range(self.width-1):
                s += self.spaces[row][col]
                s += '|' if self.vWalls[row][col] == 1 else ' '
            s += self.spaces[row][self.width-1]
            s += '|\n+'
            for col in range(self.width):
                s += '-' if self.hWalls[row][col] == 1 else ' '
                s += '+'
            s += '\n'
        s += '|'
        for col in range(self.width-1):
            s += self.spaces[self.height-1][col]
            s += '|' if self.vWalls[self.height-1][col] == 1 else ' '
        s += self.spaces[row][self.width-1]
        s += '|\n+'
        for col in range(self.width):
            s += '-'
            s += '+'
        s += '\n'
        return s

q = board(7,7)
print q