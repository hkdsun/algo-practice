REP = {0: ".", 1: "R", 2: "Y"}

def diagonalsPos(matrix, cols, rows):
    """Get positive diagonals, going from bottom-left to top-right."""


def diagonalsNeg(matrix, cols, rows):
    """Get negative diagonals, going from top-left to bottom-right."""


class Game:
    def __init__(self, nrows=6, ncols=7):
        self.cols = ncols
        self.rows = nrows
        self.turn = 1
        self.board = [[0 for x in xrange(nrows)] for x in xrange(ncols)]

    def insert(self, col, color):
        column = self.board[col]
        i = 0
        while i < len(column)-1 and column[i+1] == 0:
            i += 1
        column[i] = color


    def next_round(self):
        if self.winner():
            return False
        self.pretty()
        column = int(input('{}\'s turn: '.format(REP[1] if self.turn == 1 else REP[2])))
        self.insert(column, self.turn)
        self.turn = 1 if self.turn == 2 else 2
        return True

    def winner(self):


    def pretty(self):
        print ' '.join(map(str, range(self.cols)))
        for y in range(self.rows):
            print(' '.join(REP[self.board[x][y]] for x in range(self.cols)))


if __name__ == "__main__":
    g = Game()
    while g.next_round():
        True
