n,m,k = map(int,input().split())
import sys

dp = [[1]*(n+m) for _ in range(n+m)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
        dp[j][i] = dp[i][j]
if k > dp[n][m] :
    print(-1)
    sys.exit()

skip = ''

def make_string(n,m,k):
    global skip
    if n==0:
        for i in range(m):
            skip += 'z'
        return
    if m==0:
        for j in range(n):
            skip += 'a'
        return
    if dp[n-1][m] >=k:
        skip += 'a'
        make_string(n-1,m,k)
    else :
        skip += 'z'
        make_string(n,m-1,k-dp[n-1][m])


make_string(n,m,k)
print(skip)