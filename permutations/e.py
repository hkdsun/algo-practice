def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1)


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    for i, n in enumerate(nums):
        res = []
        for j in nums:
            res = nums[:i] + [j] + nums[i+1:]
            print nums[:i]
            print nums[i+1:]
            print res



print fact(3)
permute([1, 2, 3])
