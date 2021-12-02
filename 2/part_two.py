#! /usr/bin/env python3

# just cat the input file and pipe it to this program

aim = 0
horizontal = 0
depth = 0

while True:
    try:
        instruction = input()
    except EOFError:
        break
    directionStr, multiplierStr = instruction.split(' ')
    multiplier = int(multiplierStr)
    if directionStr == 'up':
        aim -= multiplier
    elif directionStr == 'down':
        aim += multiplier
    else:
        depth += multiplier*aim
        horizontal += multiplier

print(horizontal*depth)

