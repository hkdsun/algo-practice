# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        bad = -1
        while low <= high:
            mid = (low+high)//2
            is_bad = isBadVersion(mid)
            if is_bad:
                high = mid-1
                bad = mid
            else:
                low = mid+1
        return bad
