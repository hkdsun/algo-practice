class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        r = len(nums)-1
        l = 0
        while l < r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            l += 1
        return r

nums = [5, 1, 2, 3, 1, 4, 5, 1, 3, 1, 5, 6, 7]
nums = [1, 1, 1, 1]
i = Solution().removeElement(nums, 1)
print nums[:i]
