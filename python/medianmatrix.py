def merge(list1, list2):
    res = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    if i < len(list1):
        while i < len(list1):
            res.append(list1[i])
            i += 1
    elif j < len(list2):
        while j < len(list2):
            res.append(list2[j])
            j += 1
    return res


def solution(matrix):
    """
    :type matrix: List[List[int]]
    :rtype int
    """

    if len(matrix) == 0:
        return -1
    if len(matrix[0]) == 0:
        return -1

    res = list(matrix[0])
    n = len(matrix)
    m = len(matrix[0])

    for row in range(1, len(matrix)):
        res = merge(matrix[row], res)

    mn = m * n
    if mn % 2 == 0:
        return (res[mn/2-1] + res[mn/2+1])/2
    else:
        return res[mn/2]


r1 = [1, 2, 3, 4]
r2 = [5, 7, 8, 11]
r3 = [6, 15, 16, 20]
r4 = [10, 21, 23, 24]
m = [r1, r2, r3, r4]
sol = solution(m)
print sol
ans = sorted(r1 + r2 + r3 + r4)
print ans
med = 0
if len(ans) % 2 == 0:
    med = (ans[len(ans)/2-1] + ans[len(ans)/2+1])/2
else:
    med = ans[len(ans)/2]

print med == sol
