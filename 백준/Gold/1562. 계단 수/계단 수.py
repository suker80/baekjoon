n = int(input())

dp = [[[0] * 10 for _ in range(n + 1)] for _ in range(2 ** 10)]
mod = 1000000000
for i in range(1, 10):
    dp[1 << i][1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(2 ** 10):

            if j < 9:
                dp[k | 1 << j][i][j] += (dp[k][i - 1][j + 1]) % mod
            if j > 0:
                dp[k | 1 << j][i][j] += (dp[k][i - 1][j - 1]) % mod

print(sum(dp[-1][-1]) % mod)
