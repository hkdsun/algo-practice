class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        last = len(triangle) - 1
        dp = [0 for _ in range(len(triangle[last]))]
        for i in range(len(triangle[last])):
            dp[i] = triangle[last][i]
        gloMin = triangle[0][0]
        for i in range(len(triangle) - 2, -1, -1):
            locMin = float("inf")
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j] + triangle[i][j], dp[j + 1] + triangle[i][j])
                locMin = min(locMin, dp[j])
            gloMin = locMin
        return gloMin


t = [[2],
     [4, 5],
     [1, 1, 1],
     [6, 1, 1, 1]]
t = [[-1], [3, 2], [1, -2, -1]]
print Solution().minimumTotal(t)
