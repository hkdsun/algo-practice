class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            res = []
            for i in range(1, n+1):
                res.append([i])
            return res
        elif n == k:
            res = []
            for i in range(1, n+1):
                res.append(i)
            return [res]
        else:
            rs=[]
            rs+=self.combine(n-1,k)
            part=self.combine(n-1,k-1)
            for ls in part:
                ls.append(n)
            rs+=part
            return rs



print Solution().combine(6, 3)
print len(Solution().combine(6, 3))
