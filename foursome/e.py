def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    ss = sorted(nums)

    sols = set()
    dic = {}
    for s in ss:
        dic[target-s]=s
    for s in ss:
        if s in dic:
            sols.add(frozenset([s, dic[s]]))
    return sols

s=[1,0,-1,0,-2,2]
print twoSum(s,0)
