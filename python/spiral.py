class Solution(object):

    def done(self, left, right, top, bottom):
        if left >= right or top >= bottom:
            return True
        return False

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        if not matrix[0]:
            return []
        nrows, ncols = len(matrix), len(matrix[0])
        top, left = 0, 0
        right, bottom = ncols, nrows
        res = []
        while True:
            for j in range(left, right):
                res.append(matrix[top][j])
            top += 1
            if self.done(left, right, top, bottom):
                break
            for j in range(top, bottom):
                res.append(matrix[j][right-1])
            right -= 1
            if self.done(left, right, top, bottom):
                break
            for j in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][j])
            bottom -= 1
            if self.done(left, right, top, bottom):
                break
            for j in range(bottom-1, top-1, -1):
                res.append(matrix[j][left])
            left += 1
            if self.done(left, right, top, bottom):
                break
        return res

l = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20]]

print Solution().spiralOrder(l)
