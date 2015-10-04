def get_pos_diagonals(a):
    nrows = len(a)
    ncols = len(a[0])
    for i in range(nrows):
        j = 0
        diag = []
        while i > -1 and j < ncols:
            diag.append(a[i][j])
            i -= 1
            j += 1
        print diag
    for j in range(1, ncols):
        i = nrows-1
        diag = []
        while j < ncols and i > -1:
            diag.append(a[i][j])
            j += 1
            i -= 1
        print diag

a = [[1, 0, 0, 0, 0, 1, 0],
     [0, 1, 0, 0, 0, 1, 0],
     [0, 0, 1, 1, 0, 1, 0],
     [0, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0]]

for row in a:
    print ' '.join(map(str, row))
print "=========="
get_pos_diagonals(a)
print "=========="
cols = 6
rows = 4
print list([(j, i - j) for j in range(cols)] for i in range(cols + rows -1))
