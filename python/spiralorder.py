class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        nrows = len(matrix)
        ncols = len(matrix[0])
        br, bl, bu, bd = ncols, -1, 0, nrows
        count = nrows * ncols
        i, j = 0, 0
        right, down, left, up = True, False, False, False
        res = []
        while count > -1:
            while right:
                if j == br:
                    right, down = False, True
                    br -= 1
                    j -= 1
                    i += 1
                    break
                res.append(matrix[i][j])
                j += 1
                count -= 1
            while down:
                if i == bd:
                    down, left = False, True
                    bd -= 1
                    i -= 1
                    j -= 1
                    break
                res.append(matrix[i][j])
                i += 1
                count -= 1
            while left:
                if j == bl:
                    left, up = False, True
                    bl += 1
                    j += 1
                    i -= 1
                    break
                res.append(matrix[i][j])
                j -= 1
                count -= 1
            while up:
                if i == bu:
                    up, right = False, True
                    bu += 1
                    i += 1
                    break
                res.append(matrix[i][j])
                i -= 1
                count -= 1
        return res

matrix = [[00, 01, 02, 03],
          [10, 11, 12, 13],
          [20, 21, 22, 23],
          [30, 31, 32, 33],
          [40, 41, 42, 43]]

print Solution().spiralOrder(matrix)
