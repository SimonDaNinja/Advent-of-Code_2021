#! /usr/bin/env python3

# just cat the input file and pipe it to this program

if __name__ == '__main__':
    heightMap = []
    while True:
        try:
            heightMap.append([int(i) for i in input()])
        except EOFError:
            break

    length = len(heightMap)
    width  = len(heightMap[0]) if length else 0

    lowPointRiskLevels = []

    for i in range(length):
        for j in range(width):
            currentHeight = heightMap[i][j]
            lowest = True
            if i > 0:
                if currentHeight >= heightMap[i-1][j]:
                    lowest = False
            if i < (length-1):
                if currentHeight >= heightMap[i+1][j]:
                    lowest = False
            if j > 0:
                if currentHeight >= heightMap[i][j-1]:
                    lowest = False
            if j < (width-1):
                if currentHeight >= heightMap[i][j+1]:
                    lowest = False
            if lowest:
                lowPointRiskLevels.append(1 + currentHeight)

    print(sum(lowPointRiskLevels))
