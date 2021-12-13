#! /usr/bin/env python3

# just cat the input file and pipe it to this program

from pprint import pprint

def getNeighbours(octopusMap, i, j):
    neighbours = []
    if i > 0:
        neighbours.append((i-1, j))
        if j > 0:
            neighbours.append((i-1, j-1))
        if j < 9:
            neighbours.append((i-1, j+1))
    if i < 9:
        neighbours.append((i+1, j))
        if j > 0:
            neighbours.append((i+1, j-1))
        if j < 9:
            neighbours.append((i+1, j+1))
    if j > 0:
        neighbours.append((i, j-1))
    if j < 9:
        neighbours.append((i, j+1))
    return neighbours

def printMap(octopusMap):
    printStr = "\n".join(["".join([(str(i) if i != 0 else "*") + " " for i in line]) for line in octopusMap])
    print(printStr)

def flash(octopusMap, i, j, flashed):
    nFlashes = 1
    flashed.append((i,j))
    for neighbour in getNeighbours(octopusMap, i, j):
        octopusMap[neighbour[0]][neighbour[1]] += 1
        if octopusMap[neighbour[0]][neighbour[1]] > 9 and neighbour not in flashed:
            nFlashes += flash(octopusMap, neighbour[0], neighbour[1], flashed)
    return nFlashes

if __name__ == '__main__':
    lines = []
    while True:
        try:
            cols = [int(i) for i in input()]
            lines.append(cols)
        except EOFError:
            break

    nFlashes = 0
    step = 1
    while True:
        flashed = []
        for i in range(10):
            for j in range(10):
                lines[i][j] += 1
                if lines[i][j] > 9 and (i,j) not in flashed:
                    nFlashes += flash(lines, i, j, flashed)
        allFlash = True
        for i in range(10):
            for j in range(10):
                if lines[i][j] > 9:
                    lines[i][j] = 0
                else:
                    allFlash = False
        if allFlash:
            break
        step += 1

    print(step)
