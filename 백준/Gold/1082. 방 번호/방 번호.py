n = int(input())

arr = list(map(int, input().split()))

m = int(input())

dp = [0] * 51

for idx, i in enumerate(arr):
    if idx:
        dp[i] = max(dp[i], idx)

answer = 0
for money in range(m + 1):
    for idx, cost in enumerate(arr):
        if money +cost <= m:

            dp[money + cost] = max(dp[money + cost] , (dp[money]* 10) + idx)
            answer = max(answer ,dp[money + cost])
print(answer)