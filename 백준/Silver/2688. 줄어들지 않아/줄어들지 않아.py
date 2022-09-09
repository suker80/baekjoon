t = int(input())
dp = [[0] * 10 for _ in range(65)]

for i in range(10):
    dp[1][i] = 1

for i in range(65):
    for j in range(10):

        if dp[j] == 0:
            dp[i][j] = 1

        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

for i in range(t):

    n = int(input())
    print(sum(dp[n]))