def permutestr(string):
    if len(string) == 2:
        return [string[0]+string[1], string[1]+string[0]]
    res = []
    for i in range(len(string)):
        perms = permutestr(string[:i] + string[i+1:])
        for word in perms:
            res.append(string[i]+word)
    return res

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) == 2:
        return [[nums[0], nums[1]], [nums[1], nums[0]]]
    res = []
    for i, n in enumerate(nums):
        permutations = permute(nums[:i] + nums[i+1:])
        for i in permutations:
            r = [n] + i
            res.append(r)
    return res

print permute([1, 2, 3, 4])
print len(permute([1, 2, 3, 4]))
print permutestr("HORMOZ")
