#! /usr/bin/env python3

# just cat the input file and pipe it to this program

nSoughtValues = 0

if __name__ == '__main__':
    while True:
        try:
            outputDigits = input().split(' | ')[1].split(' ')
        except EOFError:
            break
        for digit in outputDigits:
            if len(digit) in {2, 4, 3, 7}:
                nSoughtValues += 1

print(nSoughtValues)
