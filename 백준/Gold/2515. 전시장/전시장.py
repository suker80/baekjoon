n, s= map(int,input().split())
import sys
input = sys.stdin.readline
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[0],-x[1]))
idx = [arr[i][0] for i in range(n)]
from bisect import bisect_left

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i + 1
    return i

max_height = arr[-1][0] + 1

dp = [0] * n
dp[0] = arr[0][1]
for i in range(1,n):
    k = index(idx,idx[i] - s )
    for j in range(k-1,-1,-1):
        dp[i] = max(dp[j] + arr[i][1] ,dp[i-1])
        # dp[i] = max(dp[j] + arr[i][1], dp[i - 1])
        break
    if dp[i] == 0:
        dp[i] = max(dp[i - 1], arr[i][1])
print(dp[-1])
