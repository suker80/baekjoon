n = int(input())

arr = list(map(int, input().split()))

dp = [0] * (n+1)

for i in arr:

    dp[i] = dp[i-1] + 1

print(n - max(dp))