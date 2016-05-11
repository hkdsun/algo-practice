class Solution(object):
    def findDuplicate(self, nums):
            slow, fast, finder = nums[0], nums[nums[0]], 0

            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]

            while slow != finder:
                slow = nums[slow]
                finder = nums[finder]

            return finder

print Solution().findDuplicate([1, 2, 2, 4])
