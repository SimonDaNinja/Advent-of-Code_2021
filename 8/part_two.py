#! /usr/bin/env python3

# just cat the input file and pipe it to this program

def getSegments2Digits(empiricalDigits):
    empirical1 = [digit for digit in empiricalDigits if len(digit) == 2][0]
    empirical4 = [digit for digit in empiricalDigits if len(digit) == 4][0]
    empirical7 = [digit for digit in empiricalDigits if len(digit) == 3][0]
    empirical8 = set('abcdefg')

    empiricalABCDF = empirical7 | empirical4

    empirical9 = [digit for digit in empiricalDigits if len(digit) == 6 and 
            empiricalABCDF.issubset(digit)][0]

    empirical0 = [digit for digit in empiricalDigits if len(digit) == 6 and
            digit != empirical9 and empirical1.issubset(digit)][0]

    empirical5 = [digit for digit in empiricalDigits if len(digit) == 5 and 
            (empirical9-empirical1).issubset(digit)][0]

    empirical6 = [digit for digit in empiricalDigits if digit != empirical8
            and (empirical8-empirical7).issubset(digit)][0]
    segments2Digits =   {
                            tuple(sorted(empirical0)) : 0,
                            tuple(sorted(empirical1)) : 1,
                            tuple(sorted(empirical4)) : 4,
                            tuple(sorted(empirical5)) : 5,
                            tuple(sorted(empirical6)) : 6,
                            tuple(sorted(empirical7)) : 7,
                            tuple(sorted(empirical8)) : 8,
                            tuple(sorted(empirical9)) : 9
                        }
    for digit in empiricalDigits:
        if tuple(sorted(digit)) not in segments2Digits:
            if empirical1.issubset(digit):
                segments2Digits[tuple(sorted(digit))] = 3
            else:
                segments2Digits[tuple(sorted(digit))] = 2
    return segments2Digits


if __name__ == '__main__':
    outputSum = 0
    while True:
        try:
            inputDigitString, outputDigitString = input().split(' | ')
        except EOFError:
            break
        digits = [set(i) for i in inputDigitString.split()]
        outputDigits = [set(i) for i in outputDigitString.split()]
        segments2Digits = getSegments2Digits(digits)
        for i, digit in enumerate(outputDigits):
            outputSum += 10**(3-i)*segments2Digits[tuple(sorted((digit)))]

    print(outputSum)
