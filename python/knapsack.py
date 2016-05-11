def knapsack(values, weights, capacity):
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(values)+1)]

    for i in range(1, len(values)+1):
        for j in range(capacity+1):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], values[i-1] +
                               dp[i-1][j-weights[i-1]])
            else:
                dp[i][j] = dp[i-1][j]

    print ''.join('====' * len(dp[0]))
    for d in dp:
        print ''.join('{0: >4}'.format(k) for k in d)
    print ''.join('====' * len(dp[0]))
    return dp[len(values)][capacity]

values = [20, 30, 40, 50, 60, 10, 10, 40, 30, 50]
weights = [3, 4, 7, 1, 4, 10, 5, 4, 6, 3]
capacity = 10
print knapsack(values, weights, capacity)
