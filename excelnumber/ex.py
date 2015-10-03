s = "AAA"
length = len(s)
res = 0

for i,c in enumerate(s):
    res += (ord("A") - 64) * (26 ** (length-1-i))

print res
