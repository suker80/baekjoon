n, m = map(int,input().split())

men = list(map(int,input().split()))
women = list(map(int,input().split()))

men.sort()
women.sort()
dp = [[0] * (1012) for _ in range(1012)]

for i in range(1, n + 1):
    for j in range(1, m + 1):

        if i == j:
            dp[i][j] = dp[i - 1][j - 1] + abs(men[i - 1] - women[j - 1])
        elif i > j:
            dp[i][j] = min(dp[i - 1][j - 1] + abs(men[i - 1] - women[j - 1]), dp[i - 1][j])
        else:
            dp[i][j] = min(dp[i - 1][j - 1] + abs(men[i - 1] - women[j - 1]), dp[i][j - 1])

print(dp[n][m])