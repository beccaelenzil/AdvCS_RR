from visual import *


from visual import *
import random

def spinBoxes():
    boxList = []
    for boxNumber in range(10):
        x = random.randint(-5, 5) # integer between -5,5
        y = random.randint(-5, 5)
        z = random.randint(-5, 5)
        red = random.random()     # real number between 0 & 1
        green = random.random()
        blue = random.random()
        newBox = box(pos = vector(x, y, z),
                     color = (red, green, blue) )
        boxList.append(newBox)
    while True:
        for myBox in boxList:
            rate(60)
            myBox.rotate(angle=pi/100)
spinBoxes()