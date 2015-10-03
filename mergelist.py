class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not n:
            return
        i1, i2, r = m-1, n-1, m+n-1
        while r > i1:
            if i1 < 0:
                break
            if nums1[i1] > nums2[i2]:
                nums1[r], nums1[i1] = nums1[i1], nums1[r]
                i1 -= 1
                r -= 1
            else:
                nums1[r] = nums2[i2]
                i2 -= 1
                r -= 1
        if i1 < 0:
            while r > -1:
                nums1[r] = nums2[i2]
                i2 -= 1
                r -= 1

n2 = [1]
n1 = [2] + [0]*len(n2)
Solution().merge(n1, len(n1)-len(n2), n2, len(n2))
print n1
