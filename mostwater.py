class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ln = len(height)
        max_area = 0
        r = ln-1
        l = 0
        while l < r:
            max_area = max(max_area, (r-l)*min(height[r], height[l]))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return max_area

h = [1, 2, 5, 4, 5, 1, 6]

print Solution().maxArea(h)
