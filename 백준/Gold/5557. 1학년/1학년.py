n = int(input())

arr =list(map(int,input().split()))

answer = arr[-1]

count = 0

dp = [[0]* 21 for i in range(n-1)]

dp[0][arr[0]] =1
for i in range(1,n-1):
    k = arr[i]
    for j in range(0,21-k):
        dp[i][j+k] += dp[i-1][j]
    for j in range(k,21):
        dp[i][j-k] += dp[i-1][j]
print(dp[n-2][answer])

