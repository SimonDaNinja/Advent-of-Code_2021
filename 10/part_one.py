#! /usr/bin/env python3

# just cat the input file and pipe it to this program

openToClose =  {
                    '(':')',
                    '<':'>',
                    '[':']',
                    '{':'}'
                }

closeToScore = {
                    ')':3,
                    '>':25137,
                    ']':57,
                    '}':1197
                }
            

if __name__ == '__main__':
    score = 0
    while True:
        try:
            line = input()
        except EOFError:
            break
        opens = []
        for character in line:
            if character in openToClose:
                opens.append(character)
            elif openToClose[opens[-1]] != character:
                score += closeToScore[character]
                break
            else:
                opens.pop(-1)

    print(score)
