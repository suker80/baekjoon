n,k = map(int,input().split())

dp = [[0] * (n+1) for _ in range(k+1)]

for i in range(n+1):
    dp[1][i] = 1

for i in range(1,n+1):
    for j in range(2,k+1):

        if i == 1 :
            dp[j][i] = j
            continue
        dp[j][i] = (dp[j-1][i] + dp[j][i-1]) % 1e9
print(int(dp[k][n]))