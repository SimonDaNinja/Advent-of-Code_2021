#! /usr/bin/env python3

# just cat the input file and pipe it to this program

class BingoSquare:
    def __init__(self, value, marked = False):
        self.value = value
        self.marked = marked

    def __str__(self):
        return (' ' if self.value < 10 else '') + str(self.value) + '(' + ('X' if self.marked else ' ') + ')'

    def __repr__(self):
        return self.__str__()

    def unmark(self):
        self.marked = False

    def mark(self):
        self.marked = True

    def __eq__(self, other):
        if type(other) is BingoSquare:
            return self.value == other.value and self.marked == other.marked
        else:
            return self.value == other

    def __bool__(self):
        return self.marked


class BingoBoard:
    def __init__(self, boardInitializer):
        self.board = [[BingoSquare(j) for j in i] for i in boardInitializer]
        self.height = len(self.board)
        self.width = len(self.board[0])

    def __getitem__(self, index):
        return self.board[index]

    def __str__(self):
        return '\n'.join([' '.join([str(square) for square in line]) for line in self.board])

    def __repr__(self):
        return self.__str__()

    def isBingo(self):
        # see if any of the lines is bingo
        for line in self.board:
            isBingo = True
            for square in line:
                if not square:
                    isBingo = False
                    break
            if isBingo:
                return True
        # see if any of the columns is bingo
        for j in range(self.width):
            isBingo = True
            for i in range(self.height):
                if not self[i][j]:
                    isBingo = False
                    break
            if isBingo:
                return True

    def mark(self, number):
        for line in self.board:
            for square in line:
                if square == number:
                    square.mark()
        return self.getScore(number)

    def getScore(self, number):
        if self.isBingo():
            return number*sum([sum([0 if square else square.value for square in line]) for line in self.board])
        return 0

drawSeries = [int(i) for i in input().split(',')]

boards = []
boardInitializer = []

doLoop = True
while doLoop:
    try:
        line = input()
    except EOFError:
        line = ''
        doLoop = False
    if line:
        boardLine = [int(i) for i in line.split()]
        boardInitializer.append(boardLine)
    elif boardInitializer:
        boards.append(BingoBoard(boardInitializer))
        boardInitializer = []

for draw in drawSeries:
    for board in boards:
        score = board.mark(draw)
        if score > 0:
            print(board)
            print(score)
            exit()
