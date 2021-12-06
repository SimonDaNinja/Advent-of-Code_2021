#! /usr/bin/env python3

# just cat the input file and pipe it to this program

fishyBois = [int(i) for i in input().split(',')]

for i in range(80):
    for j, fish in enumerate(fishyBois.copy()):
        if not fish:
            fishyBois.append(8)
            fishyBois[j] = 6
        else:
            fishyBois[j] = fish-1

print(len(fishyBois))
