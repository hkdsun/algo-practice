REP = {0: ".", 1: "R", 2: "Y"}


class Game:
    def __init__(self, nrows=6, ncols=7):
        self.cols = ncols
        self.rows = nrows
        self.board = [[0]*ncols]*nrows

    def continues():


    def pretty(self):
        print ' '.join(map(str, range(self.cols)))
        for cols in self.board:
            print ' '.join(map(lambda x: REP[x], cols))


if __name__ == "__main__":
    g = Game()
    g.pretty()
    while(g.continues()):
        # Gameplay

    print "Player with", g.winner, "wins!"
