class Solution(object):

    # Iterative
    def binarySearch2(self, nums, target):
        if len(nums) == 0:
            return False
        low = 0
        high = len(nums) - 1
        while True:
            if low > high:
                return False
            mid = (high + low) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

    # Recursive
    def binarySearch1(self, nums, target):
        if len(nums) == 0:
            return False
        return self.search(nums, 0, len(nums) - 1, target)

    def search(self, nums, a, b, target):
        mid = (b + a) // 2
        if nums[mid] == target:
            return True
        if b - a < 1:
            return False
        elif nums[mid] < target:
            return self.search(nums, mid + 1, b, target)
        else:
            return self.search(nums, a, mid - 1, target)

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.find_first(nums, target), self.find_last(nums, target)]

    def find_last(self, nums, target):
        i = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
            if nums[mid] == target:
                i = mid
        return i

    def find_first(self, nums, target):
        i = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
            if nums[mid] == target:
                i = mid
        return i


print Solution().searchRange([1, 2, 2], 2)
