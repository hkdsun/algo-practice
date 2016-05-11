class Solution(object):
    def climbStairs(self, n, count = {}):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        if n == 2:
            return 2
        if (n-1) not in count:
            count[n-1] = self.climbStairs(n-1, count)
        if (n-2) not in count:
            count[n-2] = self.climbStairs(n-2, count)
        count = count[n-1] + count[n-2]
        return count

print Solution().climbStairs(35)
