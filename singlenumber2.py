class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        for i in nums:
            res ^= i
        return res

n = [1, 2, 2, 2, 3, 3, 3]
print Solution().singleNumber(n)