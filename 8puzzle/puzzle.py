import copy
import random

all_moves = {
    'left'  : (0, -1),
    'right' : (0, 1),
    'up'    : (-1, 0),
    'down'  : (1, 0)
}

class Board(object):
    def __init__(self, state):
        self.state = state

    @staticmethod
    def encode(state):
        return Board([state[i:i+3] for i in range(0, 9, 3)])

    @staticmethod
    def decode(board):
        return [x for sublist in board.state for x in sublist]

    @staticmethod
    def is_legal(new_r, new_c):
        return (new_r in range(3) and new_c in range(3))

    @staticmethod
    def random(moves=1000):
        board = Board.encode([1,2,3,4,5,6,7,8,-1])
        while moves > 0:
            board = board.move(random.choice(board.get_available_moves()))
            moves -= 1
        return board

    def hashable_state(self):
        return str(self.state)

    def is_solved(self):
        return Board.decode(self) == range(1, 9) + [-1]

    def get_empty_rc(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == -1:
                    return (i, j)

    def move(self, direction):
        new_r, new_c = old_r, old_c = self.get_empty_rc()
        new_r += all_moves[direction][0]
        new_c += all_moves[direction][1]

        if not Board.is_legal(new_r, new_c):
            raise Exception("Illegal move attempted")

        new_board = copy.deepcopy(self)
        state = new_board.state

        old_value = state[new_r][new_c]
        state[new_r][new_c] = -1
        state[old_r][old_c] = old_value

        return new_board

    def get_available_moves(self):
        legal_moves = []
        new_r, new_c = self.get_empty_rc()
        for direction, rc in all_moves.iteritems():
            new_r += rc[0]
            new_c += rc[1]
            if Board.is_legal(new_r, new_c):
                legal_moves.append(direction)
            new_r, new_c = self.get_empty_rc()
        return legal_moves

def solve(board):
    queue = [board]
    seen = set()
    parents = {}
    while queue:
        board = queue.pop(0)
        available_moves = board.get_available_moves()
        for direction in available_moves:
            new_board = board.move(direction)
            if (new_board.hashable_state(), direction) not in seen:
                queue.append(new_board)
                seen.add((new_board.hashable_state(), direction))
                parents[new_board] = (board, direction)
                if new_board.is_solved():
                    b = new_board
                    res = []
                    while b in parents:
                        res.append(parents[b][1])
                        b = parents[b][0]
                    res = res[::-1]
                    return res


board = Board.random()

for row in board.state:
    print ' '.join(map(lambda x: str(x), row))

print solve(board)
