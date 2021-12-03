#! /usr/bin/env python3

# just cat the input file and pipe it to this program

diagnostic = input()
diagnosticLength = len(diagnostic)

stats = [1 if i == '1' else -1 for i in diagnostic]

while True:
    try:
        diagnostic = input()
    except EOFError:
        break
    for i in range(diagnosticLength):
        stats[i] += 1 if diagnostic[i] == '1' else -1

gamma = 0
epsilon = 0

stats.reverse()

for i in range(diagnosticLength):
    if stats[i] > 0:
        gamma += 2**i
    else:
        epsilon += 2**i

print(gamma*epsilon)
