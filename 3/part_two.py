#! /usr/bin/env python3

# just cat the input file and pipe it to this program

diagnostic = input()
diagnosticLength = len(diagnostic)

diagnostics = [diagnostic]

while True:
    try:
        diagnostic = input()
    except EOFError:
        break
    diagnostics.append(diagnostic)

diagnosticsForOxygen = diagnostics.copy()

for bit in range(diagnosticLength):
    if len(diagnosticsForOxygen) == 1:
        break
    stats=0
    for diagnostic in diagnosticsForOxygen:
        stats += 1 if diagnostic[bit] == '1' else -1
    commonBit = '0' if stats < 0 else '1'
    for diagnostic in diagnosticsForOxygen.copy():
        if diagnostic[bit] != commonBit:
            diagnosticsForOxygen.remove(diagnostic)

oxygenRating = int(diagnosticsForOxygen[0],2)

diagnosticsForCo2 = diagnostics.copy()

for bit in range(diagnosticLength):
    if len(diagnosticsForCo2) == 1:
        break
    stats=0
    for diagnostic in diagnosticsForCo2:
        stats += 1 if diagnostic[bit] == '1' else -1
    commonBit = '0' if stats < 0 else '1'
    for diagnostic in diagnosticsForCo2.copy():
        if diagnostic[bit] == commonBit:
            diagnosticsForCo2.remove(diagnostic)

co2Rating = int(diagnosticsForCo2[0],2)

print(oxygenRating*co2Rating)
