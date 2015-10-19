class Solution(object):

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        d = {str(x): [] for x in range(10)}
        maxes = {str(x): 0 for x in range(10)}
        for num in nums:
            d[num[0]].append(num)
            maxes[num[0]] = max(maxes[num[0]], len(num))
        for k, lis in d.iteritems():
            max_len = maxes[k]
            new_lis = []
            for i in range(max_len):
                res = filter(lambda x: True if len(x) == i + 1 else False, lis)
                res = sorted(res, key=int, reverse=True)
                new_lis += res
            d[k] = new_lis
        string = ""
        print d
        for i in range(9, -1, -1):
            for s in d[str(i)]:
                string += s
        return string


print Solution().largestNumber([128, 12])
