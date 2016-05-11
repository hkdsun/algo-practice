class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        n = len(nums)
        while l <= r:
            if nums[r] == val:
                r -= 1
                n -= 1
                continue
            if nums[l] == val and r != l:
                nums[l], nums[r] = nums[r], nums[l]
                n -= 1
                l += 1
                r -= 1
                continue
            l += 1
        return n

l = [1, 2, 2]
i = Solution().removeElement(l, 2)
print l[:i]
