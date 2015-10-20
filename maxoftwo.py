class Solution(object):
    def findMax(self, a, b):
        x = a ^ b
        mask = 1 << 31
        idx = -1
        for i in range(32, -1, -1):
            if (mask & x) == 1:
                idx = i
                break
            mask = mask >> 1
        print idx


Solution().findMax(10, 10)

