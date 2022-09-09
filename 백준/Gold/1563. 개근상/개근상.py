n = int(input())

# dp = [2][3][1000]

dp = [[[0] * 1012 for _ in range(3)] for _ in range(2)]
mod = 1_000_000
dp[1][0][0] = 1
dp[0][1][0] = 1
dp[0][0][0] = 1
for i in range(1, 1012):
    dp[0][0][i] = (dp[0][0][i - 1] + dp[0][1][i - 1] + dp[0][2][i - 1]) % mod
    dp[0][1][i] = dp[0][0][i - 1] % mod
    dp[0][2][i] = dp[0][1][i - 1] % mod

    dp[1][0][i] = (dp[1][0][i - 1] + dp[1][1][i - 1] + dp[1][2][i - 1] + \
                   dp[0][0][i - 1] + dp[0][1][i - 1] + dp[0][2][i - 1]) % mod
    dp[1][1][i] = dp[1][0][i - 1] % mod
    dp[1][2][i] = dp[1][1][i - 1] % mod
ans = 0
for i in range(3):
    for j in range(2):
        ans += dp[j][i][n-1]
print(ans % mod)
