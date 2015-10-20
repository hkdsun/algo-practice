class Solution(object):
    def _sift_down(self, nums, node, end):
        max_i = left = node*2+1
        right = left + 1

        if left > end:
            return

        if right <= end:
            if nums[right] > nums[left]:
                max_i = right

        if nums[node] < nums[max_i]:
            nums[node], nums[max_i] = nums[max_i], nums[node]
            self._sift_down(nums, node, end)
        return

    def heapify(self, nums, start, end):
        mid = (end-start)//2
        for i in range(mid, -1, -1):
            self._sift_down(nums, i, end-1)
        return

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.heapify(nums, 0, len(nums))
        res = 0
        for i in range(len(nums)-1, -1, -1):
            if len(nums)-k-i == 0:
                return nums[0]
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, 0, i)

nums = [3, 2, 1, 9, 2, 7, 4]
print Solution().findKthLargest(nums, 2)
