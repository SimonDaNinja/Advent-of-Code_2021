#! /usr/bin/env python3

# just cat the input file and pipe it to this program

import numpy as np

directions =    {
                    'forward' : np.array([1,0]),
                    'up' : np.array([0,-1]),
                    'down' : np.array([0,1]),
                }

position = np.array([0,0])

while True:
    try:
        instruction = input()
    except EOFError:
        break
    directionStr, multiplierStr = instruction.split(' ')
    multiplier = int(multiplierStr)
    position += directions[directionStr]*multiplier

print(position[0]*position[1])

