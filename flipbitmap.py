def flip(a):
    nrows = len(a)
    ncols = len(a[0])
    for row in range(nrows):
        for col in range(ncols/2):
            a[row][col], a[row][ncols-1-col] = a[row][ncols-1-col], a[row][col]

a = [[0, 1, 0, 1, 0, 1, 1, 0], [1, 1, 1, 1, 0, 0, 1, 1]]
for row in a:
    print ' '.join(map(str, row))
flip(a)
for row in a:
    print ' '.join(map(str, row))
