#! /usr/bin/env python3

# just cat the input file and pipe it to this program

X = 0
Y = 1

class Grid:

    def __init__(self, gridPoints={}):
        self.gridPoints = gridPoints
        self.maxX = 0
        self.maxY = 0

    def addPoint(self, gridPoint):
        if gridPoint not in self.gridPoints:
            self.maxX = max(self.maxX, gridPoint[X])
            self.maxY = max(self.maxY, gridPoint[Y])
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

def isHorizontal(line):
    return line[0][X] == line[1][X]

def isVertical(line):
    return line[0][Y] == line[1][Y]

def isHorizontalOrVertical(line):
    return isHorizontal(line) or isVertical(line)

grid = Grid()

while True:
    try:
        lineStr = input()
    except EOFError:
        break
    line = tuple(tuple(int(i) for i in point.split(',')) for point in lineStr.split(' -> '))
    if isHorizontal(line):
        x = line[0][X]
        yStart = min(line[0][Y], line[1][Y])
        yStop = max(line[0][Y], line[1][Y])
        for y in range(yStart, yStop+1):
            grid[(x,y)] += 1
    elif isVertical(line):
        y = line[0][Y]
        xStart = min(line[0][X], line[1][X])
        xStop = max(line[0][X], line[1][X])
        for x in range(xStart, xStop+1):
            grid[(x,y)] += 1

print(len([gridPoint for gridPoint in grid.gridPoints if grid[gridPoint] >= 2]))
