class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        n = len(nums)
        res = float("inf")
        l = r = sr = 0
        while r < n:
            sr += nums[r]
            r += 1
            print sr
            if sr >= s:
                while sr - nums[l] >= s:
                    sr -= nums[l]
                    l += 1
                res = min(res, r-l)
        return res if res != float("inf") else 0


print Solution().minSubArrayLen(3, [1, 1])
