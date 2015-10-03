first = [1]
second = [1,1]
third = [1,2,1]
numRows = 100

total = [first]
if numRows == 1:
    print total
if numRows == 2:
    total.append(second)
    print total
else:
    total.append(second)
    for i in range(1,numRows):
        row = [1]
        for j in range(0,len(total[i])-1):
            row.append(total[i][j]+total[i][j+1])
        row.append(1)
        total.append(row)
    for i in total:
        print i

