#! /usr/bin/env python3

# just cat the input file and pipe it to this program

def isLowPoint(heightMap, i, j):
    currentHeight = heightMap[i][j]
    lowest = True
    for neighbour in getVonNeumannNeighbours(heightMap, i, j):
        if currentHeight >= heightMap[neighbour[0]][neighbour[1]]:
            lowest = False
            break
    return lowest

def getVonNeumannNeighbours(heightMap, i, j):
    neighbours = []
    length = len(heightMap)
    width  = len(heightMap[0]) if length else 0
    if i > 0:
        neighbours.append((i-1, j))
    if i < (length-1):
        neighbours.append((i+1, j))
    if j > 0:
        neighbours.append((i, j-1))
    if j < (width-1):
        neighbours.append((i, j+1))
    return neighbours

def collectBasin(heightMap, point, basin, collected):
    if heightMap[point[0]][point[1]] == 9:
        return basin
    collected.add(point)
    basin.add(point)
    toBeCollected = set(getVonNeumannNeighbours(heightMap, point[0], 
        point[1])) - collected
    collected |= toBeCollected
    for newPoint in toBeCollected:
        collectBasin(heightMap, newPoint, basin, collected)
    return basin

if __name__ == '__main__':
    heightMap = []
    while True:
        try:
            heightMap.append([int(i) for i in input()])
        except EOFError:
            break

    length = len(heightMap)
    width  = len(heightMap[0]) if length else 0

    investigatedPoints = set()
    top3Basins = []

    for i in range(length):
        for j in range(width):
            if (i,j) in investigatedPoints:
                continue
            if isLowPoint(heightMap, i, j):
                basin = collectBasin(heightMap, (i,j), set(), set())
                investigatedPoints |= basin
                top3Basins.append(basin)
                if len(top3Basins) > 3:
                    top3Basins.remove(min(top3Basins, key = lambda k: len(k)))

    product = 1
    for basin in top3Basins:
        product *= len(basin)

    print(product)
