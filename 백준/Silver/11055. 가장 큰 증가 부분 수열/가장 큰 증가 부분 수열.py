n = int(input())

nums = list(map(int,input().split()))

dp = nums[:]
dp[0] = nums[0]
max_value = nums[0]
for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + nums[i])

print(max(dp))
            

dp