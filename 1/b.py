#! /usr/bin/env python3

previousWindow = []
nIncreases = 0

while True:
    try:
        nbrStr = input()
    except EOFError:
        break
    currentNbr = int(nbrStr)
    if len(previousWindow) == 3:
        currentWindow = previousWindow[1:] + [currentNbr]
        if sum(currentWindow) > sum(previousWindow):
            nIncreases += 1
        previousWindow = currentWindow
    else:
        previousWindow.append(currentNbr)
        
print(nIncreases)