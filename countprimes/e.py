def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if(n<2):
        return 0
    if(n==2):
        return 1
    up = n/2+1
    r = [True] * (n+1)
    r[0] = False
    r[1] = False
    for i in range(2, up):
        if r[i]:
            for j in range(i*i, n+1, i):
                # print j
                r[j] = False
    # for i, c in enumerate(r):
        # print (i, c)
    return sum(r)

print countPrimes(20)
