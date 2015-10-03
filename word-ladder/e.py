length = 2

print sorted(lis)

front = set([beg])
lis.add(end)
lis.discard(beg)

def almost_done(str1, str2):
    if len(str1) != len(str2):
        return False
    once = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if once:
                return False
            once = True
    return True

while front:
    ws = set()
    for ch in 'abcdefghijklmnopqrstuvwxyz' :
        for index in range(len(beg)):
            print front
            for word in front:
                w =  word[:index] + ch + word[index+1:]
                if w in lis:
                    print w
                    lis.discard(w)
                    ws.add(w)
                    length += 1
                if almost_done(w, end):
                    print length
                    exit(1)
    print ws
    front=set(ws)

print "0"
