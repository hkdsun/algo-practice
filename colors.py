class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        i0, i1, i2 = 0, 0, len(nums)-1
        while i1 <= i2:
            if nums[i1] == 0:
                nums[i1], nums[i0] = nums[i0], nums[i1]
                i0 += 1
                i1 += 1
            elif nums[i1] == 2:
                nums[i1], nums[i2] = nums[i2], nums[i1]
                i1 += 1
                i2 -= 1
            else:
                i1 += 1
        return nums

print Solution().sortColors([2, 0])
