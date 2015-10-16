class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [1 for _ in range(n)]
        right = [1 for _ in range(n)]
        for i in range(1, n):
            left[i] *= left[i-1]*nums[i-1]
        for i in range(n-2, -1, -1):
            right[i] *= right[i+1]*nums[i+1]
        out = map(lambda x: x[0]*x[1], zip(left, right))
        return out


l = [1, 2, 3, 4, 5]
print Solution().productExceptSelf(l)
