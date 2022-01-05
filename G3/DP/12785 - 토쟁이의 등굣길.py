w, h = map(int, input().split())

x, y = map(int, input().split())
mod = 1_000_007
x -= 1
y -= 1
dp = [[0] * w for _ in range(h)]

dp[0][0] = 1
for i in range(y + 1):
    for j in range(x + 1):
        if i > 0:
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]

for i in range(y, h):
    for j in range(x, w):
        if i > y:
            dp[i][j] += dp[i - 1][j]
        if j > x:
            dp[i][j] += dp[i][j - 1]

print(dp[-1][-1] % mod)
