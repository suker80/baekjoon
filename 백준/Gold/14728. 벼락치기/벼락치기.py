n, t = map(int, input().split())
problems = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (t + 1) for _ in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, t + 1):
        time, score = problems[i-1]
        if time <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - time] + score)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][t])