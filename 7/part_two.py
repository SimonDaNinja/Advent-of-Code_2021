#! /usr/bin/env python3

# just cat the input file and pipe it to this program

from math import inf

crabPositions = [int(i) for i in input().split(',')]

def triangular(n):
    return n*(n+1)//2

bestCumulativeDistance = inf
bestDestination = None
minCrab = min(crabPositions)
maxCrab = max(crabPositions)
nDestinations = maxCrab-minCrab + 1
for destination in range(min(crabPositions), max(crabPositions)+1):
    percentDone = int(100*(destination-minCrab)/nDestinations)
    print(f"{percentDone} % done", end='\r')
    cumulativeDistance = sum([triangular(abs(destination - crabPosition)) for 
                                crabPosition in crabPositions])
    if cumulativeDistance < bestCumulativeDistance:
        bestDestination = destination
        bestCumulativeDistance = cumulativeDistance

print(f"\n{bestCumulativeDistance}")
