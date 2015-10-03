res = int(raw_input())

di = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
remain = []
while res != 0:
    n = res % 16
    if n >= 10:
        remain.append(di[n])
    else:
        remain.append(str(n))
    res = res/int(16)

print "".join(remain)
