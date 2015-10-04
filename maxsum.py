def solution(a):
    """
    :type a: List[int]
    """
    if len(a) == 0:
        return -1
    if len(a) == 1:
        return a[0]

    max_sum = a[0]

    for i in range(len(a)):
        for j in range(i, len(a)):
            s = 0
            for k in range(i, j+1):
                s += a[k]
            if s > max_sum:
                max_sum = s

    return max_sum

print solution([2, -8, 3, -2, 4, -10])
