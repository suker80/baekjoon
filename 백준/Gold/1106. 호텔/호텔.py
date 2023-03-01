import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(m)]
dp = [float('inf')] * 1234

for money, customer in cities:
    dp[customer] = min(dp[customer], money)

for i in range(len(dp)):
    for j in range(m):
        money, customer = cities[j]

        if i - customer >= 0:
            dp[i] = min(dp[i - customer] + money, dp[i])

answer = float('inf')
for i in range(n, len(dp)):
    answer = min(answer, dp[i])
print(answer)