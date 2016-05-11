class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        l = 1
        cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == cur:
                continue
            nums[i], nums[l] = nums[l], nums[i]
            cur = nums[l]
            l += 1
        return l


nums = [1, 1, 2, 2, 2, 3, 4, 5, 5]
i = Solution().removeDuplicates(nums)
print nums[:i]
