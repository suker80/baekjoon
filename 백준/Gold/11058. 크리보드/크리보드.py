n = int(input())

dp = [0] * 111

for i in range(1, 101):
    dp[i] = max(dp[i - 1] + 1, dp[i])
    dp[i + 3] = max(dp[i] * 2, dp[i + 3])
    dp[i + 4] = max(dp[i] * 3, dp[i + 4])
    dp[i + 5] = max(dp[i] * 4, dp[i + 5])

print(dp[n])
