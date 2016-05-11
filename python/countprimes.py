class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        r = [1] * (n)
        r[0], r[1] = 0, 0
        for i in range(2, n/2+1):
            if r[i]:
                for j in range(i*i, n, i):
                    r[j] = 0
        return sum(r)

print Solution().countPrimes(22)
