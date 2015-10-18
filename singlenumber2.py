class Solution(object):
    def singleNumber(self, nums):
        one, two = 0, 0
        for x in nums:
            one, two, three = one ^ x, two | (one & x), two & x
            print "first", bin(one), bin(two), bin(three)
            one, two = one & ~three, two & ~three
            print "then", bin(one), bin(two), bin(three)
        return one

n = [1, 2, 2, 2, 3, 3, 3]
print Solution().singleNumber(n)
