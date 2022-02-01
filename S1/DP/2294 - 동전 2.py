n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins = list(set(coins))
dp = [float("inf")] * (k + 1)

for coin in coins:
    if coin <k:

        dp[coin] = 1

for i in range(min(coins), k + 1):
    for coin in coins:
        if i - coin > 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k]) if dp[k] != float('inf') else print(-1)
