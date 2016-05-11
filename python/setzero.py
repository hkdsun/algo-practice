class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        if not matrix[0]:
            return
        rows, cols = set(), set()
        nrows, ncols = len(matrix), len(matrix[0])
        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for row in rows:
            for i in range(ncols):
                matrix[row][i] = 0
        for col in cols:
            for i in range(nrows):
                matrix[i][col] = 0


m = [[1, 1, 1, 0, 1],
     [1, 0, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 0, 1]]

Solution().setZeroes(m)
for row in m:
    print ' '.join(map(str, row))
