class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            max_sum = max(dp[i], max_sum)
        return max_sum

    def maxProduct(self, nums):
        dpmax = [0 for _ in range(len(nums))]
        dpmin = [0 for _ in range(len(nums))]
        dpmax[0], dpmin[0], max_p = nums[0], nums[0], nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                dpmax[i] = max(dpmin[i-1]*nums[i], nums[i])
                dpmin[i] = min(dpmax[i-1]*nums[i], nums[i])
            else:
                dpmax[i] = max(dpmax[i-1]*nums[i], nums[i])
                dpmin[i] = min(dpmin[i-1]*nums[i], nums[i])
            max_p = max(max_p, dpmax[i])
        return max_p

l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
l = [2, 3, -2, 4]
print Solution().maxSubArray(l)
print Solution().maxProduct(l)
