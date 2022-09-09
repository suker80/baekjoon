n = int(input())
dp = [float('inf')] * 5001

dp[3] = 1
dp[5] = 1

for i in range(6, 5001):
    dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1)

print(dp[n]) if dp[n] != float('inf') else print(-1)