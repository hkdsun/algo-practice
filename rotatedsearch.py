class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if target < nums[0]:
            for icur in range(len(nums)-1, -1, -1):
                cur = nums[icur]
                inext = icur-1
                next = nums[inext]
                if cur == target:
                    return icur
                if next == target:
                    return inext
                if cur < next or inext == 0:
                    return -1
        else:
            for icur in range(len(nums)):
                cur = nums[icur]
                inext = icur+1
                next = nums[inext]
                if cur == target:
                    return icur
                if next == target:
                    return inext
                if cur > next or inext == len(nums)-1:
                    return -1

print Solution().search([1], 0)
print Solution().search([0], 1)
print Solution().search([1, 3], 3)
