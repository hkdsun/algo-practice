class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        subbedtarget = {}
        for i, c in enumerate(nums):
            subbedtarget[target-c] = i
        for i, c in enumerate(nums):
            if c in subbedtarget and i != subbedtarget[c]:
                return [i+1, subbedtarget[c]+1]
