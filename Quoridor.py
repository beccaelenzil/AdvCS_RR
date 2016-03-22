
class board:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.hWalls = [[0]*(width-2) for i in range(height-2)]
        self.vWalls = [[0]*(width-2) for i in range(height-2)]
        self.fPawn = [0,int(width/2)]
        self.sPawn = [height-1,int(width/2)]

    def __repr__(self):
        for row in range(7):
            