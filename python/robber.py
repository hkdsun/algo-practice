class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = {}
        dp[0] = 0
        dp[1] = max(nums[0], nums[1])

        for k in range(2, len(nums)+1):
            dp[k] = max(dp[k-2]+nums[k-1], dp[k-1])

        return dp[k]

p = [1, 1, 1]
print Solution().rob(p)
