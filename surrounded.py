class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return
        nrows = len(board)
        ncols = len(board[0])
        save = [(i, 0) for i in range(nrows)] + [(0, j) for j in range(ncols)]
        save += [(nrows-1, j) for j in range(ncols)] + [(i, ncols-1) for i in range(nrows)]

        while save:
            y, x = save.pop()
            if x < 0 or x >= ncols or y < 0 or y >= nrows:
                continue
            elif board[y][x] == 'O':
                new_str = list(board[y])
                new_str[x] = 'S'
                board[y] = ''.join(new_str)
                save += [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]
        board[:] = [['XO'[c == 'S'] for c in row] for row in board]

board = ["XOXOXO", "OXOXOX", "XOXOXO", "OXOXOX"]
Solution().solve(board)
for i in board:
    print ' '.join(map(str, i))
