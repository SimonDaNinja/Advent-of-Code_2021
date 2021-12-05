#! /usr/bin/env python3

# just cat the input file and pipe it to this program

previous = None
nIncreases = 0
while True:
    try:
        nbrStr = input()
    except EOFError:
        break
    current = int(nbrStr)
    if previous is not None:
        if current > previous:
            nIncreases += 1
    previous = current
print(nIncreases)
