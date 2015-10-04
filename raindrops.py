class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0
        l = 0
        r = 0
        dip = 0
        sum = 0
        while l < len(height):
            if r == l:
                r += 1
            while r < len(height) and height[r] < height[l]:
                r += 1
            if r == len(height):
                l += 1
                r, dip = l, l
                if l == len(height):
                    break  # done
            else:
                dip += 1
                while dip != r:
                    print l, r, dip
                    sum += min(height[l], height[r]) - height[dip]
                    dip += 1
                l = dip
            print sum
        return sum


elev = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print Solution().trap(elev)
elev = [4, 3, 2]
print Solution().trap(elev)
