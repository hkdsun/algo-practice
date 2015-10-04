def solution(st):
    if len(st) == 1:
        return st
    perms = []
    for i in range(len(st)):
        for word in solution(st[:i]+st[i+1:]):
            perms.append(st[i]+word)
    return perms


print solution("lfksjdf")
