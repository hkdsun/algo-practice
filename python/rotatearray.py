class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        pivot = n - k
        left = nums[pivot:]
        right = nums[:pivot]
        nums[:n - pivot] = left
        nums[n - pivot:] = right

l = [1, 2, 3, 4]
Solution().rotate(l, 2)
print l
