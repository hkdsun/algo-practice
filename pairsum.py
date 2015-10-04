def solution(n, lis):
    dic = {}
    res = []
    for i in lis:
        dic[n-i] = i
    for i in lis:
        if i in dic:
            res.append((i, dic[i]))
    return res

print solution(10, [2, 9, 8, 1, 10, 0, 5, 6, 4])
