#! /usr/bin/env python3

# just cat the input file and pipe it to this program

fishyBois = [int(i) for i in input().split(',')]
fishCounters = {i:fishyBois.count(i) for i in range(9)}

for i in range(256):
    zeros = fishCounters[0]
    for i in range(8):
        fishCounters[i] = fishCounters[i+1]
    fishCounters[6] += zeros
    fishCounters[8] = zeros

print(sum([fishCounters[i] for i in fishCounters]))
