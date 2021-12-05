#! /usr/bin/env python3

# just cat the input file and pipe it to this program

import numpy as np

X = 0
Y = 1

class Grid:

    def __init__(self, gridPoints={}):
        self.gridPoints = gridPoints
        self.maxX = 0
        self.maxY = 0

    def addPoint(self, gridPoint):
        self.maxX = max(self.maxX, gridPoint[X])
        self.maxY = max(self.maxY, gridPoint[Y])
        if gridPoint not in self.gridPoints:
            self.gridPoints[gridPoint] = 0

    def __getitem__(self, key):
        if key not in self.gridPoints:
            return 0
        return self.gridPoints[key]

    def __setitem__(self, key, val):
        self.addPoint(key)
        self.gridPoints[key] = val

    def __str__(self):
        printStrings = []
        for y in range(self.maxY+1):
            printString = ''
            for x in range(self.maxX+1):
                printString += str(self[(x,y)]) if self[x,y] != 0 else '.'
            printStrings.append(printString)
        return '\n'.join(printStrings)

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    grid = Grid()

    while True:
        try:
            lineStr = input()
        except EOFError:
            break
        line = tuple(tuple(int(i) for i in point.split(',')) for point in lineStr.split(' -> '))

        point1 = line[0]
        point2 = line[1]

        x, y   = point1
        x2, y2 = point2

        yStep = np.sign(y2-y)
        xStep = np.sign(x2-x)

        nSteps = max(abs(y2-y), abs(x2-x))+1

        for i in range(nSteps):
            grid[(x,y)] += 1
            x += xStep
            y += yStep

    print(len([gridPoint for gridPoint in grid.gridPoints if grid[gridPoint] >= 2]))
