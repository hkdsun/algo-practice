def permute(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]
    res = []
    for i, c in enumerate(s):
        remain = s[:i] + s[i+1:]
        subperm = permute(remain)
        for sublist in subperm:
            res.append([c] + sublist)
    return res

chars = [1, 2,3,4,5]
p = permute(chars)
print len(p)
print p
