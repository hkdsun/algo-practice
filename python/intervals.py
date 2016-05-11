# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[ " + str(self.start) + ", " + str(self.end) + " ]"

    def __reprt__(self):
        return self.__str__()


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda i: i.start)
        res = [intervals[0]]
        for i in intervals:
            if self.overlaps(i, res[-1]):
                res[-1] = self.merge2(i, res[-1])
            else:
                res.append(i)
        return res

    def overlaps(self, i1, i2):
        if i1.start < i2.start:
            if i1.end+1 >= i2.start:
                return True
        elif i1.start >= i2.start:
            if i2.end+1 >= i1.start:
                return True
        return False

    def merge2(self, i1, i2):
        start = min(i1.start, i2.start)
        end = max(i1.end, i2.end)
        return Interval(start, end)

l = [Interval(1, 3), Interval(2, 6), Interval(2, 7),
     Interval(8, 10), Interval(15, 18)]

for i in Solution().merge(l):
    print i
