N = int(input())
lst = list(map(int, input().split()))
dp = [0] * (N+1)
for i in range(N):
    dp[i+1] = dp[i]
    minval = maxval = lst[i]
    j = i-1
    while j >= 0 and (lst[j] < minval or lst[j] > maxval):
        minval, maxval = min(lst[j], minval), max(lst[j], maxval)
        dp[i+1] = max(dp[i+1], dp[j] + maxval - minval)
        j -= 1
print(dp[-1])