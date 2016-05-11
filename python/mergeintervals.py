# Definition for an interval.
class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        L = []
        d = {}
        for interval in intervals:
            if interval.start in d:
                if interval.end >= d[interval.start].end:
                    d[interval.start] = interval
            else:
                d[interval.start] = interval
                L.append(interval.start)
        L = sorted(L)
        A = [d[L[0]]]
        for i in L:
            if i < A[-1].end:
                a = min(i, A[-1].start)
                b = max(d[i].end, A[-1].end)
                inn = Interval(a, b)
                A[-1] = inn
            else:
                A.append(d[i])
        return A

    def intersect(self, i1, i2):
        i1 = self.merge(i1)
        i2 = self.merge(i2)
        L = []
        for i in i1:
            L.append(i)
        for i in i2:
            L.append(i)
        L = sorted(L, key=lambda x: x.start)
        res = []
        for i in range(len(L)-1):
            if L[i+1].start <= L[i].end:
                a = max(L[i].start, L[i+1].start)
                b = min(L[i].end, L[i+1].end)
                res.append(Interval(a, b))
        return res

l = map(lambda i: Interval(i[0], i[1]), [[2, 10], [50, 300]])
r = map(lambda i: Interval(i[0], i[1]), [[1, 5], [2, 20], [41, 100]])
print map(lambda x: [x.start, x.end], Solution().intersect(l, r))
