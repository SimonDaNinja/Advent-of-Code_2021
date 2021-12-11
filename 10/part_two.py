#! /usr/bin/env python3

# just cat the input file and pipe it to this program

openToClose =  {
                    '(':')',
                    '<':'>',
                    '[':']',
                    '{':'}'
                }

closeToScore = {
                    ')':1,
                    ']':2,
                    '}':3,
                    '>':4
                }
            

if __name__ == '__main__':
    scores = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        opens = []
        corrupt = False
        for character in line:
            if character in openToClose:
                opens.append(character)
            elif openToClose[opens[-1]] != character:
                score += closeToScore[character]
                corrupt = True
                break
            else:
                opens.pop(-1)
        if corrupt:
            continue
        opens.reverse()
        score = 0
        for character in opens:
            score *= 5
            score += closeToScore[openToClose[character]]
        scores.append(score)

    scores.sort()
    middleScore = scores[len(scores)//2]

    print(middleScore)
