class Solution(object):
    def heapsort(self, nums):
        self.heapify(nums, 0, len(nums))
        for i in range(len(nums)-1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, 0, i)
        return

    def heapify(self, nums, start, end):
        mid = (end-start)//2
        for i in range(mid, -1, -1):
            self._sift_down(nums, i, end)
        return

    def _sift_down(self, nums, node, end):
        end = end - 1
        m = left = node*2+1
        right = left + 1

        if left > end:
            return

        if right <= end:
            if nums[right] > nums[left]:
                m = right

        if nums[node] < nums[m]:
            nums[node], nums[m] = nums[m], nums[node]
            self._sift_down(nums, m, end)
        else:
            return

nums = [46, 52, 28, 17, 3, 63, 34, 81, 70, 95]
Solution().heapsort(nums)
print nums
