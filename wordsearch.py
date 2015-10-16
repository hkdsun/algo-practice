class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not any(board):
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j):
                    return True
        return False

    def dfs(self, board, word, i, j):
        nrows = len(board)
        ncols = len(board[0])
        if len(word) == 0:
            return True
        if i < 0 or i >= nrows or j < 0 or j >= ncols or board[i][j] != word[0]:
            return False
        tmp = board[i][j]
        board[i] = board[i][:j] + '#' + board[i][j+1:]
        res = self.dfs(board, word[1:], i+1, j) or self.dfs(board, word[1:], i-1, j) or self.dfs(board, word[1:], i, j+1) or self.dfs(board, word[1:], i, j-1)
        board[i] = board[i][:j] + tmp + board[i][j+1:]
        return res


board = ["ABCE",
         "SFCS",
         "ADEE"]
print Solution().exist(board, "ABCCED")
print Solution().exist(board, "SS")
print Solution().exist(board, "ABCESEEDAS")
print Solution().exist(board, "ABCESEEDASA")
