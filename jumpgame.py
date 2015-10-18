class Solution(object):

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        for idx in range(len(nums) - 2, -1, -1):
            locMin = float("inf")
            for i in range(0, min(nums[idx], len(nums) - idx - 1)):
                locMin = min(dp[idx + i + 1] + 1, locMin)
            dp[idx] = locMin
        return dp[0]

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        step = nums[0]
        for i in range(len(nums)):
            step -= 1
            if step < 0:
                return False
            step = max(step, nums[i])
        return True

print Solution().canJump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0])
print Solution().canJump([0, 1])
print Solution().canJump([2, 5, 0, 0])
print Solution().canJump([2, 0])
print Solution().canJump([1])
print Solution().canJump([2, 3, 1, 1, 4])
print Solution().canJump([3, 2, 1, 0, 4])
# print Solution().jump([2, 3, 1, 5, 3, 1, 1, 2, 1])
# print Solution().jump([2, 3, 1, 1, 4])
