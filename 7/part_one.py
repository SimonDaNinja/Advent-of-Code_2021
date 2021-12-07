#! /usr/bin/env python3

# just cat the input file and pipe it to this program

from math import inf

crabPositions = [int(i) for i in input().split(',')]

bestCumulativeDistance = inf
bestDestination = None
for destination in range(min(crabPositions), max(crabPositions)+1):
    cumulativeDistance = sum([abs(destination - crabPosition) for 
                                crabPosition in crabPositions])
    if cumulativeDistance < bestCumulativeDistance:
        bestDestination = destination
        bestCumulativeDistance = cumulativeDistance

print(bestCumulativeDistance)
